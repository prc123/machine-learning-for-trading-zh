# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: tags,-all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# # 基于因子的 regime 识别（中文阅读版）
#
# **第 1 章 · 1.4 Keeping up with changing market regimes**
#
# **Docker 镜像**：`ml4t`
#
# 本文件是 `factor_regimes.ipynb` 的中文阅读副本。代码 cell、输出和图表保持原样；仅翻译 Markdown 说明文字。
#
# 市场并不是每年都以同一种方式运行。同一个价值策略可能在长期扩张中稳定赚取溢价，也可能连续十年亏损；同一个动量策略也可能在一个季度内回吐多年收益。**Regime** 指收益的联合行为在某段时间内足够稳定，可以被视为同一种环境的时期：均值、波动率和相关性在区间内大致维持，在区间结束时发生移动。
#
# 没有机构官方发布 regime 标签。本 notebook 用**高斯混合模型**（GMM）从数据中估计一个标签。它把每个月的因子收益向量视为来自少数几个多元正态分布之一，并同时推断这些分布以及每个月最可能来自哪一个。输入是 AQR Century of Factor Premia 数据集中九个因子策略的月收益，序列从 1927 年开始。
#
# ## 学习目标
#
# 完成本 notebook 后，你将能够：
#
# - 对月度因子收益面板拟合高斯混合模型，并读取每个月被分配到的簇。
# - 通过比较三个衡量不同目标的标准来选择簇数量，并说明每个标准奖励什么。
# - 将 regime 时间线与有日期的市场事件对照，判断这些簇是否对应读者能识别的历史时期。
# - 度量每个因子在每个簇内的收益，并据此判断哪些因子在环境恶化时彼此分散。
# - 解释为什么在全样本上拟合的标签不能直接作为交易信号。
#
# ## 书籍参考
#
# 第 1 章第 1.4 节 “Keeping up with changing market regimes”。`macro_regimes` 是 companion notebook，改用宏观经济指标估计 regime。
#
# ## 前置条件
#
# - 月度收益序列和标准化（减均值、除标准差），使不同量纲的序列对距离的贡献可比。
# - AQR Century of Factor Premia 数据集。`AQRFactorProvider` 会从 `ML4T_DATA_PATH` 下的 `data/factors/aqr` 读取。若缺失，执行 `uv run python data/factors/aqr_download.py`。
#
# ## 本 notebook 建立了什么，没有建立什么
#
# 模型在完整历史上拟合，再把标签赋回同一段历史。输出描述的是因子空间如何划分，以及有日期的事件落在划分的哪个位置。每个月的标签都受其他所有月份影响，包括之后的月份，所以这些标签描述样本，而不是预测样本。若要构建策略当时可行动的 regime 标签，必须在每个日期只使用当时可得的信息做 walk-forward 拟合；第 6 章之后引入这套机制，案例研究章节会应用它。
#

# %% [markdown]
#
# ## 初始化
#
# AQR provider 通过 `structlog` 记录下载和缓存决策，输出会直接写入 notebook，而不是走标准库 logging。把阈值提高到 `WARNING` 可以让数据加载 cell 更易读，同时保留真正报告问题的日志。
#

# %%
"""Factor-based regime detection - Gaussian mixture regimes over AQR factor returns."""

from __future__ import annotations

import logging
from collections.abc import Iterable
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import polars as pl
import structlog
from IPython.display import Markdown, display
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap
from ml4t.data.providers import AQRFactorProvider
from ml4t.diagnostic.metrics import sharpe_ratio
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

import utils.style as style
from utils.paths import get_output_dir
from utils.reproducibility import set_global_seeds

structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.WARNING))

COLORS = style.COLORS

# %% tags=["parameters"]
# Production defaults (Papermill overrides these when the test suite runs the notebook)
SEED = 42

# %% [markdown]
#
# ### 参数及其作用
#
# `SEED` 固定后续所有估计器的初始化。高斯混合从随机起点用 EM 算法拟合，不同起点可能落入不同局部最优，并交换簇编号；固定随机种子是本 notebook 图形可复现的关键。
#
# `N_REGIMES_GRID` 是要拟合和比较的簇数量集合。2 是能形成划分的最小数量；搜索到 6 为止，目的在于展示标准如何随簇数增加而变化，到 6 时它们已经分开。
#
# `MONTHS_PER_YEAR` 用于把月度统计年化：月均收益乘以它，月度标准差乘以它的平方根。
#
# `ROLLING_VOL_MONTHS` 是绘制波动率序列的移动窗口宽度。12 个月短到能在 regime 内变化，又长到单个异常月不会主导估计。
#

# %%
N_REGIMES_GRID = [2, 3, 4, 5, 6]
MONTHS_PER_YEAR = 12
ROLLING_VOL_MONTHS = 12

OUTPUT_DIR = get_output_dir(1, "factor_regimes")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

set_global_seeds(SEED)

# %% [markdown]
#
# ## 加载因子面板
#
# AQR Century of Factor Premia 数据集包含多个资产类别内构建的多空因子策略月收益，以及直接持有各类资产的收益。provider 返回一行一个月、一列一个策略。
#

# %%
aqr_raw = AQRFactorProvider().fetch("century_premia")

date_range = aqr_raw.select(
    pl.col("timestamp").min().alias("first"), pl.col("timestamp").max().alias("last")
)
print(f"AQR Century of Factor Premia: {aqr_raw.height} months, {aqr_raw.width - 1} series")
print(f"Covering {date_range['first'][0]:%Y-%m} to {date_range['last'][0]:%Y-%m}")

# %% [markdown]
#
# ### 这里使用的九个序列
#
# 其中四个是跨资产多空策略，同时作用于股票指数、债券、货币和商品：
#
# - **Value** 买入相对基本面锚点便宜的资产，卖出昂贵的资产。
# - **Momentum** 买入过去一年上涨的资产，卖出下跌的资产。
# - **Carry** 买入高收益率资产，卖出低收益率资产。
# - **Defensive** 买入低风险资产，卖出高风险资产。
#
# 另外两个只在美国股票市场内应用 value 和 momentum 定义。最后三个是直接持有股票指数、固定收益、商品的收益，而不是多空策略；它们让月份被放入风险环境，而不只是风格环境。
#

# %%
FACTOR_COLUMNS = [
    "All asset classes Value",
    "All asset classes Momentum",
    "All asset classes Carry",
    "All asset classes Defensive",
    "US Stock Selection Value",
    "US Stock Selection Momentum",
    "Equity indices Market",
    "Fixed income Market",
    "Commodities Market",
]
EQUITY_COLUMN = "Equity indices Market"

missing = [c for c in FACTOR_COLUMNS if c not in aqr_raw.columns]
if missing:
    raise ValueError(
        f"The AQR file is missing {missing}. Re-fetch it with "
        "`uv run python data/factors/aqr_download.py`."
    )

# Short names for the figures and tables below; the full AQR column names do not fit on an
# axis.
SHORT_NAMES = {
    "All asset classes Value": "Value",
    "All asset classes Momentum": "Momentum",
    "All asset classes Carry": "Carry",
    "All asset classes Defensive": "Defensive",
    "US Stock Selection Value": "US Value",
    "US Stock Selection Momentum": "US Momentum",
    "Equity indices Market": "Equity",
    "Fixed income Market": "Bonds",
    "Commodities Market": "Commodities",
}

# %% [markdown]
#
# ### 面板中实际有什么
#
# 聚类把每个月视为九维空间中的一个点，因此只有九个序列都有报价的月份才可用。下表逐序列报告起始月、观测数，以及原始文件的均值和标准差。在计算任何结果前先读它：它说明哪些序列缩短了可用历史，以及序列量纲差异有多大；这也是计算距离前先标准化的原因。
#

# %%
coverage = pd.DataFrame(
    [
        {
            "Series": SHORT_NAMES[column],
            "First month": aqr_raw.filter(pl.col(column).is_not_null())["timestamp"].min(),
            "Months quoted": aqr_raw.select(pl.col(column).is_not_null().sum()).item(),
            "Mean (% / month)": aqr_raw.select(pl.col(column).mean()).item() * 100,
            "Std (% / month)": aqr_raw.select(pl.col(column).std()).item() * 100,
        }
        for column in FACTOR_COLUMNS
    ]
).set_index("Series")
coverage["First month"] = pd.to_datetime(coverage["First month"]).dt.strftime("%Y-%m")
coverage.style.format({"Mean (% / month)": "{:.2f}", "Std (% / month)": "{:.2f}"})

# %% [markdown]
#
# ## 为聚类准备面板
#
# 九个序列中任意一个缺失报价的月份会被删除，而不是填充。前向填充会重复上个月收益；重复一个收益并不是恢复了缺失观测，而是发明了一个观测，混合模型会把它当作某个簇的证据。
#
# 随后九个序列标准化为零均值、单位方差。上面的覆盖表说明了原因：面板中最宽序列的月度标准差是最窄序列的数倍，而欧氏距离会被移动幅度最大的坐标主导。标准化让每个序列站在同一基础上，划分反映面板移动的方向，而不是哪个列刚好量纲最大。
#

# %%
factors_pl = aqr_raw.select(["timestamp", *FACTOR_COLUMNS]).sort("timestamp").drop_nulls()

factors_df = factors_pl.select(FACTOR_COLUMNS).to_pandas()
factors_df.index = pd.DatetimeIndex(factors_pl["timestamp"].to_pandas())

factors_scaled = StandardScaler().fit_transform(factors_df)

start_year = factors_df.index.min().year
end_year = factors_df.index.max().year
print(f"Complete months: {len(factors_df)} ({start_year} to {end_year})")

# %% [markdown]
#
# ## 拟合一组混合模型
#
# 不存在能返回“真实 regime 数量”的检验，簇数量是通过比较候选模型做出的建模选择。下面的 helper 对每个候选数量拟合一个混合模型，并记录三个量。
#
# **BIC**（Bayesian information criterion）是拟合对数似然减去自由参数数乘样本量对数的惩罚。**AIC**（Akaike information criterion）思想相同，但每个参数固定惩罚 2。两者都是越低越好；BIC 的惩罚随样本增大，因此在长面板上远比 AIC 更不愿意为额外簇付费。全协方差混合模型消耗参数很快：每个额外簇都需要一个九维均值向量和协方差矩阵，两个标准正是在为这一点定价。
#
# **Silhouette score** 衡量的是另一件事。对每个月，它比较其到同簇其他月份的平均距离，以及到最近的其他簇月份的平均距离，并报告归一化差值；最终得分是所有月份的平均。取值范围 -1 到 1，越高越好；负值表示典型月份离别的簇比离自己的簇更近。它是关于分隔度的几何陈述，与似然无关。
#
# 同一簇数量下还拟合 K-means。它按到质心的距离划分，没有协方差也没有概率；把它的 silhouette 与混合模型并列，可以看出分隔有多少来自混合模型允许拟合的形状。
#
# 最后两列统计三个标准都不看的内容：相邻月份标签不同的频率，以及最空簇包含多少个月。一个标准只能说明划分拟合得多好；划分是否足够稳定以至于可称为 regime，以及每个簇是否有足够月份可描述，是另外两个问题。这两个计数是提出这些问题最便宜的方式。
#


# %%
@dataclass(frozen=True)
class GmmFitResult:
    """One fitted mixture and the three quantities used to compare it against the others."""

    model: GaussianMixture
    labels: np.ndarray
    probabilities: np.ndarray
    bic: float
    aic: float
    silhouette: float


# %%
def fit_gmm_grid(
    x: np.ndarray,
    n_components_list: Iterable[int],
    random_state: int = SEED,
) -> dict[int, GmmFitResult]:
    """Fit one full-covariance mixture per requested cluster count."""
    results: dict[int, GmmFitResult] = {}
    for n in n_components_list:
        model = GaussianMixture(
            n_components=n,
            covariance_type="full",
            random_state=random_state,
            n_init=10,
            reg_covar=1e-6,
        )
        model.fit(x)
        labels = model.predict(x)
        results[n] = GmmFitResult(
            model=model,
            labels=labels,
            probabilities=model.predict_proba(x),
            bic=float(model.bic(x)),
            aic=float(model.aic(x)),
            silhouette=float(silhouette_score(x, labels)),
        )
    return results


# %%
gmm_grid = fit_gmm_grid(factors_scaled, N_REGIMES_GRID)

kmeans_labels = {
    n: KMeans(n_clusters=n, random_state=SEED, n_init=10).fit_predict(factors_scaled)
    for n in N_REGIMES_GRID
}


def switch_count(labels: np.ndarray) -> int:
    """How many times consecutive months carry different labels."""
    return int(np.sum(np.diff(labels) != 0))


selection = pd.DataFrame(
    {
        "Clusters": N_REGIMES_GRID,
        "BIC": [gmm_grid[n].bic for n in N_REGIMES_GRID],
        "AIC": [gmm_grid[n].aic for n in N_REGIMES_GRID],
        "Silhouette (mixture)": [gmm_grid[n].silhouette for n in N_REGIMES_GRID],
        "Silhouette (k-means)": [
            silhouette_score(factors_scaled, kmeans_labels[n]) for n in N_REGIMES_GRID
        ],
        "Switches": [switch_count(gmm_grid[n].labels) for n in N_REGIMES_GRID],
        "Smallest cluster (months)": [
            int(np.bincount(gmm_grid[n].labels).min()) for n in N_REGIMES_GRID
        ],
    }
).set_index("Clusters")
selection.style.format(
    {
        "BIC": "{:,.0f}",
        "AIC": "{:,.0f}",
        "Silhouette (mixture)": "{:.3f}",
        "Silhouette (k-means)": "{:.3f}",
    }
)

# %% [markdown]
#
# ### 相互对照地阅读三个标准
#
# 下方柱状图绘制表格中的三列。两个信息准则使用缩放后的纵轴，因为候选模型之间的差异相对整体水平很小，如果从 0 开始画就看不清；silhouette 面板使用包含 0 的自然刻度。
#


# %%
def plot_selection_criterion(ax: Axes, values: list[float], label: str, best: str) -> None:
    """Draw one criterion as bars, highlighting the count it favours."""
    bars = ax.bar(N_REGIMES_GRID, values, color=COLORS["recede"])
    chosen = int(np.argmin(values)) if best == "min" else int(np.argmax(values))
    bars[chosen].set_color(COLORS["amber"])
    ax.set_xlabel("Clusters")
    ax.set_ylabel(label)
    ax.set_xticks(N_REGIMES_GRID)


# %%
fig, axes = plt.subplots(1, 3, figsize=style.FIGSIZE["triple_h_tall"])

plot_selection_criterion(axes[0], selection["BIC"].tolist(), "BIC (lower is better)", "min")
plot_selection_criterion(axes[1], selection["AIC"].tolist(), "AIC (lower is better)", "min")
plot_selection_criterion(
    axes[2], selection["Silhouette (mixture)"].tolist(), "Silhouette (higher is better)", "max"
)
for ax, values in ((axes[0], selection["BIC"]), (axes[1], selection["AIC"])):
    span = values.max() - values.min()
    ax.set_ylim(values.min() - 0.15 * span, values.max() + 0.15 * span)

style.add_message_title(
    axes[0],
    "BIC, AIC and silhouette do not pick the same number of regimes",
    subtitle="Highlighted bar is the count each criterion favours; note the zoomed axes on BIC and AIC",
)
style.show_with_alt(
    fig,
    "Three bar charts over cluster counts two to six. BIC rises with the count, AIC falls "
    "with it, and the silhouette score falls sharply after the smallest count and hovers "
    "near zero at the larger ones.",
)

# %%
bic_choice = int(selection["BIC"].idxmin())
aic_choice = int(selection["AIC"].idxmin())
silhouette_choice = int(selection["Silhouette (mixture)"].idxmax())
display(
    Markdown(
        f"BIC is lowest at **{bic_choice} clusters** and the silhouette score is highest at "
        f"**{silhouette_choice}**, while AIC keeps falling out to **{aic_choice}**, the "
        "largest count fitted."
    )
)

# %% [markdown]
#
# 当标准不一致时，选择取决于模型用途。AIC 面向预测似然，只要继续增加簇能提高似然就会继续买入；最后两列显示它在较大簇数下买到的是标签更频繁切换的划分，且至少有一个簇月份太少而难以描述。一小段样本配上自己的协方差可以改善拟合，但不是一个能命名的 regime。
#
# BIC 的样本缩放惩罚和 silhouette 的分隔检验都要求簇足够清晰，能经得起描述；如果 regime 要出现在风险报告中，它必须满足这一点。基于这个理由，本 notebook 后续使用两簇模型；下一节时间线展示更大簇数如何处理新增簇。
#

# %%
N_REGIMES_SELECTED = 2
# fit_gmm_grid fitted exactly the counts in N_REGIMES_GRID, and the swimlane and label
# cells below read gmm_grid[N_REGIMES_SELECTED]. Narrowing the grid without moving this
# constant reaches them as a KeyError.
assert N_REGIMES_SELECTED in N_REGIMES_GRID, (
    f"N_REGIMES_SELECTED={N_REGIMES_SELECTED} was never fitted; N_REGIMES_GRID={N_REGIMES_GRID}"
)

# %% [markdown]
#
# ## 每个簇数量如何划分样本
#
# 下方每条色带对应一个拟合模型。月份被涂在它所属簇的行中，因此连续水平段表示模型维持在同一个 regime，斑点状区段表示频繁切换。比较色带可以看出额外簇买到了什么：新增簇是切出一个可识别时代，还是散布在整个世纪。
#


# %%
def decade_ticks(dates: pd.DatetimeIndex) -> tuple[list[int], list[str]]:
    """Positions and labels for the first month of each decade in a monthly index."""
    years = dates.year.tolist()
    ticks = [
        j for j, year in enumerate(years) if year % 10 == 0 and (j == 0 or years[j - 1] != year)
    ]
    return ticks, [str(years[j]) for j in ticks]


# %%
def draw_swimlanes(ax: Axes, rows: np.ndarray, n_rows: int, cmap: ListedColormap) -> None:
    """Shade each month in the row given by *rows*, one row per regime."""
    matrix = np.zeros((n_rows, len(rows)))
    matrix[rows, np.arange(len(rows))] = 1
    ax.imshow(
        matrix,
        aspect="auto",
        cmap=cmap,
        vmin=0,
        vmax=1,
        extent=(0, len(rows), -0.5, n_rows - 0.5),
        interpolation="nearest",
        origin="lower",
    )
    for boundary in range(1, n_rows):
        ax.axhline(y=boundary - 0.5, color=COLORS["bg_light"], linewidth=1.5)


# %%
lane_cmap = ListedColormap([COLORS["bg_light"], COLORS["blue"]])
ticks, tick_labels = decade_ticks(factors_df.index)

fig, axes = plt.subplots(
    len(N_REGIMES_GRID),
    1,
    figsize=(style.PAGE_WIDTH, 1.0 * len(N_REGIMES_GRID) + 1.0),
    sharex=True,
)
for ax, n in zip(axes, N_REGIMES_GRID):
    draw_swimlanes(ax, gmm_grid[n].labels, n, lane_cmap)
    ax.set_yticks([])
    ax.set_ylabel(f"K = {n}", rotation=0, ha="right", va="center")

axes[-1].set_xticks(ticks)
axes[-1].set_xticklabels(tick_labels)
axes[-1].set_xlabel("Year")
style.add_message_title(
    axes[0],
    "Adding clusters makes the timeline switch more often, not cleaner",
    subtitle="One panel per fitted model; a month is shaded in the row of the cluster it was assigned",
)
style.show_with_alt(
    fig,
    "Five stacked panels, one per cluster count. The two-cluster panel shows one row "
    "occupied most of the time and the other taking short scattered stretches. Each panel "
    "below it is more finely speckled than the one above, with no row holding a long "
    "uninterrupted stretch by the largest count.",
)

# %% [markdown]
#
# 没有任何一条色带随着簇数增加而稳定下来。新增簇并没有切出早期模型合并的时代，而是从整个世纪各处取走月份，所以每个面板都比上一个更细碎。混合模型没有时间概念，也没有任何机制偏好月份保持邻居的标签，因此更多簇不可能自动产生更长区段。这个缺口正是后文讨论 regime 持续时间时指向隐马尔可夫模型的原因：HMM 提供了这个模型缺少的机制。
#

# %% [markdown]
#
# ## 两簇模型：risk-on 与 risk-off
#
# 混合模型返回的是簇编号，不是名称，编号本身没有含义，换随机种子可能交换编号。要描述两个簇，必须用模型外的信息识别它们；自然选择是能说明市场整体状态的序列：每个簇内持有股票指数的平均收益。**Risk-on** 和 **risk-off** 是市场对这些环境的常用称呼，分别指投资者增加风险资产暴露和减少暴露的时期。
#
# 这种命名使用完整样本，和拟合一样。它描述划分最终是什么，而不是一条 1929 年就能应用的规则。
#

# %%
labels_2 = gmm_grid[N_REGIMES_SELECTED].labels
equity_returns = factors_df[EQUITY_COLUMN]

mean_equity_by_cluster = equity_returns.groupby(labels_2).mean()
risk_on_cluster = int(mean_equity_by_cluster.idxmax())
risk_off_cluster = int(mean_equity_by_cluster.idxmin())

regime_name = pd.Series(
    np.where(labels_2 == risk_on_cluster, "Risk-on", "Risk-off"),
    index=factors_df.index,
    name="regime",
)

# %% [markdown]
#
# ### 时间线与有日期事件对照
#
# 上方面板是同一种泳道色带，限制为两簇模型，并标出七个有日期的片段。下方面板是股票指数收益累计乘积的对数刻度曲线，颜色对应该月被分配的 regime。对数刻度让 1930 年代与 2010 年代可比：相同垂直距离代表相同百分比变动，因此同样幅度的下跌在世纪中任何位置占用的横轴空间相同。
#

# %%
HISTORICAL_EVENTS = {
    1929: ("Great Crash", "top"),
    1937: ("Recession", "bottom"),
    1973: ("Oil crisis", "top"),
    1987: ("Black Monday", "bottom"),
    2000: ("Dot-com peak", "top"),
    2008: ("Global financial crisis", "bottom"),
    2020: ("COVID-19", "top"),
}


# %%
def mark_events(ax: Axes, years: list[int]) -> None:
    """Draw a rule and a label at the first month of each dated episode."""
    for event_year, (event_label, side) in HISTORICAL_EVENTS.items():
        position = next((j for j, year in enumerate(years) if year == event_year), None)
        if position is None:
            continue
        ax.axvline(x=position, color=COLORS["neutral"], alpha=0.6, linewidth=1.0)
        ax.annotate(
            event_label,
            xy=(position, 1.7 if side == "top" else -0.7),
            ha="center",
            va="bottom" if side == "top" else "top",
            fontsize=7,
            color=COLORS["neutral"],
        )


# %%
def plot_by_regime(ax: Axes, values: np.ndarray, in_risk_on: np.ndarray) -> None:
    """Draw one line whose every segment takes the colour of the month it ends in.

    The segment from month t-1 to month t is the move month t produced, so month t's regime
    is the one that colours it. Masking each regime into its own line instead would drop
    every segment that spans a transition, and would draw nothing at all for a one-month
    episode, which is most of them here.
    """
    y = np.asarray(values, dtype=float)
    points = np.column_stack([np.arange(len(y)), y]).reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    drawable = np.isfinite(segments[:, :, 1]).all(axis=1)
    colours = np.where(in_risk_on[1:], COLORS["recede"], COLORS["blue"])
    ax.add_collection(LineCollection(segments[drawable], colors=colours[drawable], linewidths=1.2))
    finite = y[np.isfinite(y)]
    ax.set_xlim(0, len(y) - 1)
    ax.set_ylim(finite.min() * 0.9, finite.max() * 1.1)


# %%
fig, (ax_band, ax_equity) = plt.subplots(
    2, 1, figsize=style.FIGSIZE["dual_v"], height_ratios=[1, 2], sharex=True
)

rows = np.where(labels_2 == risk_on_cluster, 1, 0)
draw_swimlanes(ax_band, rows, 2, lane_cmap)
ax_band.set_yticks([0, 1])
ax_band.set_yticklabels(["Risk-off", "Risk-on"])
ax_band.set_ylim(-0.5, 1.5)
mark_events(ax_band, factors_df.index.year.tolist())

cumulative = (1 + equity_returns).cumprod()
in_risk_on = labels_2 == risk_on_cluster
plot_by_regime(ax_equity, cumulative.to_numpy(), in_risk_on)
ax_equity.set_yscale("log")
ax_equity.set_ylabel("Growth of 1 unit invested (log scale)")
ax_equity.set_xlabel("Year")
ax_equity.set_xticks(ticks)
ax_equity.set_xticklabels(tick_labels)
ax_equity.grid(True, alpha=0.3)

style.add_message_title(
    ax_band,
    "Risk-off months come in short bursts, not in long bear markets",
    subtitle="Upper: assigned regime. Lower: cumulative equity index return, coloured by regime",
)
style.show_with_alt(
    fig,
    "A two-row regime band above a rising cumulative return curve on a log scale. The "
    "risk-off row is occupied in many short bursts spread across the whole century rather "
    "than in a few long blocks, and the curve is drawn dark through those same stretches.",
)

# %% [markdown]
#
# ## 每个 regime 内的波动率
#
# regime 标签只有对应风险经理会行动的内容才值得保留；第一个检查是两个环境中市场波动幅度是否不同。下方序列是股票指数收益在 trailing 12 个月窗口内的标准差，乘以根号 12 年化，颜色对应当月 regime。虚线是每个 regime 内该滚动序列的平均。
#

# %%
rolling_vol = equity_returns.rolling(ROLLING_VOL_MONTHS).std() * np.sqrt(MONTHS_PER_YEAR)

rolling_vol_by_regime = (
    rolling_vol.groupby(regime_name)
    .agg(["mean", "median", "max"])
    .rename(columns={"mean": "Mean (%)", "median": "Median (%)", "max": "Max (%)"})
    .mul(100)
    .loc[["Risk-on", "Risk-off"]]
)
rolling_vol_by_regime.index.name = "Regime"
rolling_vol_by_regime.style.format("{:.1f}")

# %%
fig, (ax_band, ax_vol) = plt.subplots(
    2, 1, figsize=style.FIGSIZE["dual_v"], height_ratios=[1, 3], sharex=True
)

draw_swimlanes(ax_band, rows, 2, lane_cmap)
ax_band.set_yticks([0, 1])
ax_band.set_yticklabels(["Risk-off", "Risk-on"])
ax_band.set_ylim(-0.5, 1.5)

plot_by_regime(ax_vol, rolling_vol.to_numpy() * 100, in_risk_on)
for regime, colour in (("Risk-on", COLORS["copper"]), ("Risk-off", COLORS["amber"])):
    ax_vol.axhline(
        rolling_vol_by_regime.loc[regime, "Mean (%)"],
        color=colour,
        linestyle="--",
        linewidth=1.2,
        label=f"{regime} average",
    )
ax_vol.set_ylabel(f"Trailing {ROLLING_VOL_MONTHS}-month volatility, annualized (%)")
ax_vol.set_xlabel("Year")
ax_vol.set_xticks(ticks)
ax_vol.set_xticklabels(tick_labels)
ax_vol.legend(loc="upper right")
ax_vol.grid(True, alpha=0.3)

style.add_message_title(
    ax_band,
    "The risk-off cluster sits on the higher-volatility stretches of the century",
    subtitle=f"Trailing {ROLLING_VOL_MONTHS}-month standard deviation of the equity index, "
    f"annualized by the square root of {MONTHS_PER_YEAR}",
)
style.show_with_alt(
    fig,
    "A two-row regime band above a rolling volatility series in percent. The dark risk-off "
    "segments concentrate on the peaks of the volatility series, and the risk-off average "
    "rule sits above the risk-on one.",
)

# %% [markdown]
#
# ### 图 1.5 输入
#
# 书籍印刷版图 1.5 由书稿仓库中的
# `book/01_process_is_edge/figures/scripts/generate_figure_1_5_factor_regimes_volatility.py`
# 绘制。它读取下方写出的数组，因此书籍构建使用本 notebook 的拟合结果，而不是重新估计混合模型。
#

# %%
ARTIFACT_DIR = OUTPUT_DIR / "figure_1_5"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
np.savez(
    ARTIFACT_DIR / "inputs.npz",
    dates=factors_df.index.astype("datetime64[ns]").astype("int64"),
    labels_2=np.asarray(labels_2, dtype=np.int64),
    good_regime=np.int64(risk_on_cluster),
    rolling_vol=rolling_vol.to_numpy(dtype=float),
    risk_on_mean_vol=float(rolling_vol_by_regime.loc["Risk-on", "Mean (%)"]) / 100,
    risk_off_mean_vol=float(rolling_vol_by_regime.loc["Risk-off", "Mean (%)"]) / 100,
    start_year=np.int64(start_year),
    end_year=np.int64(end_year),
)

# %% [markdown]
#
# ## 每个因子在每个 regime 的收益
#
# 波动率检查说明两个环境中市场移动幅度不同。对组合构建更有用的问题是策略在两种环境中是否表现不同：在两种环境都赚溢价的是分散工具；只在平静环境赚溢价的，实际上是对市场状态的变相加杠杆。
#
# 下方每根柱子是一个序列在某个 regime 月份上的月均收益乘以 12。它是一组月份内的平均，不是在 regime 之间切换的策略收益；实时可用的规则不可能产生这个划分。
#

# %%
annualized_by_regime = (
    factors_df.groupby(regime_name).mean().mul(MONTHS_PER_YEAR * 100).rename(columns=SHORT_NAMES)
).loc[["Risk-on", "Risk-off"]]

# %%
fig, ax = plt.subplots(figsize=style.FIGSIZE["single_tall"])

x = np.arange(annualized_by_regime.shape[1])
width = 0.38
ax.bar(
    x - width / 2,
    annualized_by_regime.loc["Risk-on"],
    width,
    label="Risk-on",
    color=COLORS["recede"],
)
ax.bar(
    x + width / 2,
    annualized_by_regime.loc["Risk-off"],
    width,
    label="Risk-off",
    color=COLORS["blue"],
)
ax.set_xticks(x)
ax.set_xticklabels(annualized_by_regime.columns, rotation=30, ha="right")
ax.set_ylabel("Mean return within the regime, annualized (%)")
style.zero_line(ax)
ax.legend(loc="upper right")
ax.grid(axis="y", alpha=0.3)

style.add_message_title(
    ax,
    "Value and bonds hold up in the risk-off months; carry and defensive do not",
    subtitle="Mean monthly return within each regime times twelve, by series",
)
style.show_with_alt(
    fig,
    "Paired bars per factor. Value and bonds have taller risk-off bars than risk-on bars; "
    "momentum, equity, carry and defensive have taller risk-on bars, with carry and "
    "defensive falling below zero in the risk-off months.",
)

# %%
annualized_by_regime.T.style.format("{:+.1f}")

# %% [markdown]
#
# 平静市场视为安全收益的两个策略：collect yield spread 的 carry，以及做多低风险资产的 defensive，在环境恶化时停止支付。Value 和债券相反，收益更高。
#
# 因此，策略在完整样本的平均收益不能说明它是否会在组合需要它的环境中存在。要找出答案，必须按环境条件化并观察；这也正是即使 regime 标签不能被交易，它仍值得估计的原因。
#

# %% [markdown]
#
# ## Regime 统计
#
# 下表仅通过股票指数刻画每个 regime。所有统计都作用在同一串收益上：把模型分配给该 regime 的月份按日期顺序拼接，并删除另一个 regime 的月份。
#
# 对于均值、标准差和 Sharpe ratio，这是普通条件统计；一组月份的平均不依赖顺序。**最大回撤**不同，它是路径统计：复利这串收益、跟踪滚动高点，并报告从高点到之后某点的最大百分比跌幅。把剔除缺口后拼接的序列复利，不等于复利原指数，因此下表数字描述的是一个只在某个 regime 持有股票、在其他 regime 空仓的投资者。表后一节展示两种读法差距有多大。
#


# %%
def drawdown_path(returns: pd.Series) -> pd.Series:
    """Fractional decline from the running high-water mark of the compounded stream."""
    wealth = (1 + returns).cumprod()
    return wealth / wealth.cummax() - 1


# %%
regime_statistics = pd.DataFrame(
    [
        {
            "Regime": regime,
            "Months": int(len(returns)),
            "Share of sample": len(returns) / len(equity_returns),
            "Return, annualized": returns.mean() * MONTHS_PER_YEAR,
            "Volatility, annualized": returns.std() * np.sqrt(MONTHS_PER_YEAR),
            "Sharpe ratio": sharpe_ratio(returns, periods_per_year=MONTHS_PER_YEAR),
            "Max drawdown": float(drawdown_path(returns).min()),
        }
        for regime, returns in (
            (name, equity_returns[regime_name == name]) for name in ("Risk-on", "Risk-off")
        )
    ]
).set_index("Regime")
regime_statistics.style.format(
    {
        "Share of sample": "{:.1%}",
        "Return, annualized": "{:+.1%}",
        "Volatility, annualized": "{:.1%}",
        "Sharpe ratio": "{:.2f}",
        "Max drawdown": "{:.1%}",
    }
)

# %%
pooled_vol_ratio = (
    regime_statistics.loc["Risk-off", "Volatility, annualized"]
    / regime_statistics.loc["Risk-on", "Volatility, annualized"]
)
rolling_vol_ratio = (
    rolling_vol_by_regime.loc["Risk-off", "Mean (%)"]
    / rolling_vol_by_regime.loc["Risk-on", "Mean (%)"]
)
display(
    Markdown(
        f"Risk-off volatility is **{pooled_vol_ratio:.2f}x** risk-on volatility measured on "
        f"the pooled monthly returns, against **{rolling_vol_ratio:.2f}x** measured as the "
        "average of the trailing twelve-month series."
    )
)

# %% [markdown]
#
# 这两个比例回答不同问题，读者应当预期它们不同。滚动序列让每个月与周围 11 个月平均，一个极端月会轻微抬高 12 个窗口；合并标准差则让这个月以完整幅度进入一次。合并值描述在 regime 内持续持有的组合经历；滚动值是监控面板会显示的值。单独报告任何一个都可以辩护；报告其中一个并称之为“唯一的”波动率比例则不行。
#

# %% [markdown]
#
# ### 受限回撤实际度量什么
#
# Risk-off regime 的回撤很大，引用之前值得看清它来自哪里。下方 cell 找出受限序列的高水位、跌幅最深的月份，并把同一段时间内原指数本身的回撤放在旁边。
#

# %%
risk_off_returns = equity_returns[regime_name == "Risk-off"]
risk_off_drawdown = drawdown_path(risk_off_returns)
trough_month = risk_off_drawdown.idxmin()
peak_month = (1 + risk_off_returns).cumprod().loc[:trough_month].idxmax()

restricted_drawdown = float(risk_off_drawdown.min())
index_over_span = equity_returns.loc[peak_month:trough_month]
index_drawdown = float(drawdown_path(index_over_span).min())
display(
    Markdown(
        f"The restricted stream peaks in **{peak_month:%B %Y}** and reaches its low in "
        f"**{trough_month:%B %Y}**, a fall of "
        f"**{abs(restricted_drawdown):.1%}** spread over "
        f"**{trough_month.year - peak_month.year} years**. Over the same span the equity "
        f"index itself fell at most **{abs(index_drawdown):.1%}** from its own high-water "
        "mark."
    )
)

# %% [markdown]
#
# 没有人真实经历过第一个数字代表的路径。Risk-off 月份由混合模型分配决定，不是由股票收益符号决定，所以这串收益既包含亏损也包含盈利，其月均收益为正。它缺少的是中间月份；关闭这些缺口会把一个十年的亏损立即放在下一个十年的亏损旁边，中间没有恢复期。复利之后，多个独立片段读起来像一次不间断下跌。
#
# 这个统计没有错；它是所计算对象的真实回撤。但对象是本 notebook 的构造，把它当成股市崩溃就会被误导，而表格从未说明自己指的是哪个对象。
#
# 这是通用形式：条件统计继承条件化的假设。均值能幸存，因为均值不关心项的顺序。任何读取路径的统计，包括回撤、持续长度、恢复时间、止损，在路径被切开之后都是另一个统计；不说明这一点就报告，就是一个数字被读成另一个数字的典型方式。
#

# %% [markdown]
#
# ## Regime 持续多久
#
# 只有 regime 持续得足够久，标签才可能被策略利用。下面的 **episode** 定义为连续携带同一标签的最大月份区间；表格报告每个 regime 的 episode 数量和持续长度。
#

# %%
episode_id = (labels_2 != np.roll(labels_2, 1)).cumsum()
episode_lengths = (
    pd.DataFrame({"regime": regime_name.to_numpy(), "episode": episode_id})
    .groupby(["regime", "episode"])
    .size()
    .rename("months")
    .reset_index()
)

duration = (
    episode_lengths.groupby("regime")["months"]
    .agg(["mean", "max", "count"])
    .rename(
        columns={"mean": "Mean length (months)", "max": "Longest (months)", "count": "Episodes"}
    )
    .loc[["Risk-on", "Risk-off"]]
)
duration.index.name = "Regime"
duration.style.format({"Mean length (months)": "{:.1f}"})

# %%
switches = int(np.sum(np.diff(labels_2) != 0))
months_between_switches = len(labels_2) / switches
display(
    Markdown(
        f"The two-cluster model changes regime **{switches}** times over "
        f"{end_year - start_year} years, about once every "
        f"**{months_between_switches:.1f} months**."
    )
)

# %% [markdown]
#
# 这个发现决定了模型用途。一年变化几次的标签不能驱动重新配置：每次切换都要支付换手成本，包括一个月后又被模型反转的切换；无论 regime 判断是否正确，交易成本都会到来。同一标签作为观察历史的透镜和风险报告的一个输入仍然有用，这正是第 1.4 节主张的用法。
#
# 若模型是为行动而建，会采用不同构建方式。它会携带让停留在当前 regime 比离开更可能的转移结构，标准选择是隐马尔可夫模型；并且按时间向前拟合，使每个月标签只使用之前月份。`09_model_based_features/11_hmm_regimes` 构建前者，`09_model_based_features/13_regime_as_feature` 把结果转成下游模型可读取的特征。
#

# %% [markdown]
#
# ## 关键结论
#
# - **簇数量是决策，不是估计。** BIC、AIC 和 silhouette 奖励不同目标，因此会不一致；选择目标与标签用途匹配的标准，并说明你选了哪个、为什么。
# - **簇编号在模型外的东西命名前没有含义。** 这里用每个簇的平均股票收益命名；不同种子可以在不改变划分的情况下重新编号。
# - **信任因子均值前先按环境条件化。** 策略的全样本溢价可能完全来自一种环境，这在合并数字中不可见，却决定它是否能分散风险。
# - **说明条件统计如何构造。** 把收益流限制在某个 regime 月份并拼接，会产生只有在该 regime 持有才可能经历的回撤；同一个数字是否误导，取决于是否说明这个构造。
# - **全样本拟合买到的是描述，不是预测。** 这里每个标签都受之后月份影响，因此不能作为特征。Walk-forward 拟合才让它们可用；第 6 章之后介绍它。
#
# **已知限制。** 混合模型没有时间概念：它可以把 1932 年 1 月和 2019 年 1 月分到同一簇，也没有机制偏好月份保留上月标签，因此 episode 很短。AQR 序列是月频，无法分辨比月更快的现象。面板长达一个世纪，资产类别构成和市场微观结构都发生了显著变化；模型把 1927 年和 2024 年视为来自同一组分布。
#
# **下一步**：`macro_regimes` 用宏观经济指标而不是因子收益研究同一问题，并用已实现股票波动率检验簇。
#

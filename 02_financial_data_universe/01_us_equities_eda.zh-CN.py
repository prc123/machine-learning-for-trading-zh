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

# %% [markdown] tags=[]
# > **中文阅读版**：本文件是 `01_us_equities_eda.ipynb` 的 Markdown 翻译副本。代码、输出、图表和路径保持原样；专有名词和标识符保留英文。
# # 美股 — 探索性数据分析
#
# **Docker 镜像**：`ml4t`
#
# ## 目的
#
# 对**美股面板数据 (panel)** 进行剖析：其 schema、其价格约定，以及——决定它能否支撑回测的关键所在——其覆盖范围随时间变化的形态。
#
# 该面板数据来自已停用的 Quandl WIKI 日线 (end-of-day) 文件：由社区维护、免费，且已于 2018 年 3 月停止发布。这一来源绝非细枝末节。它决定了面板能告诉我们什么、不能告诉我们什么，而本 notebook 的任务正是查明究竟是哪一种。
#
# ## 学习目标
#
# - 通过 `data.load_us_equities` 加载面板数据，并检查其标准 schema。
# - 区分原始价格列与经拆股/分红调整后的价格列。
# - 绘制面板每年覆盖的代码 (symbol) 数量，以及代码进入和离开面板的时间。
# - 将覆盖范围图表解读为关于*数据采集过程*的证据，而非关于市场本身的证据。
# - 检查整个面板的 OHLC 不变量与空值率。
#
# ## 本 notebook 与 `15_survivorship_bias_detection` 的关联
#
# 本 notebook 确定**文件中有什么**。它在结尾处揭示覆盖记录中的一处异常，但刻意不对此做出解答。
#
# `15_survivorship_bias_detection` 承接该异常并提出后续问题：*鉴于面板记录了关于离开它的代码的哪些信息，忽略这些代码的回测会有多大的偏差？* 请先阅读本篇；它篇幅更短，并为该问题做了铺垫。
#
# ## 书籍参考
#
# §2.2，“资产类别市场数据全景”（The asset-class market data landscape）——其中关于股票的部分。
#
# ## 前置条件
#
# `data` 包需位于 `PYTHONPATH` 中；面板的 parquet 文件需存在于
# `ML4T_DATA_PATH/equities/market/us_equities/`。若缺失，请运行
# `python data/equities/market/us_equities/download.py`。

# %% tags=[]
"""US Equities — Exploratory data analysis of the US equities panel."""

import plotly.graph_objects as go
import polars as pl
from IPython.display import Markdown, display

from data import load_us_equities
from utils.data_quality import check_ohlc_invariants
from utils.style import COLORS, show_plotly_with_alt

# %% tags=["parameters"]
# Production defaults — Papermill injects overrides for CI
MAX_SYMBOLS = 0  # 0 = all symbols; a positive value subsets for fast execution

# %% [markdown] tags=[]
# ## 1. 加载与检查

# %% tags=[]
wiki = load_us_equities()

if MAX_SYMBOLS:
    keep = sorted(wiki["symbol"].unique().to_list())[:MAX_SYMBOLS]
    wiki = wiki.filter(pl.col("symbol").is_in(keep))

print("=== US equities panel ===")
print(f"Shape: {wiki.shape}")
print(f"Columns: {wiki.columns}")

# %% tags=[]
print("Schema:")
for col, dtype in wiki.schema.items():
    print(f"  {col}: {dtype}")

# %% [markdown] tags=[]
# ### 原始价格与调整后价格
#
# 该面板同时保留了**两种**价格约定。选用哪一种并非风格偏好——它改变的是数字本身。
#
# | 列类型 | 列 | 用途 |
# |---|---|---|
# | 原始 | `open`, `high`, `low`, `close`, `volume` | 在实际成交价格水平上进行分析 |
# | 调整后 | `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_volume` | 收益率计算与回测 |
#
# 调整后的列旨在吸收拆股与分红的影响，使得跨越公司行为 (corporate action) 计算出的收益率是投资者本可实际获得的收益率。计算收益率请使用 `adj_*`；当你需要交易在当时实际成交的价格时，请使用原始列。
#
# 该面板还直接附带了公司行为的两个原始输入项：`ex-dividend` 与 `split_ratio`，这使得 `02_corporate_actions` 能够通过一个具体算例验证调整结果，而不必想当然地信任。该检查在 AAPL 上通过，但并非处处通过——参见 `15_survivorship_bias_detection` §3。

# %% [markdown] tags=[]
# ## 2. 覆盖范围：横截面

# %% tags=[]
print("=== Coverage ===")
print(f"Unique symbols: {wiki['symbol'].n_unique():,}")
print(f"Date range: {wiki['timestamp'].min()} to {wiki['timestamp'].max()}")
print(f"Total rows: {len(wiki):,}")

# %% tags=[]
# One row per symbol: when it enters the panel, when it leaves, how long it trades.
dataset_end = wiki.select(pl.col("timestamp").max()).item()

lifespans = (
    wiki.group_by("symbol")
    .agg(
        [
            pl.len().alias("days"),
            pl.col("timestamp").min().alias("first_date"),
            pl.col("timestamp").max().alias("last_date"),
            pl.col("adj_close").mean().alias("avg_price"),
        ]
    )
    .with_columns(
        [
            pl.col("first_date").dt.year().alias("entry_year"),
            pl.col("last_date").dt.year().alias("exit_year"),
            (pl.col("last_date") < dataset_end).alias("leaves_early"),
        ]
    )
)

# %% [markdown] tags=[]
# 每个代码的覆盖分布——交易天数与平均调整后价格。

# %% tags=[]
lifespans.select(["days", "avg_price"]).describe()

# %% [markdown] tags=[]
# ## 3. 覆盖范围随时间的变化
#
# 上面的横截面说明了面板*总共*持有多少代码，却对**何时**只字未提。同样的总数，既可能对应每个代码在每一年都有报价，也可能对应一个随公司上市与退市而扩张收缩的投资范围 (universe)。这是两种截然不同的数据集，而只有其中一种能够支撑回测。
#
# 两种视图可以回答这个问题：
#
# - **投资范围规模** — 每个日历年度有多少个不同的代码有报价。
# - **进入与退出** — 每年有多少代码记录其*首次*观测，又有多少代码记录其*最后一次*观测。
#
# 对于一个跟踪真实股票市场的面板而言，这两种流转都应持续不断：每年都有公司 IPO，每年也都有公司被收购或倒闭。

# %% tags=[]
active_by_year = (
    wiki.select(pl.col("timestamp").dt.year().alias("year"), "symbol")
    .group_by("year")
    .agg(pl.col("symbol").n_unique().alias("active"))
    .sort("year")
)

peak = active_by_year.sort("active", descending=True).head(1)
peak_year, peak_active = peak["year"][0], peak["active"][0]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=active_by_year["year"].to_list(),
        y=active_by_year["active"].to_list(),
        mode="lines",
        name="Symbols quoted",
        line=dict(color=COLORS["blue"], width=2),
    )
)
fig.add_annotation(
    x=peak_year,
    y=peak_active,
    text=f"Peak: {peak_active:,} symbols ({peak_year})",
    showarrow=True,
    arrowhead=2,
    ax=-70,
    ay=-30,
    font=dict(color=COLORS["copper"]),
)
fig.update_layout(
    title="Distinct symbols quoted per year",
    xaxis_title="Year",
    yaxis_title="Distinct symbols",
    height=420,
)
show_plotly_with_alt(
    fig,
    "A line of the number of distinct symbols quoted each year. It rises steadily from the "
    "early 1960s, reaches its highest point a few years before the panel ends, and falls "
    "away sharply after that.",
)

# %% [markdown] tags=[]
# 投资范围增长了五十年，见顶，随后开始衰退。市场不会如此，*数据采集过程*才会如此。记住这一点；下一张图表将点明其机制。

# %% tags=[]
entries = (
    lifespans.group_by("entry_year").agg(pl.len().alias("entries")).rename({"entry_year": "year"})
)
# A symbol whose last observation is the panel's last date has not left — it is still quoted.
exits = (
    lifespans.filter(pl.col("leaves_early"))
    .group_by("exit_year")
    .agg(pl.len().alias("exits"))
    .rename({"exit_year": "year"})
)

years = pl.DataFrame(
    {"year": list(range(lifespans["entry_year"].min(), lifespans["exit_year"].max() + 1))}
)
flows = (
    years.join(entries, on="year", how="left")
    .join(exits, on="year", how="left")
    .with_columns([pl.col("entries").fill_null(0), pl.col("exits").fill_null(0)])
    .sort("year")
)

first_exit_year = flows.filter(pl.col("exits") > 0)["year"].min()

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=flows["year"].to_list(),
        y=flows["entries"].to_list(),
        name="Entries (first observation)",
        marker_color=COLORS["slate"],
    )
)
fig.add_trace(
    go.Bar(
        x=flows["year"].to_list(),
        y=[-n for n in flows["exits"].to_list()],
        name="Exits (last observation)",
        marker_color=COLORS["copper"],
    )
)
fig.add_vline(x=first_exit_year - 0.5, line_dash="dash", line_color=COLORS["amber"])
fig.add_annotation(
    x=first_exit_year - 0.5,
    y=max(flows["entries"].to_list()),
    text=f"First exit on record: {first_exit_year}",
    showarrow=False,
    xanchor="right",
    font=dict(color=COLORS["amber"]),
)
fig.add_hline(y=0, line_color=COLORS["neutral"], line_width=1)
fig.update_layout(
    title="First and last observations per year",
    xaxis_title="Year",
    yaxis_title="Symbols",
    barmode="relative",
    height=420,
)
show_plotly_with_alt(
    fig,
    "Bars above the axis count symbols recording their first observation in each year and "
    "bars below it count those recording their last. The upper bars run through the whole "
    "span, sparse and intermittent in the earliest years and growing steadily after that; "
    "the lower bars are absent entirely until a dashed rule near the right edge, after "
    "which they appear in every remaining year.",
)

# %% [markdown] tags=[]
# ## 4. 退出记录实际显示了什么
#
# 新增记录自 1962 年起持续不断，退出则不然：**面板没有记录到 2014 年之前有任何代码退出。**
#
# 2014 年之前公司显然确实在退出——它们被收购、破产或私有化。安然（Enron）于 2002 年退市。因此，图表所展示的并非股票市场的事实，而是文件本身的事实：**直到大约 2014 年之前，退出信息都没有被采集，大约自那时起才开始被采集。**
#
# 这就是免费、由社区维护的数据所要付出的代价。该面板由项目运行时存在的代码汇编而成，每个代码都回填（backfill）至其自身的 IPO。早已消亡的代码从未被加入，因此它们的消失从未被记录。从 2014 年起面板处于实时运行状态，因此离开面板的代码*确实*会被记录下来。此后，随着贡献者逐渐流失，新增与退出流量都不断衰减，直到 2018 年 3 月数据源停止。
#
# 这对回测意味着什么：
#
# - 2014 年之前，面板中只包含**存活至 2014 年的公司**。在其上运行的 1990 年代回测不会看到哪怕一次公司倒闭，因为根本没有倒闭样本可看。
# - 从 2014 年起，面板确实记录了退出，可以支持考虑幸存者偏差（survivorship bias）的工作。
# - 2014 年之前退出记录的缺失是**证据的缺失**，而非没有公司退出的证据。我们不知道哪些公司退出了，面板无法告诉我们。

# %% tags=[]
exit_summary = (
    lifespans.filter(pl.col("leaves_early"))
    .group_by("exit_year")
    .agg(pl.len().alias("symbols"))
    .sort("exit_year")
    .rename({"exit_year": "year"})
)
exit_summary

# %% tags=[]
n_total = lifespans.height
n_left = lifespans.filter(pl.col("leaves_early")).height
n_still = n_total - n_left
first_year, last_year = lifespans["entry_year"].min(), flows["year"].max()

longest_run = lifespans["days"].max()
display(
    Markdown(
        f"**Coverage summary.** The panel holds **{n_total:,} symbols** over "
        f"**{first_year}-{last_year}**, and its longest single-symbol history runs "
        f"**{longest_run:,} trading days**. **{n_still:,}** ({n_still / n_total:.1%}) are "
        f"still quoted on the final date ({dataset_end}); **{n_left:,}** "
        f"({n_left / n_total:.1%}) leave earlier. Every one of those exits falls in "
        f"**{first_exit_year} or later**, so the panel records no exit across its first "
        f"**{first_exit_year - first_year} years**."
    )
)

# %% [markdown] tags=[]
# ## 5. 数据质量

# %% tags=[]
null_counts = wiki.null_count()
total_nulls = null_counts.sum_horizontal()[0]
print("=== Nulls ===")
print(f"Total null values: {total_nulls:,}")
for col in null_counts.columns:
    val = null_counts[col][0]
    if val > 0:
        print(f"  {col}: {val:,} ({val / len(wiki) * 100:.4f}%)")
print(f"\nNull rate: {total_nulls / (len(wiki) * len(wiki.columns)) * 100:.4f}% of values")

# %% tags=[]
invariants = check_ohlc_invariants(
    wiki,
    open_col="adj_open",
    high_col="adj_high",
    low_col="adj_low",
    close_col="adj_close",
    volume_col="adj_volume",
)

print("OHLC invariants (adjusted prices):")
for row in invariants.iter_rows(named=True):
    status = "[OK]" if row["valid_pct"] >= 99.99 else "[WARN]"
    print(f"  {status} {row['check']}: {row['valid_pct']:.2f}%")

# %% [markdown] tags=[]
# 两项检查均通过，但任何一项都无法发现 §4 中的覆盖缺口。空值（null）与 OHLC 不变性检验是*行内*检查：它们检验每个观测值内部是否一致。而幸存者偏差是**究竟存在哪些行**这一层面的属性，任何行级验证都无法找出从未写入文件的代码。

# %% [markdown] tags=[]
# ## 6. 示例：单个代码

# %% tags=[]
aapl = wiki.filter(pl.col("symbol") == "AAPL").sort("timestamp")

print("=== AAPL ===")
print(f"Trading days: {len(aapl):,}")
print(f"Date range: {aapl['timestamp'].min()} to {aapl['timestamp'].max()}")

# %% [markdown] tags=[]
# AAPL 最近五个交易日的调整后价格。

# %% tags=[]
aapl.select(["timestamp", "adj_open", "adj_high", "adj_low", "adj_close", "adj_volume"]).tail(5)

# %% [markdown] tags=[]
# ## 核心要点
#
# - **在分析行之前，先分析覆盖范围。** 空值与 OHLC 不变性检验关注的是每个观测值内部是否一致。而幸存者偏差是究竟存在哪些行这一层面的属性，任何行内检查都无法发现从未写入文件的代码。
# - **绘制两条流量曲线，而不是总数。** 每年的代码数量与每年的首次及最后一次观测数量回答的是不同的问题，正是后者显示出退出记录在样本中途才开始启用。而总数与两种数据集情形都相符。
# - **数据采集记录中的不连续并非市场事件。** 在这段历史中，公司一直有被收购和倒闭；只是面板在采集上线之前并未记录这些事件。应首先将覆盖范围的中断视为文件本身的事实，并寻找产生它的采集机制。
# - **退出记录的缺失只是证据的缺失。** 对于记录开始之前的年份，该面板无法说明哪些代码退出了，因此也无法说明在它之上运行的回测会错到什么程度。这一陈述比“偏差很小”更强，但比任何具体数字都要弱。
# - **说明每个数字来自哪种价格口径。** 原始价格是交易实际会打印出的价格；调整后列才是计算收益率所应依据的口径。面板同时提供两者，而两者在每一次拆股（split）与分红（dividend）处都不一致。
#
# **已知局限。** 该面板是已停更的 Quandl WIKI 文件，因此数据止于 2018 年，本文中没有任何内容超出该时点。代码以股票代码（ticker）标识，而 ticker 在退市后会被复用，因此同一 ticker 下的长历史并不能证明是同一家连续经营的公司。此外，本笔记对调整列是直接信任采用的：`02_corporate_actions` 在一个实例中检验了它们，而 `15_survivorship_bias_detection` 则找出了该检验失效之处。
#
# **下一步**：`02_corporate_actions` 在一个实例中验证 `adj_*` 列背后的调整因子。`15_survivorship_bias_detection` 基于上述覆盖范围的发现，探讨忽略退出公司的回测会错到什么程度。**本书参考**：§2.2。

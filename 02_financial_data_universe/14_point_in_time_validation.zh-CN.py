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
# > **中文阅读版**：本文件是 `14_point_in_time_validation.ipynb` 的 Markdown 翻译副本。代码、输出、图表和路径保持原样；专有名词和标识符保留英文。
# # Point-in-Time (PIT) 数据验证
#
# **Docker 镜像**：`ml4t`
#
# ## 目的
# 为使回测在真实 ETF 与宏观经济数据上避免前视偏差，演示所需的运行检查。笔记本贯穿三条线索：特征时间与决策时间的对齐、用于捕获明显特征泄漏的基于相关性的启发式方法，以及通过 FRED provider 查看宏观数据的双时态（vintage）视角。
#
# ## 学习目标
# - 区分*事件时间*（某件事实际发生的时间）与*知识时间*（我们获知其发生的时间），以及宏观数据发布所涉及的双时态轴。
# - 说明为什么中心化移动平均会泄漏未来信息，以及为什么水平值与收益率之间的相关性启发式方法无法识别这一点。
# - 构建修正后的尺度不变启发式方法（特征收益率与未来收益率），该方法对 `close.pct_change(-1)` 特征确实能命中。
# - 通过实测确定宏观面板时间戳的含义，以及当这些时间戳是期间戳（period stamps）时，对其进行前向填充的代价。
# - 使用 `vintage_date` 查询 FRED，查看 GDP 初值估计与修订值有何不同。
#
# ## 书中参考
# 第 2 章，§2.3（数据质量框架——Point-in-Time 正确性与双时态数据）。下图是 §2.3 的示意图。
#
# ## 前置条件
# - 已在 `ML4T_DATA_PATH` 下生成的 ETF parquet 文件。
# - 已在 `ML4T_DATA_PATH` 下生成的宏观 parquet（FRED 快照），或可通过 `data.load_macro` 加载。
# - 用于实时 vintage 查询的 `FRED_API_KEY` 环境变量；该查询位于最后一节，因此在此之前的所有内容无需密钥即可运行（免费密钥见 https://fred.stlouisfed.org/docs/api/api_key.html）。

# %%
"""Point-in-Time Data Validation."""

import os
from datetime import datetime

import plotly.graph_objects as go
import polars as pl
from ml4t.data.providers import FREDProvider

from data import load_etfs, load_macro
from utils.style import COLORS, show_plotly_with_alt

# %% [markdown]
# ### 声明的参数
#
# `LEAK_THRESHOLD` 是相关性阈值，高于该阈值时，倒数第二节中的验证器会将某个特征判定为泄漏。它在此处声明，而不是放在类上，这样读者看到的值与检查使用的值就是同一个，并且第 4 节会打印它必须区分的实测相关性。
#
# `MONTHLY_RELEASE_LAG_DAYS` 和 `QUARTERLY_RELEASE_LAG_DAYS` 表示一个期间结束后，其首次估计值发布所需的滞后时长。它们是用作替代真实发布日历的整数：美国非农就业和失业率在参考月份之后的第一个周五发布，CPI 在次月中旬发布，GDP 初值估计在季度结束后约四周发布。生产系统会读取实际日历；这两个参数使修正幅度可见。

# %% tags=["parameters"]
DEMO_SYMBOL = "SPY"
MA_WINDOW = 5  # window for the leakage demonstrations
MA_WINDOW_LONG = 20  # window for the figure
PLOT_TAIL_DAYS = 120
LEAK_THRESHOLD = 0.30  # |corr| above which the validator flags a feature
MAX_GAP_DAYS = 5
EXECUTION_LAG_ROWS = 1  # trading days between a close-of-day signal and its fill

MONTHLY_RELEASE_LAG_DAYS = 7
QUARTERLY_RELEASE_LAG_DAYS = 30
MACRO_DEMO_SERIES = "unrate"

# %% [markdown]
# ## 1. 加载真实市场数据
#
# 一只 ETF 的日线 bar 为下文所有示例提供基准。

# %%
spy = load_etfs().filter(pl.col("symbol") == DEMO_SYMBOL).sort("timestamp")
print(f"{DEMO_SYMBOL}: {len(spy):,} rows; {spy['timestamp'].min()} to {spy['timestamp'].max()}")
spy.head()

# %% [markdown]
# ## 2. 前视偏差：可视化演示
#
# 在时间 $T$ 处、宽度为 $w$ 的滚动移动平均对 $[T - w + 1,\ T]$ 取平均，这是实时系统可以计算的内容。*中心化*移动平均则是将同一窗口向前滑动，使 $T$ 位于其中心附近，从而把部分输入放在 $T$ 之后。
#
# 具体有多少取决于库的中心化约定以及宽度是奇数还是偶数，因此下一个单元格通过实际运行来确认，而不是假设：在斜坡（ramp）上运行中心化平均，会让每个输出暴露产生它的窗口。


# %%
def centered_window_offsets(width: int) -> tuple[int, int]:
    """Return the first and last offsets, relative to T, of a centered window of `width`.

    Averaging a ramp gives back the midpoint of whatever window was used, so one output value
    identifies the window exactly.
    """
    ramp = pl.DataFrame({"x": [float(i) for i in range(4 * width)]}).with_columns(
        pl.col("x").rolling_mean(window_size=width, center=True).alias("centered")
    )
    row = next(i for i, v in enumerate(ramp["centered"]) if v is not None)
    # The mean of a ramp is its window's midpoint, so this recovers the window's first input.
    first_input = ramp["centered"][row] - (width - 1) / 2
    return int(first_input - row), int(first_input + width - 1 - row)


for _w in (MA_WINDOW, MA_WINDOW_LONG):
    _lo, _hi = centered_window_offsets(_w)
    print(
        f"Centered window of width {_w:>2}: [T{_lo:+d}, T{_hi:+d}], "
        f"{_hi} of {_w} inputs are in the future"
    )

# %%
spy_ma = (
    spy.with_columns(
        pl.col("close").rolling_mean(window_size=MA_WINDOW_LONG).alias("ma_trailing"),
        pl.col("close").rolling_mean(window_size=MA_WINDOW_LONG, center=True).alias("ma_centered"),
    )
    .drop_nulls()
    .tail(PLOT_TAIL_DAYS)
)

_tracking = spy_ma.select(
    (pl.col("close") - pl.col("ma_trailing")).abs().mean().alias("trailing"),
    (pl.col("close") - pl.col("ma_centered")).abs().mean().alias("centered"),
)
print(
    f"Mean absolute distance from the close over the plotted window: "
    f"trailing {_tracking['trailing'][0]:.2f}, centered {_tracking['centered'][0]:.2f}"
)

# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=spy_ma["timestamp"].to_list(),
        y=spy_ma["close"].to_list(),
        name="SPY close",
        line=dict(color=COLORS["blue"], width=1),
    )
)
fig.add_trace(
    go.Scatter(
        x=spy_ma["timestamp"].to_list(),
        y=spy_ma["ma_trailing"].to_list(),
        name=f"{MA_WINDOW_LONG}d trailing MA",
        line=dict(color=COLORS["slate"], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        x=spy_ma["timestamp"].to_list(),
        y=spy_ma["ma_centered"].to_list(),
        name=f"{MA_WINDOW_LONG}d centered MA",
        line=dict(color=COLORS["copper"], width=2, dash="dash"),
    )
)
fig.update_layout(
    title=f"{DEMO_SYMBOL} close with trailing and centered moving averages",
    xaxis_title="Date",
    yaxis_title=f"{DEMO_SYMBOL} price",
    height=420,
)
show_plotly_with_alt(
    fig,
    "A price line rising across about six months, with two moving averages drawn over it. "
    "The solid trailing average runs below the price and turns after each move in it. The "
    "dashed centered average runs above the trailing one for the whole window, shifted "
    "left relative to it, and tracks the middle of the price's oscillation rather than "
    "lagging behind it.",
)

# %% [markdown]
# 中心化平均更贴近收盘价，距离为上文打印的实测距离；并且它在价格转向之处转向，而不是在价格转向之后才转向。两者都源于同一件事：其一半输入是尚未出现的价格。没有任何实时系统能生成这条线，因此使用它的回测会报告策略本不可能拥有的技能。
#
# 这两个实测窗口表明，随着窗口变宽，未来信息占比并不会下降：它趋近于一半，并随宽度的奇偶性而波动，而不是递减。泄漏的距离确实会增长，约为宽度的一半。因此，更长的中心化平均并不是更小的违规；它是会向前延伸得更远的违规。
#
# 还有第二个迹象，而且它是实践中最先出现的迹象。中心化平均对最近几行没有值，因为它们仍在等待输入，因此上方的 `drop_nulls` 会悄悄让绘制的序列在数据结束前提前终止。无法为今天计算的特征，是任何实时系统都无法据以交易的特征，而这一缺失的尾部远在任何相关性检验运行之前就已可见。

# %% [markdown]
# ## 3. 为什么朴素相关性启发式方法会失败
#
# 一个自然会想到的泄漏检验，是将特征的*水平值*与下一期的*收益率*做相关。它并不可行，而原因一旦说明并不微妙：价格水平值主要由序列多年来的漂移位置主导，而次日收益率则接近围绕该漂移的均值为零的噪声。这种相关性是慢趋势与快波动之间的相关性，无论特征是否包含明天的价格，结果都接近零。下一个单元格会对三个特征评分，其中之一就是明天的收盘价本身。


# %%
def naive_leakage_corr(df: pl.DataFrame, feature: str, price: str = "close") -> float:
    """Correlation between a level feature and the next-period price return.

    Reproduces the textbook-warning heuristic that *seems* like it should
    catch lookahead but rarely does because it compares incompatible scales.
    """
    enriched = df.with_columns(
        (pl.col(price).shift(-1) / pl.col(price) - 1).alias("next_ret")
    ).drop_nulls([feature, "next_ret"])
    return float(enriched.select(pl.corr(feature, "next_ret")).item())


# %%
naive_features = spy.with_columns(
    pl.col("close").rolling_mean(window_size=MA_WINDOW).alias("ma_trailing"),
    pl.col("close").rolling_mean(window_size=MA_WINDOW, center=True).alias("ma_centered"),
    pl.col("close").shift(-1).alias("tomorrow_close"),
).drop_nulls()

LEAKAGE_FEATURES = ["ma_trailing", "ma_centered", "tomorrow_close"]

naive_results = pl.DataFrame(
    [
        {"feature": f, "naive_corr_with_next_return": naive_leakage_corr(naive_features, f)}
        for f in LEAKAGE_FEATURES
    ]
)
naive_results

# %% [markdown]
# 三项得分都接近零，包括那个*确实*就是明日价格的项。该检验无法把干净特征与泄漏特征区分开，因此一个通过该检验的特征矩阵对自身一无所知。
#
# 检验需要的是两边都是同一类量。把特征转成它自身的环比收益率（period-over-period return）就能做到这一点，这也正是下一节要构建的内容。

# %% [markdown]
# ## 4. 正确的尺度不变泄漏检验
#
# 把任意特征转换为其自身的环比收益率，再将其与下一期的价格收益率求相关。由 $\mathrm{close}_{T+k}$ 构建的特征此时便暴露自己：当 $k \ge 1$ 时，该特征在 $T$ 的收益率*就是*$k$ 期之后的价格收益率，因此相关系数趋近于一。


# %%
def leakage_corr_scale_invariant(df: pl.DataFrame, feature: str, price: str = "close") -> float:
    """Correlation between a feature's own return and the next price return.

    Most useful when `feature` is a price-like (level) series — for return-
    shaped features the pct_change is unstable near zero, so the caller
    should pass them through directly instead.
    """
    enriched = (
        df.with_columns(
            pl.col(feature).pct_change().alias("feat_ret"),
            (pl.col(price).shift(-1) / pl.col(price) - 1).alias("next_ret"),
        )
        .drop_nulls(["feat_ret", "next_ret"])
        .filter(pl.col("feat_ret").is_finite() & pl.col("next_ret").is_finite())
    )
    if enriched.is_empty():
        return float("nan")
    return float(enriched.select(pl.corr("feat_ret", "next_ret")).item())


# %%
fixed_results = pl.DataFrame(
    [
        {
            "feature": f,
            "scale_invariant_corr": leakage_corr_scale_invariant(naive_features, f),
        }
        for f in LEAKAGE_FEATURES
    ]
)
fixed_results

# %% [markdown]
# 同样的三个特征现在可以排序了：滚动平均保持在低位，中心化平均因其窗口有一部分落在未来而上升，而 `tomorrow_close` 因它就是次日价格而饱和于接近 1 的位置。
#
# 把它们区分开的是尺度中部的一道间隙（gap），本 notebook 后面的验证器就把阈值放在那里。正是这道间隙才使阈值成为可能：如果一个检测器的干净样本与泄漏样本彼此靠得很近，那它就得靠选一个能产生已知答案的截断值，这算不上检测器。

# %% [markdown]
# ## 5. 信号到交易的时滞：交易日而非日历日
#
# 由 $T$ 的收盘价计算出的信号，最早只能在 $T+1$ 的开盘时被利用。位移必须按*行*而非按日历日进行，因为周五收盘之后的下一个可交易时点是周一开盘，而再多的日期运算也不知道哪些周一是节假日。按行对时间戳列做位移，等于从数据本身继承了交易日历。


# %%
def validate_signal_trade_lag(signals: pl.DataFrame, execution_lag: int = 1) -> pl.DataFrame:
    """Tag each signal with the earliest tradable date `execution_lag` rows ahead."""
    return signals.sort("timestamp").with_columns(
        pl.col("timestamp").alias("signal_date"),
        pl.col("timestamp").shift(-execution_lag).alias("earliest_execution"),
    )


# %%
spy_with_signal = spy.with_columns(
    (pl.col("close") / pl.col("close").shift(MA_WINDOW) - 1).alias("momentum_signal")
)
_lagged = validate_signal_trade_lag(spy_with_signal, execution_lag=EXECUTION_LAG_ROWS)
_calendar_gap = _lagged.select(
    (pl.col("earliest_execution") - pl.col("signal_date")).dt.total_days().alias("days")
).drop_nulls()
print(
    f"Calendar days between a signal and its earliest execution: "
    f"{_calendar_gap['days'].min()} to {_calendar_gap['days'].max()}, "
    f"for a lag of {EXECUTION_LAG_ROWS} trading day(s)"
)
print(_calendar_gap.group_by("days").len().sort("days"))
_lagged.select(
    ["timestamp", "close", "momentum_signal", "signal_date", "earliest_execution"]
).drop_nulls().head(8)

# %% [markdown]
# ## 6. 宏观面板的时间戳意味着什么
#
# 宏观序列以不同的频率到达，而面板把它们并排存放在同一个日频网格上，因此某一列在其自身两次发布之间必须被向前结转。通常的建议是前向填充（forward-fill）而绝不后向填充，这个建议正确但并不充分：只有当时间戳是该数字*发布*的日期时它才安全。如果时间戳是该数字所*描述*的时期，那么从它开始前向填充，就等于在统计机构之外的任何人拿到该数字之前数周，就把这个数字交给了回测。
#
# 这个面板采用哪种约定是关乎该文件的问题，所以接下来的单元格就来问它。

# %%
macro = load_macro()
macro = macro.rename({col: col.lower() for col in macro.columns})

date_col = "timestamp" if "timestamp" in macro.columns else "date"
_series_cols = [c for c in macro.columns if c != date_col]

freshness = (
    pl.DataFrame(
        {
            "series": _series_cols,
            "nulls": [macro[c].null_count() for c in _series_cols],
            "value_changes": [
                macro.select((pl.col(c) != pl.col(c).shift(1)).sum()).item() for c in _series_cols
            ],
        }
    )
    .with_columns(
        (pl.col("value_changes") / (macro.height / 365.25)).round(1).alias("changes_per_year")
    )
    .sort("changes_per_year")
)
print(f"Macro panel: {macro.height:,} rows, {macro[date_col].min()} to {macro[date_col].max()}")
print(f"Distinct dates: {macro[date_col].n_unique():,} (a row per calendar day, weekends included)")
freshness

# %% [markdown]
# 已经能看到两件事。每一列都是完整的：没有空值需要前向填充，因为面板到手时就已经填好了。而变动次数无需任何人声明就把各列分成了不同频率，从一年几次一直到每个工作日一次。
#
# 约定问题由变动*发生的时间*来回答。

# %%
_change_day = (
    pl.concat(
        [
            macro.select(
                pl.lit(c).alias("series"),
                pl.col(date_col).dt.day().alias("day_of_month"),
            ).filter(
                macro.select((pl.col(c) != pl.col(c).shift(1)).alias("x"))["x"]
                & macro.select(pl.col(c).shift(1).is_not_null().alias("y"))["y"]
            )
            for c in _series_cols
        ]
    )
    .group_by("series", "day_of_month")
    .len()
)
_first_of_month = (
    _change_day.group_by("series")
    .agg(
        pl.col("len").sum().alias("changes"),
        pl.col("len").filter(pl.col("day_of_month") == 1).sum().alias("on_the_first"),
    )
    .with_columns((pl.col("on_the_first") / pl.col("changes")).alias("share_on_the_first"))
    .sort("share_on_the_first", descending=True)
)
print("Share of each series' value changes that land on the first of a month:")
_first_of_month

# %% [markdown]
# 低频序列每次都在每月 1 号改变其数值。这不是发布日历：没有哪个统计机构在每个月的 1 号发布数据，也没有哪个机构在某季度的第一天发布该季度的产出。这是时期戳记。FRED 用月度观测所描述月份的第一天来标注该观测，季度观测则用该季度的第一天，而面板把每个数值从那时起向前结转。
#
# 因此，某个月的失业率在这个面板中从该月第一天起就可读，甚至在该月尚未结束、更谈不上被调查和发布之前。这个面板中的前向填充不是 PIT 安全的，而再自己加一次前向填充也无济于事，因为已没有东西可填。

# %%
_period_days = {"monthly": 31, "quarterly": 92}


def stamp_to_availability(frame: pl.DataFrame, column: str, cadence: str) -> pl.DataFrame:
    """Move a period-stamped series to the date its first estimate could have been read.

    The stamp is the first day of the period, so the period ends roughly a period length later
    and the first estimate follows the declared release lag after that.
    """
    lag_days = _period_days[cadence] + (
        MONTHLY_RELEASE_LAG_DAYS if cadence == "monthly" else QUARTERLY_RELEASE_LAG_DAYS
    )
    return frame.select(
        (pl.col(date_col) + pl.duration(days=lag_days)).alias("available_from"),
        pl.col(column).alias(f"{column}_pit"),
    )


_demo = macro.select(date_col, MACRO_DEMO_SERIES)
_pit = stamp_to_availability(_demo, MACRO_DEMO_SERIES, "monthly")
_joined = (
    _demo.join(_pit, left_on=date_col, right_on="available_from", how="left")
    .with_columns(pl.col(f"{MACRO_DEMO_SERIES}_pit").forward_fill())
    .drop_nulls()
)
_differs = _joined.filter(pl.col(MACRO_DEMO_SERIES) != pl.col(f"{MACRO_DEMO_SERIES}_pit"))

print(
    f"Rows where the panel's {MACRO_DEMO_SERIES} and the release-lagged version disagree: "
    f"{_differs.height:,} of {_joined.height:,} "
    f"({100 * _differs.height / _joined.height:.0f}%)"
)
print(
    "Largest disagreement: "
    f"{(_differs[MACRO_DEMO_SERIES] - _differs[f'{MACRO_DEMO_SERIES}_pit']).abs().max():.1f} "
    "percentage points"
)
_joined.filter(pl.col(date_col).dt.year() == 2020).head(12)

# %% [markdown]
# 这两列在四天中有三天不一致，而最大分歧大于该序列在寻常十年中所占据的整个区间：2020 年失业率在两个月内变动超过十个点，而面板的这一列在该变动发布之前数周就已将其反映出来。
#
# 这里施加的时滞只是一个代表发布日历的整数，所以修正后的列本身并非生产级。它确立的是方向与量级：未修正的列在大多数日子都偏早，而偏早的幅度恰恰在数据有意思时最大。直接基于这个面板构建的宏观特征，是一个在衰退被宣布之前就知道衰退的特征。
#
# 一般规则，也是本 notebook 存在的原因：**时间戳是关于某事物何时可知的一种主张，而文件很少说明它主张的是哪一种。** 用测量一次性确定它，并把答案记录在加载器所在之处。
#
# ## 7. PIT 验证器演示
#
# 把尺度不变泄漏检验、日期单调性检查和间隙审计包装起来，一次调用即可把整个特征矩阵跑一遍。泄漏阈值就是已声明的 `LEAK_THRESHOLD`，而第 4 节的表格正是把它放在该位置的理由：干净特征与泄漏特征被大部分尺度隔开，因此截断值落在空白处，而不是落在两个相邻的测量值之间。


# %%
class PITValidator:
    """Point-in-time validation for daily price-and-feature panels."""

    def __init__(self, df: pl.DataFrame, date_col: str = "timestamp"):
        self.df = df
        self.date_col = date_col
        self.violations: list[dict] = []

    def check_future_leakage(self, feature_col: str, price_col: str = "close") -> dict:
        corr = leakage_corr_scale_invariant(self.df, feature_col, price_col)
        severity = "HIGH" if abs(corr) > LEAK_THRESHOLD else "LOW"
        result = {
            "feature": feature_col,
            "scale_invariant_corr": round(corr, 4),
            "severity": severity,
            "violation": severity == "HIGH",
        }
        if result["violation"]:
            self.violations.append(result)
        return result

    def check_date_gaps(self, max_gap_days: int = MAX_GAP_DAYS) -> dict:
        gaps = (
            self.df.sort(self.date_col)
            .with_columns(pl.col(self.date_col).diff().dt.total_days().alias("gap_days"))
            .filter(pl.col("gap_days") > max_gap_days)
        )
        return {
            "rows": len(self.df),
            "gaps_above_threshold": len(gaps),
            "max_gap_days": int(gaps["gap_days"].max()) if len(gaps) > 0 else 0,
        }

    def check_monotonic_dates(self) -> dict:
        diffs = self.df[self.date_col].diff().drop_nulls().dt.total_days()
        is_sorted = bool((diffs >= 0).all())
        return {"is_monotonic": is_sorted, "violation": not is_sorted}


# %%
spy_features = spy.with_columns(
    pl.col("close").rolling_mean(window_size=MA_WINDOW).alias("ma_short_trailing"),
    pl.col("close").rolling_mean(window_size=MA_WINDOW_LONG).alias("ma_long_trailing"),
    pl.col("close").rolling_mean(window_size=MA_WINDOW, center=True).alias("ma_short_centered"),
    pl.col("close").shift(-1).alias("tomorrow_close"),
).drop_nulls()

validator = PITValidator(spy_features)
validation_table = pl.DataFrame(
    [
        validator.check_future_leakage(f)
        for f in [
            "ma_short_trailing",
            "ma_long_trailing",
            "ma_short_centered",
            "tomorrow_close",
        ]
    ]
)
validation_table

# %%
gap_check = validator.check_date_gaps()
mono_check = validator.check_monotonic_dates()
print(
    f"Date gaps over {MAX_GAP_DAYS} calendar days: "
    f"{gap_check['gaps_above_threshold']} (max {gap_check['max_gap_days']} days); "
    f"monotonic={mono_check['is_monotonic']}"
)
print(f"Features flagged as leaking: {len(validator.violations)} of {validation_table.height}")

# %% [markdown]
# 两个由未来数据构造的特征被标记出来，而两个滚动平均未被标记，这正是本节想要得到的排序。值得明确说明这能证明什么、不能证明什么。验证器是在状态已知的特征上运行的，因此这是对验证器的测试，而不是对特征的测试。若在无人审计过的特征矩阵上运行，它会捕捉到表现为与下一期收益相关的泄漏，却捕捉不到不会如此表现的泄漏：一个特征如果使用的是某个*其他*变量的未来值，而该变量并非其评分所对照的价格，就会原封不动地通过这项检查。
#
# ## 8. 通过 FRED `vintage_date` 获取双时态 GDP
#
# 宏观数据会被修订。FRED API 的 `realtime_start` / `realtime_end` 参数会返回**在所选历史日期已知的**数值。`FREDProvider.fetch_ohlcv` 将其暴露为 `vintage_date`。
#
# 下面的单元格需要 `FRED_API_KEY`（可免费注册）；如果缺少该密钥，获取会明确报错失败，而不是改用合成数据示例替代。

# %%
FRED_API_KEY = os.getenv("FRED_API_KEY")
if not FRED_API_KEY:
    raise RuntimeError(
        "FRED_API_KEY not set. Get a free key at "
        "https://fred.stlouisfed.org/docs/api/api_key.html and export it."
    )

provider = FREDProvider()

gdp_early = provider.fetch_ohlcv(
    "GDP",
    "2023-01-01",
    "2023-09-30",
    frequency="quarterly",
    vintage_date="2023-11-01",
)
gdp_late = provider.fetch_ohlcv(
    "GDP",
    "2023-01-01",
    "2023-09-30",
    frequency="quarterly",
    vintage_date="2024-06-01",
)
provider.close()

revisions = (
    gdp_early.select(["timestamp", pl.col("close").alias("vintage_2023_11_01")])
    .join(
        gdp_late.select(["timestamp", pl.col("close").alias("vintage_2024_06_01")]),
        on="timestamp",
    )
    .with_columns(
        (
            (pl.col("vintage_2024_06_01") - pl.col("vintage_2023_11_01"))
            / pl.col("vintage_2023_11_01")
            * 100
        )
        .round(3)
        .alias("revision_pct")
    )
)
revisions

# %% [markdown]
# 较早的季度在两个数据版本（vintage）之间一致，因为在第一个数据版本日期时，它们已经被修订为当前值。最近一个季度则不然：2023 年末对它的查询返回的是初步估计值（advance estimate），而到 2024 年中，该数值已经发生变化。
#
# 按百分比衡量，修订幅度很小，这是通常情况，也是这件事容易被忽略的原因。问题不在于单次修订的幅度，而在于：回测读取当前值时，对于它涉及的每一个被修订序列，读到的是一个在决策日期并不存在的数值；而且修订方向并非噪声：估计值会被修订得趋向实际发生的情况。

# %% [markdown]
#
# %% [markdown]
# ## 关键要点
#
# 1. **居中窗口有接近一半落在未来，而且加宽窗口也无济于事。**
#    偏移量是在上文实际测量得到的，而不是假设的，因为这一约定因库以及窗口宽度的奇偶性而异。随着窗口增大，未来占比趋近于一半，而泄漏的距离也随之增加，约为宽度的一半；因此更长的居中平均会向前伸得更远，而不是泄漏得更少。图展示了后果，打印出的距离对其进行了度量。
#
# 2. **将水平值与收益做相关并不能检测泄漏。** 明日收盘价若直接作为特征，在该测试中得分接近零，与干净的滚动平均并列。一个通过该测试的特征矩阵，并没有因此获得关于自身的任何信息。
#
# 3. **把两边都放入收益空间后，同一测试就能奏效**，而阈值之所以可设定，是因为干净情形与泄漏情形最终在大部分数值尺度上彼此分开。若在相邻的两个测量值之间取截断点，那就成了为了得到已知答案而选择的截断点。
#
# 4. **交易日滞后必须按行应用，而不是按日期应用。** 一个交易日是一到五个日历日，具体取决于它落在星期中的哪一天以及节假日日历，相关计数已在上文打印。按行平移时间戳列会从数据中继承日历。
#
# 5. **宏观面板的时间戳是时期戳，而不是发布日期，而且这是可以测量的。** 每个低频序列都在每月第一天改变数值，没有任何发布日历会这样。该面板到达时已经基于这些时期戳进行了前向填充，因此它是完整的，再做一次前向填充也是空操作，而读取某一列会在数据发布前数周就给出数值。与按发布滞后处理的版本相比，面板自带的列在四天中有三天不一致，最大差距超过十个失业率百分点——2020 年春季，知道与不知道之间的差别就是整笔交易的关键。
#
# 6. **宏观数值会被修订，因此当前值并不是当时可用的值。** 数据版本（vintage）查询返回某一日期当时可知的值。修订会使估计值趋向实际发生的情况，而这恰恰是会让回测显得更好的方向。
#
# 7. **检测是兜底手段，不能替代构造。** 这里的每一项检查都是在状态已知的特征上运行的，这测试的是检查本身。在未经审计的矩阵上，这些检查能捕捉与评分收益相关的泄漏，却会漏掉不相关的泄漏。
#
# **下一步**：`15_survivorship_bias_detection` 在本文展示的时间正确性基础上，加入投资范围成员资格这一维度。

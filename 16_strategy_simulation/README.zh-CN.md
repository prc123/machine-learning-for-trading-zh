# 第 16 章：策略模拟

回测不是用来寻找最好数字的搜索引擎，而是对交易协议的证伪工具。本章要求先显式定义信号时间、执行、成本、组合与风险规则，再比较向量化引擎、事件驱动引擎和非 ML 基线，最后解释绩效指标、经济价值和统计不确定性。

## 学习目标

- 把回测形式化为显式交易协议，覆盖信号时间、执行、成本、组合和风险处理。
- 从协议语义、状态、时序和假设差异区分向量化与事件驱动回测。
- 构建并解释一个透明、可审计的非 ML 基线策略。
- 用包含毛/净表现、风险、交易和实现细节的核心报告评估策略。
- 区分固定策略的估计误差与多次选择导致的回测过拟合，判断 Sharpe ratio 是否可信。
- 解释预测质量与交易质量为何会分离，以及信息如何在不同阶段被放大或消耗。

## 章节脉络

### 16.1 回测即证伪

回测的价值不是“证明赚钱”，而是尽可能暴露协议错误、过拟合、成本假设脆弱和不稳健的依赖。

### 16.2 明确回测协议

先写清楚投资范围、信号可用时间、成交时间、价格、成本、仓位、再平衡和风险规则。

- [`01_backtest_first_principles`](01_backtest_first_principles.ipynb)：构建一个从协议出发的组合回测。
- [`08_signal_method_comparison`](08_signal_method_comparison.ipynb)：把注册模型预测转换为可比较策略结果。
- [`02_futures_backtesting`](02_futures_backtesting.ipynb)：引入合约乘数、保证金和期货专用协议问题。

### 16.3 向量化与事件驱动回测

向量化方法适合快速研究，事件驱动方法更适合表达路径依赖、订单簿和执行逻辑；两者必须共享协议才能比较。

- [`03_single_asset_vectorbt`](03_single_asset_vectorbt.ipynb)：用 vectorbt 实现单资产 RSI 均值回归。
- [`04_single_asset_ml4t_backtest`](04_single_asset_ml4t_backtest.ipynb)：在统一协议下运行同一规则。
- [`05_stateful_strategies`](05_stateful_strategies.ipynb)：实现无法纯向量化表达的有状态策略。
- [`06_framework_parity`](06_framework_parity.ipynb)：比较数组运算与事件驱动引擎。
- [`07_engine_divergence_anatomy`](07_engine_divergence_anatomy.ipynb)：逐项拆解引擎结果差异。
- [`15_lean_engine_parity`](15_lean_engine_parity.ipynb)、[`16_case_study_lean_parity`](16_case_study_lean_parity.ipynb)：检查与 LEAN 引擎的协议一致性。

### 16.4 可审计的非 ML 基线

没有非 ML 基线，就无法判断模型复杂度是否真的增加了经济价值。

### 16.5 理解绩效指标

同时报告收益、风险、回撤、换手、交易次数、成本和覆盖率，而不是只报告最终净值或 Sharpe。

- [`09_performance_reporting`](09_performance_reporting.ipynb)：构建标准绩效报告。

### 16.6 诊断经济价值

把结果按市场状态、成本、频率和信号强度切片，识别利润来源与脆弱条件。

- [`10_regime_backtest_analysis`](10_regime_backtest_analysis.ipynb)：按 regime 检查回测表现。
- [`14_cost_sensitivity`](14_cost_sensitivity.ipynb)：在成本网格上重跑策略。

### 16.7 统计推断与回测过拟合

固定策略有抽样误差；搜索和选择又会进一步抬高最优结果。

- [`11_sharpe_ratio_inference`](11_sharpe_ratio_inference.ipynb)：研究 Sharpe ratio 的抽样分布。
- [`12_dsr_validation`](12_dsr_validation.ipynb)：使用 Deflated Sharpe Ratio 和 backtest overfitting probability。
- [`13_ras_protocol`](13_ras_protocol.ipynb)：使用 Rademacher Anti-Serium 界为多次尝试收取惩罚。

### 16.8 小结

可信回测的关键不是引擎品牌，而是协议显式、状态正确、成本现实、指标完整、证据冻结。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 16_strategy_simulation/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "16_strategy_simulation"
```

### 无显示环境

可在 headless 模式下运行图形相关示例；详见英文 [`README.md`](README.md)。

### 依赖

部分引擎或图形依赖可能需要额外安装，请以英文 [`README.md`](README.md) 的 `Dependencies` 为准。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

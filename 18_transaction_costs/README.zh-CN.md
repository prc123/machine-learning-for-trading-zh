# 第 18 章：交易成本

交易成本会贯穿因子评估、回测、组合构建、风险管理和实盘监控。本章把成本拆成显性、隐性和容量相关部分，并把它们连接到价差、冲击、市场状态、执行算法、TCA 和净收益护栏。

## 学习目标

- 识别交易成本在 ML4T 工作流中的位置，从因子评估和回测到组合构建、风险管理和生产监控。
- 区分显性、隐性和容量相关交易成本，并把每个组件映射到相应建模选择。
- 解释执行成本为何随市场状态、日内流动性、波动率和执行紧急程度变化。
- 在缺乏直接执行数据时，选择并校准保守的研究默认成本模型，如基于价差、线性冲击或 square-root impact 的模型。
- 比较 TWAP、VWAP、自适应参与率和 Almgren-Chriss 式最优执行对冲击、时序风险和信号衰减的影响。
- 用 transaction cost analysis 分解已实现成本、诊断模型误设并重新校准事前假设。
- 用盈亏平衡换手率、最低必要优势、alpha-to-go、容量分析和预承诺停止标准判断成本后策略是否仍然可行。

## 章节脉络

### 18.1 成本进入 ML4T 工作流的位置

成本不只是回测扣减项，它会改变最优频率、信号强度、组合集中度和容量。

- [`01_cost_taxonomy`](01_cost_taxonomy.ipynb)：比较七个资产类别的费用结构、价差状态和盈亏平衡 alpha。
- [`03_market_impact_calibration`](03_market_impact_calibration.ipynb)：校准冲击模型并估计容量上限。

### 18.2 面向从业者的成本分类

把佣金、费用、价差、滑点、冲击、延迟和融资成本放进统一账本。

- [`02_spread_estimation`](02_spread_estimation.ipynb)：用经典估计量从 OHLCV 估计买卖价差，并用微观结构数据验证。
- [`12_commission_slippage_comparison`](12_commission_slippage_comparison.ipynb)：比较 6 种佣金模型和 5 种滑点模型。

### 18.3 微结构与市场状态的联系

成本不是常数；价差、深度、波动率和日内成交量形状共同决定执行成本。

### 18.4 回测基线成本模型

研究阶段应使用保守默认值，并区分每笔成本、每单位名义额、每单位成交量和冲击函数。

- [`06_ml4t_execution_demo`](06_ml4t_execution_demo.ipynb)：演示 `ml4t.backtest.execution` 中的现实执行成本模型。

### 18.5 执行算法是控制手段，不是魔法

TWAP、VWAP、参与率限制和动态执行会交换冲击与时序风险，但不会消除成本。

- [`04_vwap_twap_execution`](04_vwap_twap_execution.ipynb)：实现 VWAP 和 TWAP 执行基准。
- [`07_ml4t_volume_participation`](07_ml4t_volume_participation.ipynb)：演示机构订单的成交量参与限制。
- [`08_ml_dynamic_execution`](08_ml_dynamic_execution.ipynb)：根据实时市场条件自适应选择执行参数。

### 18.6 以 Almgren-Chriss 统一执行优化

把冲击成本与时序风险放入统一目标，推导最优执行轨迹和执行前沿。

- [`05_almgren_chriss_optimal_execution`](05_almgren_chriss_optimal_execution.ipynb)：实现 Almgren-Chriss 框架和 TCA 方法。

### 18.7 交易成本分析与模型验证

用已实现成交分解成本，检查理论毛收益与净收益之间的缺口来自哪里。

- [`10_gross_vs_net_performance`](10_gross_vs_net_performance.ipynb)：系统分析理论绩效与实际绩效的差异。

### 18.8 设计实用成本护栏

用盈亏平衡点、最低信号优势、容量、频率上限和预承诺停止规则保护净收益。

- [`09_frequency_tradeoff`](09_frequency_tradeoff.ipynb)：研究信号质量与再平衡频率的成本权衡。
- [`11_cost_cliff`](11_cost_cliff.ipynb)：展示日内策略在现实成本下可能从优秀变为不可行。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 18_transaction_costs/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "18_transaction_costs"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

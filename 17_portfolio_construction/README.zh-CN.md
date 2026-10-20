# 第 17 章：组合构建

信号只是组合的一部分。本章把预期收益、协方差、约束、杠杆和再平衡规则形式化，比较等权、逆波动率、均值方差、Kelly、HRP 和深度学习分配器，并强调 allocator 选择本身也会过拟合。

## 学习目标

- 用预期收益、协方差、约束、杠杆和再平衡选择形式化组合构建问题。
- 识别补充第 16 章回测报告的 allocator 专用指标，尤其是相对基准表现、集中度、分散化和实现稳定性。
- 解释等权、逆波动率和相关启发式分配器为什么仍是难以击败的基线。
- 结合 shrinkage、现实约束和换手感知正则化使用均值方差优化。
- 把 Kelly 定价、尤其是 fractional Kelly，理解为把信号强度转换到头寸规模的对数增长原则。
- 构建优先追求分散化稳定性的层次化风险平价组合。
- 在共同研究协议下比较 allocator，限制 allocator-selection bias 和其他过拟合。

## 章节脉络

### 17.1 定义分配问题

明确目标函数、时间尺度、可交易资产、约束、交易成本和风险容忍。

### 17.2 组合构建工作流

把信号、预测不确定性、组合权重、执行和风险控制串成可重复流程。

### 17.3 组合评估指标

用绝对收益、风险调整收益、回撤、集中度、换手和基准相对表现共同评估。

- [`01_portfolio_metrics`](01_portfolio_metrics.ipynb)：用 `ml4t-diagnostic` 计算注册 ETF 分配回测的风险收益、回撤和基准相对指标。

### 17.4 定义基线 allocator

先建立等权、逆波动率、Kelly 证据和不确定性驱动头寸规则等基线。

- [`04_kelly_criterion`](04_kelly_criterion.ipynb)：从二元赌注推导 Kelly，并扩展到连续收益和多资产组合。
- [`05_factor_allocation_evidence`](05_factor_allocation_evidence.ipynb)：检查哪些收益来源彼此分散，并注意文献级多重检验。
- [`07_conformal_position_sizing`](07_conformal_position_sizing.ipynb)：用每个实体的 conformal prediction interval 决定头寸规模。

### 17.5 均值方差优化与 Markowitz 诅咒

预期收益和协方差的估计误差会被优化器放大，必须用 shrinkage、约束和稳健目标控制。

- [`02_mean_variance_optimization`](02_mean_variance_optimization.ipynb)：从零构建有效前沿、最大 Sharpe 和最小方差组合。
- [`03_robust_optimization`](03_robust_optimization.ipynb)：比较 Ledoit-Wolf shrinkage、risk parity、minimum variance 和 minimum conditional drawdown。

### 17.6 用层次化风险平价优化稳定性

HRP 通过聚类、quasi-diagonalization 和递归二分降低直接矩阵求逆的敏感性。

- [`06_hierarchical_risk_parity`](06_hierarchical_risk_parity.ipynb)：实现 HRP 并与 shrinkage MVO 和启发式方法做 walk-forward 比较。

### 17.7 比较 allocator 表现

 allocator 选择必须在 holdout 打开前冻结，之后只用 holdout 描述结果。

- [`08_library_comparison`](08_library_comparison.ipynb)：用 PyPortfolioOpt、Riskfolio-Lib 和 skfolio 从相同矩估计拟合可比组合。
- [`09_allocator_comparison`](09_allocator_comparison.ipynb)：在共享信号上比较等权、逆波动率、shrinkage MVO 和 HRP。

### 17.8 深度学习组合构建

深度模型可以直接输出权重、变量选择信号或 regime 稳健目标，但要与简单 allocator 保持同协议比较。

- [`11_dl_portfolio_allocation`](11_dl_portfolio_allocation.ipynb)：训练 softmax 输出 long-only 权重并优化可微 Sharpe loss。
- [`12_vlstm_portfolio`](12_vlstm_portfolio.ipynb)：加入变量选择网络和波动率目标层，并在训练 loss 中计入换手。
- [`13_deepm_regime_robust`](13_deepm_regime_robust.ipynb)：实现 DeePM 的 SoftMin 最差滚动窗口目标并做消融。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 17_portfolio_construction/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "17_portfolio_construction"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

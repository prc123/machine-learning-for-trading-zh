# 第 19 章：风险管理

一个回测赢家只有在经过尾部风险、路径风险、暴露分解、压力测试、自适应控制、kill switch 和治理约束后，才可能成为可交易系统。本章把这些内容放进统一的 ML4T 工作流。

## 学习目标

- 用 VaR 和 CVaR 度量尾部风险，包括 regime 条件估计和流动性感知解释。
- 用回撤深度、回撤持续时间、恢复时间和路径依赖指标评估路径风险。
- 把组合风险分解为市场、因子、行业、地理和宏观暴露，区分有意下注与无意暴露。
- 设计并解释历史、假设和反向压力测试，同时挑战收益、成本、波动率和相关性假设。
- 只使用决策时点可得信息构建波动率目标、暴露上限和头寸级退出等自适应风险控制。
- 定义 kill switch、漂移监控和治理产物，把回测策略变成可部署交易系统。

## 章节脉络

### 19.1 把回测赢家变成可交易系统

绩效只是起点；还要检查风险预算、执行约束、容量、监控和人工/自动干预边界。

- [`01_var_cvar`](01_var_cvar.ipynb)：计算历史、参数和 Cornish-Fisher VaR/CVaR，并做回测验证。
- [`06_stress_testing`](06_stress_testing.ipynb)：比较历史危机重放、假设场景和 Monte Carlo。

### 19.2 量化策略的实用风险分类

区分市场风险、模型风险、流动性风险、集中度风险、执行风险、对手方风险和运营风险。

- [`04_factor_exposure`](04_factor_exposure.ipynb)：用回归分解市场、规模、价值、盈利和投资因子暴露。

### 19.3 度量尾部：VaR 与 CVaR

VaR 回答给定置信水平下的损失阈值；CVaR 进一步回答超过阈值时的平均损失。

### 19.4 回撤、路径风险与恢复时间

最终收益相同，路径不同，投资者行为和强制平仓风险也可能完全不同。

- [`02_exit_strategies`](02_exit_strategies.ipynb)：比较固定止损、移动止损、波动率调整退出和混合方案。
- [`03_position_sizing_mae_mfe`](03_position_sizing_mae_mfe.ipynb)：用 MAE/MFE excursion 分析校准止损和头寸规模。
- [`10_ml4t_backtest_risk_demo`](10_ml4t_backtest_risk_demo.ipynb)：演示组合级止损规则、规则组合和 kill switch。

### 19.5 分解因子、行业与宏观暴露

把策略收益归因到有意因子和被动暴露，识别名义上分散但实际重复下注的组合。

- [`05_trade_shap_diagnostics`](05_trade_shap_diagnostics.ipynb)：把 SHAP 解释连接到交易结果，回答“这笔交易为什么失败”。

### 19.6 压力测试与场景分析

同时压低收益、放大成本、提高波动率并改变相关性，观察风险模型和控制是否同时失效。

### 19.7 不泄漏的自适应风险控制

波动率目标、exposure cap、退出信号和 deep hedging 都必须只使用决策时可得数据。

- [`07_drift_detection`](07_drift_detection.ipynb)：检测实盘数据分布相对训练数据的漂移。
- [`08_ml_exit_signals`](08_ml_exit_signals.ipynb)：用入口模型和退出模型分别预测机会与不利变动。
- [`09_deep_hedging`](09_deep_hedging.ipynb)：在交易成本下训练神经网络，最小化终端 P&L 的 CVaR。
- [`11_systematic_risk_sweep`](11_systematic_risk_sweep.ipynb)：系统扫描止损、止盈和移动止损参数。

### 19.8 应用 kill switch 与风险治理

把触发条件、授权边界、降杠杆规则、停止交易流程和复盘记录写进治理文档。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 19_risk_management/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "19_risk_management"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

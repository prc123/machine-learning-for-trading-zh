# 第 15 章：因果机器学习

相关性强不等于交易理由成立。本章从因果问题定义、DAG、识别假设、验证和证伪开始，进入 Double Machine Learning、Bayesian Structural Time-Series、因果发现和跨案例因果证据。

## 学习目标

- 用处理、结果、estimand 和反事实定义因果研究问题，并用 DAG 论证可容许调整集合。
- 用 placebo 检验、敏感性分析和子集稳定性检查评估因果结论是否足够稳健。
- 在高维混淆变量下用 Double Machine Learning 估计连续处理的因果效应，并遵守时间交叉拟合和处理前时序纪律。
- 用 Bayesian Structural Time-Series 为离散事件构造数据驱动反事实，并评估控制序列的溢出风险。
- 用 PCMCI、NOTEARS、VAR-LiNGAM 等因果发现方法生成候选结构，并把结果作为待验证假设而非最终事实。
- 区分预测信号与因果效应，注意混淆偏差、多重检验以及统计显著与通过证伪之间的差距。

## 章节脉络

### 15.1 从理论到估计

把因果问题的概念要素映射到库 API 和可估计对象。

- [`01_library_overview`](01_library_overview.ipynb)：按问题类型、处理类型和数据结构选择 EconML、DoWhy、CausalML、Tigramite 或 causal-learn。

### 15.2 识别与验证

检查处理定义、混杂路径、时间顺序、调整集合和可交换性假设。

### 15.3 验证与证伪

用反事实稳定性、placebo、敏感性和替代结果判断结论是否只是模型伪影。

- [`02_dowhy_causal_graph`](02_dowhy_causal_graph.ipynb)：在加密货币资金费率场景中完整走 DoWhy 验证流程。

### 15.4 用 DML 隔离因子效应

先预测处理和结果中的可预测部分，再对残差化关系估计因果效应。

- [`03_econml_dml`](03_econml_dml.ipynb)：估计动量因子对远期收益的因果效应，比较 naive OLS 与 LinearDML。
- [`04_dml_crypto_regime`](04_dml_crypto_regime.ipynb)：估计永续合约资金费率 z-score 对 8 小时收益的效应，并检查 regime 交互。
- [`05_momentum_causal_trading`](05_momentum_causal_trading.ipynb)：用 CausalForestDML 估计 CATE，并测试因果头寸缩放的样本外效果。
- [`11_factor_zoo_validation`](11_factor_zoo_validation.ipynb)：用 post-double-selection LASSO 检验因子在保留结果上的边际定价能力。

### 15.5 用 Bayesian Structural Time-Series 度量事件影响

为事件前后关系构造反事实，并用控制序列和 placebo 检查脆弱性。

- [`06_fed_announcement_bsts`](06_fed_announcement_bsts.ipynb)：研究 FOMC 公告对国债 ETF 的累计影响。

### 15.6 从观测数据做因果发现

把发现算法输出当作候选 DAG 或时序图，必须再用稳定性和机制检查过滤。

- [`07_tigramite_time_series`](07_tigramite_time_series.ipynb)：在宏观面板上运行 PCMCI，并用 block bootstrap 检验稳定性。
- [`08_neural_causal_discovery`](08_neural_causal_discovery.ipynb)：比较 NOTEARS、VAR-LiNGAM、PCMCI 和 Granger causality。
- [`09_adia_causal_benchmark`](09_adia_causal_benchmark.ipynb)：复现简化版 ADIA 因果发现基准。

### 15.7 案例研究的因果证据

- [`10_case_study_insights`](10_case_study_insights.ipynb)：汇总各案例的 DML 效应、HAC 置信区间、混淆偏差比较和 refutation 结果。

### 15.8 小结

因果方法不能自动救活坏信号；它们的价值在于更清楚地暴露假设、机制和不可证伪的结论。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 15_causal_estimation/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "15_causal_estimation"
```

### 无显示环境

涉及图形输出的 notebook 可使用 headless 方式运行；详见英文 [`README.md`](README.md)。

### 依赖

除主环境依赖外，本章 BSTS 与因果图相关示例可能需要额外系统库或 Graphviz。请以英文 [`README.md`](README.md) 的 `Dependencies` 为准。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

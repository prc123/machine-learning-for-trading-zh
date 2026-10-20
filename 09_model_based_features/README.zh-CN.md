# 第 9 章：基于模型的特征提取

直接特征通常由规则公式定义；模型化特征则由拟合过程产生。本章讨论何时值得引入这种额外复杂度，以及如何在训练窗口内正确拟合、选择和转换模型输出，从而获得诊断、状态、波动率、不确定性和 regime 特征。

## 学习目标

- 区分直接特征与模型化特征，判断拟合过程是否提供额外有用信息。
- 用拟合程序提取预测、过滤状态、残差、条件波动率、regime 概率和不确定性。
- 从诊断、信号变换、波动率模型和横截面方法中设计紧凑且可解释的模型化特征。
- 只在训练窗口内拟合和选择模型，使用过滤后的输出，保证 Point-in-Time 正确性。
- 把资产级时间序列输出转换为横截面、基准调整、成对和 universe 级特征。
- 区分有研究诊断价值的探索性时间序列方法与可部署特征方法。
- 把不确定性和 regime 输出主要作为条件特征，避免把无法支持精确预测的东西当作独立 alpha。

## 章节脉络

### 9.1 诊断与平稳性特征

从可视化、自相关、结构性断点、变点搜索和分数差分中构造诊断列。

- [`01_visual_diagnostics`](01_visual_diagnostics.ipynb)：金融时间序列诊断流程，并把滚动统计转为特征。
- [`02_structural_breaks`](02_structural_breaks.ipynb)：用经典检验和变点搜索发现 regime 变化日期。
- [`03_fractional_differencing`](03_fractional_differencing.ipynb)：在追求平稳性的同时保留更多记忆。

### 9.2 变换信号以发现隐藏结构

介绍 Kalman 滤波、频域方法、小波和 path signature。

- [`04_kalman_filter`](04_kalman_filter.ipynb)：把滤波器当作特征提取器，得到水平、趋势、创新和动态对冲比率。
- [`05_spectral_features`](05_spectral_features.ipynb)：演示频域与滚动谱特征。
- [`06_path_signatures`](06_path_signatures.ipynb)：使用 path signature 特征；需要 `ml4t-py312` 镜像。

### 9.3 波动率特征

用 ARIMA、GARCH、HAR 和 rough volatility 描述波动聚集、非对称性和多期限结构。

- [`07_arima_features`](07_arima_features.ipynb)：把 ARIMA 的残差、预测和区间宽度转化为特征。
- [`08_garch_volatility`](08_garch_volatility.ipynb)：提取条件波动率、持续参数和非对称反应。
- [`09_har_rough_volatility`](09_har_rough_volatility.ipynb)：用线性模型组合三个期限的波动率，并估计 roughness 指数。

### 9.4 不确定性特征

把预测分布、采样质量和后验不确定性作为风险条件输入。

- [`10_uncertainty_features`](10_uncertainty_features.ipynb)：前向重拟合随机波动率模型，并诊断其后验是否可用。

### 9.5 Regime 特征

将市场状态作为概率或条件模型，而不是直接当作可靠的择时信号。

- [`11_hmm_regimes`](11_hmm_regimes.ipynb)：从第一性原理推导 HMM regime 推断，并比较 filtered 与 smoothed 输出。
- [`12_wasserstein_regimes`](12_wasserstein_regimes.ipynb)：把时间窗口视为分布，用 Wasserstein 距离聚类。
- [`13_regime_as_feature`](13_regime_as_feature.ipynb)：把 regime 概率写成特征，并在每折内重拟合状态模型。

### 9.6 横截面与面板特征

把时间序列诊断转为排名、基准相对特征、协整关系和 universe 聚合。

- [`14_panel_features`](14_panel_features.ipynb)：演示成对协整、过滤对冲比率和横截面排名特征。

### 9.7 小结

- [`case_study_temporal_summary`](case_study_temporal_summary.ipynb)：检查九个案例研究写入了哪些模型化特征，以及 schema 不能说明的部分。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 09_model_based_features/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "09_model_based_features"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

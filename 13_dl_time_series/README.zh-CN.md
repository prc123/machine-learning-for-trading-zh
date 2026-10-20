# 第 13 章：时间序列深度学习

本章把深度时间序列模型放回可靠的评估框架里：先用强基线判断复杂度是否必要，再比较 RNN、分解模型、attention、状态空间模型、TCN、TSMixer、foundation model 和不确定性方法。

## 学习目标

- 解释为什么循环网络会成为长上下文预测任务的计算和优化瓶颈。
- 比较分解、attention、状态空间和强线性基线四种建模范式，理解各自适用条件。
- 用线性模型和 walk-forward 诊断等强基线判断序列模型复杂度是否合理。
- 理解 PatchTST、iTransformer、TFT 等现代时间序列 Transformer 的设计逻辑，以及它们与多变量结构、协变量和预测期限的关系。
- 判断金融预测问题应建模为带序列输入的直接面板回归，还是多步时间序列预测。
- 评估时间序列 foundation model 的适配方式，包括迁移错配和预训练污染。
- 应用 MC Dropout、deep ensembles 等不确定性估计方法，支持风险感知交易决策。

## 章节脉络

### 13.1 循环网络及其限制

回顾 MLP、1D-CNN、LSTM 和 GRU 的序列建模能力与训练瓶颈。

- [`01_core_architectures`](01_core_architectures.ipynb)：在同一面板和 purged 三段切分下比较基础架构。

### 13.2 N-BEATS 与显式分解

把趋势、季节性和残差分解作为归纳偏置，而不是直接当作可解释的经济事实。

- [`02_nbeats_interpretable`](02_nbeats_interpretable.ipynb)：用 PyTorch 实现通用与可解释 N-BEATS。

### 13.3 时间序列中的 Attention

说明 attention 如何允许模型在不同时间步之间建立数据相关连接，以及为何不能自动等同于因果解释。

### 13.4 线性基线与 Transformer

用 NLinear、DLinear 等方法检验复杂模型的时序结构是否真的被利用。

- [`03_great_debate`](03_great_debate.ipynb)：比较线性模型与 vanilla transformer，并运行 shuffle 诊断。

### 13.5 现代 Transformer 变体

比较 patch 化时间输入、变量历史 token 化和多尺度结构。

- [`04_transformers`](04_transformers.ipynb)：解释 PatchTST 与 iTransformer 中 token 定义的变化，并逐头读取 attention。

### 13.6 替代架构与基础模型

覆盖 TCN、TSMixer、selective state space model、图像化时间序列和 zero-shot foundation models。

- [`05_tcn`](05_tcn.ipynb)：演示因果卷积、逐层 dilation 和残差块。
- [`06_tsmixer`](06_tsmixer.ipynb)：只用 dense 层沿时间与变量轴交替混合。
- [`07_mamba_ssm`](07_mamba_ssm.ipynb)：用可读 Python 循环展示 selective state space model。
- [`08_cnn_image_encoding`](08_cnn_image_encoding.ipynb)：用 Gramian angular field 和 Markov transition field 转换窗口，再交给图像 CNN。
- [`09_foundation_models`](09_foundation_models.ipynb)：比较 Chronos、TinyTimeMixer 与 LSTM、ridge，并指出预训练泄漏通道。

### 13.7 实用框架

选择库和协议比追逐单一架构更重要；必须固定折与日期后再比较。

- [`11_library_landscape`](11_library_landscape.ipynb)：比较 raw PyTorch、sktime 和 Darts 的实现体验。
- [`12_case_study_insights`](12_case_study_insights.ipynb)：读取注册表，比较深度模型与线性、GBM、TabM 基线。

### 13.8 量化预测不确定性

区分模型输出 spread 与具有覆盖率保证的预测区间。

- [`10_uncertainty`](10_uncertainty.ipynb)：比较 MC Dropout、deep ensembles 和 split-conformal calibration。

### 13.9 案例研究洞察

总结在相同折和日期上的可比较结果，而不是混合不同评估窗口的指标。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 13_dl_time_series/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "13_dl_time_series"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

# 第 7 章：定义学习任务

这一章把交易研究问题转换成可训练、可评估、可执行的机器学习任务。重点是让预处理、标签、特征评估、搜索会计和因果合理性检查全部服从时间顺序与决策时点约束。

## 学习目标

- 构建切分感知的预处理管线，为标签和特征计算提供稳定、可审计的输入。
- 定义与执行一致的标签，包括固定期限标签和事件式标签，并诊断重叠、分辨率行为和隐含交易强度。
- 按折评估特征-标签组合，针对连续与离散目标选择合适的稳定性、形态和可行性诊断。
- 用换手率、盈亏平衡成本、流动性和容量检查筛选可实现候选信号。
- 通过定义被搜索集合、分离探索与确认、以及在折级汇总上做多重检验调整来控制搜索偏差。
- 用机制合理性检查区分可能稳定的信号通道与混淆代理变量、时序伪影和聚合效应。

## 章节脉络

### 7.1 数据预处理与编码

建立缺失值、异常值、切分、缩放和编码的处理顺序，防止预处理阶段发生前视偏差。

- [`01_data_quality_diagnostics`](01_data_quality_diagnostics.ipynb)：跨 ML4T 数据集做统一诊断，只评估、不清洗；约需 9 GB 内存。
- [`02_preprocessing_pipeline`](02_preprocessing_pipeline.ipynb)：演示清洗和 `SplitAwarePreprocessor`，避免 lookahead bias；约需 12 GB 内存。
- [`10_ml4t_library_ecosystem`](10_ml4t_library_ecosystem.ipynb)：介绍 `ml4t-data`、`ml4t-engineer` 和 `ml4t-diagnostic` 生态。

### 7.2 标签工程

比较固定期限、事件、三障碍等标签构造，并检查标签隐含的交易频率与可实现性。

- [`03_label_methods`](03_label_methods.ipynb)：演示主要标签方法，是后续建模章节的标签参考。
- [`04_maximum_favorable_adverse_excursion`](04_maximum_favorable_adverse_excursion.ipynb)：用真实价格 excursion 证据校准 triple-barrier 参数。

### 7.3 单变量特征-标签评估

用 Information Coefficient、分位数组合和价差指标判断信号是否有横截面预测力，以及有效期限在哪里。

- [`05_signal_evaluation`](05_signal_evaluation.ipynb)：演示 IC、分位数收益和 spread 诊断。
- [`06_ic_inference`](06_ic_inference.ipynb)：处理自相关 IC 序列，使用 HAC 调整和 block bootstrap 置信区间。

### 7.4 搜索会计与多重检验

当测试大量候选信号时，即使单次推断正确，最好结果仍会被选择偏差推高。

- [`07_multiple_testing`](07_multiple_testing.ipynb)：讨论 factor zoo 问题、FDR 控制和复杂度感知修正。

### 7.5 从相关到因果

在进入第 15 章前先做轻量证伪检查，判断相关结构是否符合提出的经济机制。

- [`08_causal_sanity_checks`](08_causal_sanity_checks.ipynb)：实现特征评估中的轻量证伪测试。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 07_defining_the_learning_task/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "07_defining_the_learning_task"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

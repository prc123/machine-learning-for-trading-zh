# 第 8 章：金融特征工程

本章把交易假设翻译成有明确时间假设、经济驱动和角色分工的特征规格。它覆盖价格衍生特征、跨工具结构特征、慢变量上下文特征，以及特征组合与搜索控制。

## 学习目标

- 用期限对齐、驱动假设和角色分离把交易假设写成文档化特征规格。
- 选择与经济主张和执行期限匹配的参考系、表示法和聚合方式，并区分改变假设的选择与噪声控制选择。
- 区分信号特征与状态变量，判断它们应单独使用、作为交互项使用，还是作为条件变量使用。
- 为价格衍生、结构/跨工具、上下文数据家族设计有代表性的特征规格，显式写出时序假设和失效模式。
- 用 gating、缩放和条件变体把信号与状态变量结合，并检验交互是否带来增量信息。
- 对慢变量和修订数据执行 Point-in-Time 纪律，包括报告滞后、事件时间和 vintage 感知可用性规则。
- 用一次只动一个旋钮、同族去重和多重检验感知分诊控制特征搜索自由度。

## 章节脉络

### 8.1 捕捉并配置经济驱动

先说明“这个特征为什么可能赚钱”，再决定窗口、变换、频率和执行期限。

### 8.2 价格衍生特征

从单资产价格与成交量历史构造动量、波动、回撤、成交量等基础特征族。

- [`01_price_volume_features`](01_price_volume_features.ipynb)：演示单资产量价核心特征。
- [`02_microstructure_features`](02_microstructure_features.ipynb)：捕捉日内 OHLCV 之外的市场动态，代理流动性、信息流和执行质量。

### 8.3 结构与跨工具特征

利用期限结构、跨资产关系和衍生品隐含量，编码单资产价格历史中看不见的信息。

- [`03_structural_cross_instrument_features`](03_structural_cross_instrument_features.ipynb)：演示期限结构、跨工具关系和衍生品隐含特征。

### 8.4 上下文与慢变量特征

用基本面、宏观和日历特征为更快信号提供状态条件。

- [`04_fundamentals_macro_calendar`](04_fundamentals_macro_calendar.ipynb)：覆盖 SEC XBRL、FRED 宏观指标和日历编码，并处理发布滞后。

### 8.5 跨领域特征类型与直接聚合的局限

说明不同数据家族不能机械拼接，必须处理时间尺度、覆盖差异、条件结构和经济含义。

### 8.6 组合特征并控制搜索

把大量候选特征压缩成可维护集合，同时测试稳健性和事件反应。

- [`05_feature_selection`](05_feature_selection.ipynb)：系统筛选、去重并形成生产就绪特征集。
- [`06_robustness_sensitivity`](06_robustness_sensitivity.ipynb)：用参数扫描、regime 条件和信号-状态交互检查稳健性。
- [`07_event_studies`](07_event_studies.ipynb)：测量信号触发、宏观数据发布或财报附近异常收益。
- [`case_study_feature_summary`](case_study_feature_summary.ipynb)：汇总跨案例特征清单、家族热力图和广度-IC 视图。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 08_financial_features/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "08_financial_features"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

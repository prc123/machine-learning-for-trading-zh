# 第 3 章：市场微观结构

本章解释为什么市场数据不能当作中性的价格序列。价差、深度、韧性、订单类型和日内交易状态都会同时影响执行质量和成交/报价数据的含义。对于构建交易系统的人来说，这一章把“价格数据”重新变成包含摩擦、激励和时序效应的经济对象。

## 学习目标

- 解释流动性、订单类型、市场设计和日内交易状态如何影响市场数据与执行质量。
- 区分 L1、L2、L3、TAQ 和增强型 bar 数据等主要市场数据产品，并根据研究或交易目标选择数据。
- 解析基于消息的交易所数据，重建 venue-local limit order book，并维持订单生命周期和簿记不变量。
- 解读关键订单簿指标和经验微观结构模式，同时认识单一交易所可见数据的局限。
- 构建并比较时间、活动和信息驱动的 bar，理解何时需要成交方向分类和 Lee-Ready 对齐。
- 执行日内数据质量和 sessionization 检查，避免顺序、时间戳和日历错误污染下游分析。

## 章节脉络

### 3.1 微观结构如何影响价格形成

说明价差、深度、韧性、订单类型和日内 regime 如何塑造可观测价格与执行结果。

### 3.2 现代市场数据源的解剖

梳理从 top-of-book 报价到完整订单级数据的层次，说明选择数据就是选择研究策略，并解释时间戳语义、延迟和市场分割的影响。

### 3.3 从原始消息到 limit order book

建立解析、标准化、回放、验证和分析订单簿的工作流。示例覆盖 NASDAQ ITCH、Databento MBO、IEX 和 AlgoSeek TAQ，包括 `01_itch_parser.ipynb` 到 `13_algoseek_minute_bars_eda.ipynb`。

### 3.4 采样的艺术：从 tick 到 bar

比较时间、tick、成交量、成交额和信息驱动 bar，说明采样规则会改变训练数据的统计性质。示例包括 `14_itch_bar_sampling.ipynb` 到 `17_databento_bar_sampling.ipynb`。

### 3.5 检测日内收益中的跳跃

使用 bipower variation 和 Lee-Mykland 检验区分日内收益的连续成分与跳跃成分。相关示例为 [`18_algoseek_jump_detection`](18_algoseek_jump_detection.ipynb)。

### 3.6 微观结构数据质量与 sessionization

关注序列错误、时间戳混乱、过期报价、非法订单簿状态转换、错误标记和交易时段边界问题。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 03_market_microstructure/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "03_market_microstructure"
```

### 内存需求

ITCH 与 AlgoSeek TAQ 示例会把多日、多代码的消息或 tick 数据载入内存。端到端运行建议至少 32 GB 内存，64 GB 更理想。高内存示例包括 `04_itch_order_lifecycle_analysis`（约 33 GB）、`05_itch_trading_activity`（约 31 GB）、`11_algoseek_taq_eda`（约 22 GB）、`12_algoseek_taq_lob_reconstruction`（约 22 GB）和 `03_itch_lob_analysis`（约 13 GB）。内存不足时应逐个运行，并在示例之间重启 kernel。

### 运行时间

多数 notebook 一分钟内完成。主要长耗时示例是 `01_itch_parser`：解析一个包含约 4.23 亿条消息的交易日约需 22 分钟，峰值内存约 8 GB。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

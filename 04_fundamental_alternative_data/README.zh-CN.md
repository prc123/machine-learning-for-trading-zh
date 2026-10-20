# 第 4 章：基本面与另类数据

本章聚焦基本面和另类数据中最容易被低估的两件事：Point-in-Time 正确性与实体一致性。它把这些要求落实为双时间存储、as-of 查询、SEC/XBRL 管线、实体与合约映射、另类数据评估和文本特征语料库。

## 学习目标

- 解释为什么 Point-in-Time 正确性和实体一致性是基本面与另类数据的核心工程约束。
- 为频繁修订的金融数据实现 bitemporal 存储和 as-of 查询模式。
- 从 SEC EDGAR 和 XBRL 文件历史构建 Point-in-Time 公司基本面管线。
- 设计时间有效的实体、证券和合约映射流程，综合确定性方法、概率方法和 embedding 方法，并设置质量检查。
- 将 Point-in-Time 对齐规则应用到宏观、大宗商品和链上数据，包括发布时间戳、数据 vintage、合约映射和终局性策略。
- 评估另类数据的增量信号、数据质量、法律合规风险以及商业和工程可行性。
- 抽取、清洗并存储 SEC 文件文本，形成可审计、Point-in-Time 安全的 NLP 语料库。

## 章节脉络

### 4.1 Point-in-Time 数据管线

建立修订、发布时间、可用时间和查询时间的管理框架，避免把后来才知道的信息当作决策时已知。

### 4.2 实体解析与映射

解决公司、证券、合约和数据供应商标识符随时间变化的问题，并加入人工与自动质量检查。

### 4.3 跨资产类别的基本面数据

讨论基本面数据的覆盖范围、报告惯例、资产类别差异和可建模性。

### 4.4 理解另类数据

评估另类数据从信号增量到采购、法律、隐私、容量和工程接入的完整成本。

### 4.5 用文本数据构建 NLP 特征

把监管文件、新闻和公告文本转换为可回放、可审计的语言特征来源。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 04_fundamental_alternative_data/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "04_fundamental_alternative_data"
```

### 必需环境变量

本章部分示例需要 API 凭据。请先查看英文 [`README.md`](README.md) 中的 `Required environment variables`，再配置对应变量。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

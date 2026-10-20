# 第 10 章：文本特征工程

金融文本包含叙事、情绪、事件和风险语言。本章比较词汇模型、静态 embedding、序列模型和 Transformer 的取舍，并说明如何把文本安全地转成 Point-in-Time 特征、评估其信号质量，再进入交易模型。

## 学习目标

- 比较词汇特征、静态 embedding、序列模型和 Transformer 各自保留或丢失的信息。
- 解释 Transformer self-attention 如何产生上下文 embedding，并理解它如何缓解多义词和长距离依赖问题。
- 应用实际金融 NLP 工作流：预训练 checkpoint、必要的领域适配，以及分类或抽取任务的微调。
- 用 Point-in-Time 安全的时间戳、模型 cutoff 和聚合规则设计情绪、叙事意外或结构化事件特征。
- 用期限感知诊断、覆盖率分析和事件时间对齐评估文本信号，而不是只看基准准确率。
- 使用 token 级归因和相关诊断审计、调试和压力测试 NLP 特征。

## 章节脉络

### 10.1 词汇与统计模型

介绍词频、词典法、BM25 和统计表示。它们简单、可解释，但难以处理上下文变化。

### 10.2 静态 Embedding

使用 Word2Vec 和 GloVe 等方法，把词或资产映射到固定向量空间。

### 10.3 序列模型

介绍 RNN、LSTM 和 GRU 如何处理词序，以及长距离依赖和训练效率的局限。

### 10.4 Transformer

通过 self-attention 建立上下文表示，是现代文本分类、情感分析和命名实体抽取的基础。

### 10.5 现代特征提取工作流

从语料时间戳、模型 cutoff、句/文档聚合、事件对齐到特征诊断，形成可部署文本信号。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 10_text_feature_engineering/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "10_text_feature_engineering"
```

### Docker 镜像分工

三个 notebook 需要 `ml4t-py312` 镜像，因为 `gensim` 没有 Python 3.14 wheel：

```bash
docker compose --profile py312 run --rm py312 \
  python 10_text_feature_engineering/01_word2vec_training.py
```

| Notebook | 镜像 |
|---|---|
| `01_word2vec_training` | `ml4t-py312`（gensim Word2Vec） |
| `02_asset_embeddings` | `ml4t-py312`（gensim Word2Vec） |
| `03_sentiment_evolution` | `ml4t-py312`（gensim GloVe loader） |
| `04_bert_finetuning` | `ml4t-gpu`（建议 PyTorch GPU） |
| `05_financial_ner_finetuning` | `ml4t-gpu`（建议 PyTorch GPU） |
| `06_finbert_cross_dataset` | `ml4t-gpu`（建议 PyTorch GPU） |
| `07_news_return_signals` | `ml4t-gpu`（建议 PyTorch GPU） |
| `08_text_feature_evaluation` | `ml4t`（仅 CPU 的 IC 与分位数诊断） |
| `09_filing_text_signals` | `ml4t-gpu`（建议 PyTorch GPU） |

### 运行时间提示

`02_asset_embeddings` 约需 5–6 分钟，为约 500 个 13F 投资组合运行 gensim skip-gram，受 CPU 限制。`09_filing_text_signals` 在 GPU 上约需 7 分钟，用于标普 500 MD&A 文件的 FinBERT 句级评分。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

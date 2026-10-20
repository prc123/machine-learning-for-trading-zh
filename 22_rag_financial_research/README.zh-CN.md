# 第 22 章：面向金融研究的 RAG

金融研究不能接受无证据的语言模型回答。Retrieval-Augmented Generation 把相关文档、结构化元数据、混合检索、重排、引用约束和可验证计算引入生成流程，使回答可审计、可溯源、可拒绝。

## 学习目标

- 解释为什么幻觉使 ungrounded LLM 用法在金融中不可接受，以及 RAG 为什么是核心架构响应。
- 设计从文档摄入到检索和 grounded generation 的金融 RAG 管线，包括结构感知解析、chunking、元数据、embedding 和引用支持。
- 比较通用与领域专用 embedding 模型，并在目标语料上用实际检索指标和延迟权衡评估质量。
- 组合语义检索、词法检索、元数据过滤和重排序，提高金融文档检索的精确率与召回率。
- 使用约束式提示、引用检查和工具验证计算，让答案更忠实、可审计、数值可靠。
- 把 RAG 失败分为检索、上下文、综合、计算和拒答错误，并对每个组件做针对性评估。
- 判断金融应用何时用 RAG、何时用 fine-tuning，并理解 RAG 只是更大 agentic 工作流中的一个工具。

## 章节脉络

### 22.1 从特征抽取到生成

文本特征工程回答“如何编码信号”；RAG 回答“如何基于证据生成、引用和拒绝”。

### 22.2 用 Retrieval-Augmented Generation grounding LLM

先生成或检索候选证据，再让语言模型只基于可引用上下文回答，并保留来源与时间。

### 22.3 智能文档摄入

处理 PDF、HTML、表格、脚注、分节和元数据，保证引用可追踪、时间可过滤。

- [`01_sec_filing_pipeline`](01_sec_filing_pipeline.ipynb)：比较两种 SEC filing 摄入方法，并加入 Point-in-Time 过滤和引用追溯元数据。

### 22.4 领域专用 Embedding

评估通用模型与金融领域模型在术语、实体、事件和披露语境上的差异。

- [`02_domain_embeddings_comparison`](02_domain_embeddings_comparison.ipynb)：比较用于金融文档检索的 embedding 模型。

### 22.5 混合检索与向量数据库

语义检索处理同义表达，词法检索保留精确术语，元数据过滤处理时间、公司、文档类型和来源。

- [`03_hybrid_retrieval`](03_hybrid_retrieval.ipynb)：组合混合检索方法并评估排序质量。

### 22.6 重排序与约束式提示

先用宽召回缩小候选，再用 cross-encoder 重排，最后用引用、模板和工具约束限制生成。

- [`05_10k_rag_assistant`](05_10k_rag_assistant.ipynb)：构建分析 SEC 10-K 的生产级 RAG 助手。

### 22.7 诊断 RAG 管线瓶颈

分别测量上下文命中率、引用有效性、数值一致性、安全性和拒答质量。

- [`04_ragas_evaluation`](04_ragas_evaluation.ipynb)：实现金融导向的 RAG 评估 harness。
- [`08_rag_security`](08_rag_security.ipynb)：评估文档投毒、提示注入等攻击与防御。

### 22.8 应用与战略选择

RAG 适合证据密集型问答；fine-tuning 更适合稳定领域风格、抽取格式或任务行为。

- [`06_esg_rag_vs_finetune`](06_esg_rag_vs_finetune.ipynb)：比较 RAG 与 fine-tuning 在 ESG 分析中的表现。
- [`07_institutional_holdings_graph`](07_institutional_holdings_graph.ipynb)：从 13F 构建 bipartite 机构-股票图，并生成共同持有、机构动量和拥挤信号。

### 22.9 Agentic 框架引介

把检索、工具调用、验证、记忆和多步规划组合起来，为第 24 章的自主 agent 打基础。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 22_rag_financial_research/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "22_rag_financial_research"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

# 第 23 章：面向金融 AI 的知识图谱

向量检索让有证据支持的金融问答变得可行，但它仍在孤立文本块上找相似内容。所有权链、供应链网络、传染路径和关系变化时间需要显式结构。知识图谱把实体表示为节点、关系表示为类型化边、来源表示为属性，从而支持可遍历、可审计、可复用的分析查询。

## 学习目标

- 区分真正需要图结构的金融问题，以及更适合表格数据库或向量检索的问题。
- 设计紧凑、类型化、可审计的金融知识图谱，保证实体身份稳定、关系词汇有限、边级来源可追溯。
- 构建并验证 LLM 辅助抽取管线，把披露文件转换为可回放的图对象，同时控制 schema、重复和时间一致性。
- 解释 Graph RAG 与向量检索的差异，并用受限 text-to-query 生成和确定性数据库执行实现安全关系查询。
- 把图结构转换为泄漏感知的 ML 特征：拓扑、拥挤、集中度和跨图交互。
- 用务实标准评估显式知识图谱、统计金融网络和学习型图表示对预测、组合构建和风险分析的价值。
- 用三时间戳框架和披露时间 cutoff 规则，避免图查询、特征生成和回测中的时间泄漏。
- 为面向生产的金融系统合理选择图数据库、ontology 范围、查询安全和 schema 演进策略。

## 章节脉络

| # | 标题 | 核心思想 |
|---|---|---|
| 23.1 | 关系结构何时释放金融洞察 | 问题具有多跳、结构拥挤或时间演化特征时，图结构的额外成本才值得。 |
| 23.2 | 构建金融知识图谱 | LLM 抽取必须配合身份、schema 和 provenance 契约，使图可回放、可审计。 |
| 23.3 | Graph RAG：确定性关系推理 | 五阶段架构把关系逻辑交给数据库，把语言生成交给 LLM。 |
| 23.4 | 从图到机器学习特征 | centrality、拥挤度、共同持有和跨图交互可转为下游表格特征。 |
| 23.5 | 金融网络：从相关到组合 | MST 和相关网络补充显式 KG；GNN 的收益要在可比较协议下验证。 |
| 23.6 | 时间完整性与无泄漏评估 | 区分事件、披露和抽取时间，并制定 cutoff 安全特征协议。 |
| 23.7 | 构建 KG-ready 管线 | 选择引擎、限制 ontology、约束 text-to-Cypher、管理 schema 版本。 |

## Notebooks

### 图构建

| Notebook | 教学重点 |
|---|---|
| [`01_sp100_sec_download`](01_sp100_sec_download.ipynb) | 从 SEC EDGAR 加载并检查 S&P 100 公司的 10-K、8-K 覆盖与文本质量。 |
| [`02_supply_chain_kg_construction`](02_supply_chain_kg_construction.ipynb) | 用 Qwen2.5-7B 抽取供应商、客户和竞争关系，解析实体并导入 Neo4j。 |
| [`05_institutional_holdings_kg`](05_institutional_holdings_kg.ipynb) | 从 13F 构建机构持仓属性图，演示共同持有和拥挤查询。 |
| [`08_8k_event_extraction`](08_8k_event_extraction.ipynb) | 从 8-K 抽取结构化事件四元组，验证 schema 后以可回放 run identity 入库。 |

### 检索与评估

| Notebook | 教学重点 |
|---|---|
| [`03_graph_rag_qa`](03_graph_rag_qa.ipynb) | 对 13F 图执行受控 text-to-Cypher 问答，强制只读校验、日期过滤和行数限制。 |
| [`04_rag_comparison_benchmark`](04_rag_comparison_benchmark.ipynb) | 在真实 13F 数据上比较图检索与 embedding 检索的支持召回和 token 成本。 |

### 图派生特征与网络

| Notebook | 教学重点 |
|---|---|
| [`09_knowledge_graph_features`](09_knowledge_graph_features.ipynb) | 组合供应链拓扑、13F 拥挤度和跨图交互，生成适合梯度提升的表格特征。 |
| [`10_network_portfolio_construction`](10_network_portfolio_construction.ipynb) | 从美股相关网络和 MST 构建组合，并运行传染模拟。 |
| [`06_gnn_feature_engineering`](06_gnn_feature_engineering.ipynb) | 训练简化 GAT 生成关系 embedding，并比较纯表格模型与混合模型。 |

### 时间完整性

| Notebook | 教学重点 |
|---|---|
| [`07_dynamic_kg_temporal`](07_dynamic_kg_temporal.ipynb) | 区分事件、披露和抽取时间，构建无泄漏快照并检验关系变化与 centrality 漂移。 |

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 23_knowledge_graphs/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "23_knowledge_graphs"

# 无显示环境
MPLBACKEND=Agg PLOTLY_RENDERER=json uv run python 23_knowledge_graphs/<notebook>.py
```

`02_supply_chain_kg_construction`、`05_institutional_holdings_kg`、`08_8k_event_extraction`、`03_graph_rag_qa` 和 `07_dynamic_kg_temporal` 需要运行中的 Neo4j。供应链与 8-K 管线的本地 LLM 抽取使用 vLLM 兼容端点上的 Qwen2.5-7B。

## 依赖

上游：第 4 章提供 13F 机构持仓 loader，第 10 章提供 NER 和文件解析模式，第 22 章提供 RAG 基础。下游供第 12、14、24 章使用。本章库包括 `neo4j`、`networkx`、`torch_geometric`、`edgartools` 和 `sentence-transformers`。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

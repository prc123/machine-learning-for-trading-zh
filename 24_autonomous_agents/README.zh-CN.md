# 第 24 章：自主 Agent

不是所有量化问题都需要 agent。当任务需要多步工具调用、证据保留、检查点、重放、聚合和治理时，agentic workflow 才有价值。本章从认知架构、记忆、工具契约、框架迁移、多 agent 预测、研究 operator 到安全和治理，建立决策级 agent 的工程边界。

## 学习目标

- 判断 agentic workflow 在量化金融中何时有价值，何时传统统计、规则或批处理管线更好。
- 区分 ReAct、Tree of Thoughts 和 Reflexion 的角色，并为证据驱动的金融任务选择合适推理预算。
- 设计显式状态与记忆 schema，支持来源追踪、检查点、重放、schema 演进和事后结果评估。
- 为研究、预测和工作流 agent 指定稳健工具契约、结构化输出、来源策略和上下文工程规则。
- 比较单 agent、多 agent 和 operator 式架构，并定义从 notebook 原型到运营服务的迁移路径。
- 构建证据优先的预测工作流，包括结构化抽取、trace 检查、可重放产物、聚合、校准和评估。
- 设计有边界的研究迭代 operator，允许使用编码、数据、注册表和 skill 检索工具，但保留审计与人工审查。
- 定义使 agent 输出达到决策级所需的运营、统计和安全控制，包括 Point-in-Time 完整性、污染感知测试、可观测性、策略门、沙箱和人工批准边界。

## 章节脉络

### 24.1 从预测函数到 agentic workflow

把 agent 视为有边界、有状态、有工具、有审计轨迹的系统，而不是自由发挥的聊天器。

- [`01_react_reasoning`](01_react_reasoning.ipynb)：回放 ReAct 会话，展示 provider 选择、有限搜索和原始消息 trace。
- [`02_tool_contracts`](02_tool_contracts.ipynb)：演示类型化工具 schema、参数验证、来源和返回域过滤。
- [`03_state_and_memory`](03_state_and_memory.ipynb)：演示显式状态、checkpoint 往返以及覆盖、新鲜度和一致性门。
- [`04_research_agent`](04_research_agent.ipynb)：只在接受保留证据和引用理由时输出有限概率；无证据则弃答。
- [`05_aggregation_math`](05_aggregation_math.ipynb)：演示聚合、Neyman 线性组合、log-odds extremization 和 held-out Platt fitting。
- [`08_forecasting_pipeline`](08_forecasting_pipeline.ipynb)：组合接受 agent 平均、可选辩论、高置信引用 supervisor 更新和固定 log-odds 修正。
- [`09_evaluation_and_governance`](09_evaluation_and_governance.ipynb)：评估预测面板，区分 proper score 与诊断指标。
- [`10_framework_comparison`](10_framework_comparison.ipynb)：在共享阶段上比较原生 Python 与 LangGraph。

### 24.2 认知架构：Agent 如何推理

用 ReAct 组织思考、行动和观察；用 Tree of Thoughts 探索分支；用 Reflexion 累积失败教训。

### 24.3 Agent 记忆：状态、持久化与重放

把证据、工具响应、假设、checkpoint 和最终决策分开存储，使失败可复盘。

### 24.4 工具集成：契约、控制与上下文工程

工具必须有类型、权限、返回域、超时、失败语义和来源标记；上下文要按任务裁剪。

### 24.5 工程栈：框架与迁移

先用显式 Python 定义阶段，再考虑 LangGraph、CrewAI 等框架；迁移不能牺牲可见性和控制。

### 24.6 设计管线核心的研究 agent

证据优先、可拒答、可重放、可审查，并把概率输出与引用理由绑定。

### 24.7 多 agent 预测系统

多 agent 不等于独立证据；必须检查信息来源、相关性、辩论偏移和聚合校准。

- [`06_multi_agent_research`](06_multi_agent_research.ipynb)：回放并行研究 agent，检查聚合敏感性。
- [`07_adversarial_debate`](07_adversarial_debate.ipynb)：回放多空辩论并跟踪概率差距与共识检测。

### 24.8 ML4T 研究 agent

- [`11_research_operator`](11_research_operator.ipynb)：回放两个保留的 operator 实验；除非外部隔离由调用者提供，Bash 会在宿主机运行。

### 24.9 面向生产准备

定义观测、评估、回滚、额度、策略门、人工审批和事故响应路径。

### 24.10 安全与治理

限制文件、网络、shell、凭据和数据权限；测试提示注入、不可信文档和工具滥用。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 24_autonomous_agents/<notebook>.py
```

验证所有 notebook 时，应关闭网络与凭据访问。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

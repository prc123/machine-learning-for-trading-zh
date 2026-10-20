# 第 26 章：MLOps 与治理

模型通过回测和第 25 章部署验证后，真实资金开始流经系统；下一问题是让它持续工作，并在不能工作时安全失效。部署模型都会衰减：市场状态变化、竞争者发现类似信号、模型学到的关系逐步弱化。盈利交易系统与毁灭资本的系统，差别常常在于发现衰减的速度和系统响应的安全程度。

本章构建部署后的基础设施。核心诊断是技术失效与统计失效的区分：技术失效是验证问题，即相同输入产生不同输出；统计失效是绩效问题，即相同输出不再预测收益。混淆二者会浪费时间与资金。章节随后建立检测、响应和自动安全三层体系，并把 feature store、registry、CI/CD 视为按团队成熟度合理裁剪的支持设施。

## 学习目标

1. 区分技术管线分叉与统计绩效衰减，并选择相应诊断和响应工作流。
2. 构建实时监控框架，组合数据完整性门、滚动绩效指标、回测-实盘比较和执行质量检查。
3. 对生产产物应用漂移诊断，包括 PSI、K-S、基于 SHAP 的特征监控，以及 ADWIN 式方法和 DDM 等在线检测器。
4. 设计安全模型更新流程：shadow mode、incumbent 与 candidate 比较、显式晋升标准、分阶段上线门和已测试回滚。
5. 实现交易、策略、组合和系统层的多级 circuit breaker，并明确恢复与人工覆盖纪律。
6. 评估并合理裁剪 MLOps 栈，包括 feature store、数据版本与血缘、模型 registry、实验追踪和 CI/CD 控制。

## 章节脉络

| § | 标题 | 核心思想 |
|---|---|---|
| 26.1 | 实盘交易的两种失效来源 | 用技术失效与统计失效的分类组织后续内容。 |
| 26.2 | 绩效监控 | 滚动指标、警报阈值、看板和回测到实盘实现比率。 |
| 26.3 | 漂移检测 | PSI/K-S 检测数据漂移，SHAP 检测特征漂移，ADWIN 式方法和 DDM 检测概念漂移。 |
| 26.4 | 安全模型更新 | 先 shadow mode，再小资金 A/B，再分阶段上线，均受晋升标准和回滚约束。 |
| 26.5 | Circuit Breaker 与安全 | 多级熔断器和 closed/open/half-open 生命周期。 |
| 26.6 | MLOps 基础设施概览 | Feature store、数据版本、模型 registry 和 CI/CD 应按运维成熟度裁剪。 |
| 26.7 | 小结 | 从检测、响应到自动安全的三层治理模型。 |

## Notebooks

### 检测（§26.2–§26.3）

| Notebook | 教学重点 |
|---|---|
| [`01_drift_monitoring`](01_drift_monitoring.ipynb) | 在 holdout 预测流上构建四面板漂移看板：逐特征 PSI、上线期与最新预测分数密度、滚动 IC 和 hit rate；先验证特征面板，再测量分布变化。 |
| [`02_online_drift_detection`](02_online_drift_detection.ipynb) | 对一年真实预测误差运行误差均值漂移检测和坏日频率 DDM 式监控，并把警报与波动代理、 turbulent episode 对照。 |

### 响应（§26.4）

| Notebook | 教学重点 |
|---|---|
| [`03_safe_model_rollout`](03_safe_model_rollout.ipynb) | 让 candidate 与已部署模型并行 shadow mode，并应用评估开始前固定下来的五项晋升标准；只有全部通过才进入 A/B 和分阶段资金。 |

### 自动安全（§26.5）

| Notebook | 教学重点 |
|---|---|
| [`04_circuit_breakers`](04_circuit_breakers.ipynb) | 构建 closed/open/half-open 状态机，实现回撤、单场亏损、连续亏损 session 和系统延迟四条 halt rule，并记录每次状态转换。 |

### MLOps 基础设施（§26.6）

| Notebook | 教学重点 |
|---|---|
| [`05_feast_feature_store`](05_feast_feature_store.ipynb) | 手写 feature store 会自动化的控制逻辑：feature view、event timestamp、TTL、Point-in-Time offline join、as-of retrieval 和前视效应测量。 |
| [`05b_feast_live`](05b_feast_live.ipynb) | 端到端运行 Feast，并与手写 join 逐特征比对；配置错误时服务可能继续运行但答案错误。需要 `feast>=0.40`。 |
| [`06_mlflow_experiments`](06_mlflow_experiments.ipynb) | 把案例 registry 变成实验目录，解析到可复现文件，再写入 MLflow 并验证查询一致性；排序与部署选择保持分离。 |

## 运行 Notebook

```bash
# 在仓库根目录生产运行
uv run python 26_mlops_governance/01_drift_monitoring.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "26_mlops_governance"

# 执行 notebook 并保留输出
uv run jupyter nbconvert --to notebook --execute --inplace \
  26_mlops_governance/01_drift_monitoring.ipynb
```

执行这些 notebook 时不要设置 `MPLBACKEND=Agg` 或 `PLOTLY_RENDERER=json`，否则会抑制执行后 notebook 应保留的图形。

## 依赖

上游：第 11 章 registry schema，第 16 章基线回测指标，第 19 章回撤和限额框架，第 25 章部署验证。本章关闭实现主线；第 27 章做系统化反思。

关键外部库：Feast（`>=0.40`）、MLflow 3.x、SciPy，以及 `ml4t-data`、`ml4t-diagnostic`。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

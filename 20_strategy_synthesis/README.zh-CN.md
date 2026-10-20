# 第 20 章：策略合成

本章把九个案例研究通过同一标准化管线：数据、特征、标签、模型、预测、组合、成本和风险覆盖层。比较单位是每个案例“从信号到冻结 holdout”的完整弧线，而不是 Sharpe ratio 排行榜。重点是诊断管线在哪里放大或削弱信号、哪类约束在哪种交易游戏中起作用，以及下一轮迭代最值得改进哪里。

## 学习目标

- 把特征分诊账本当作下游策略工作的筛选器，并识别特征级存活何时能、何时不能预测策略级存活。
- 把信号质量、组合转换、成本存活和时间稳定性视为相互独立的评估阶段。
- 比较模型家族经过完整管线后的行为，识别多个配置是否只落在测量误差范围内。
- 把验证集与 holdout 的差异分解为预测质量漂移、组合转换漂移和结构性突变等机制。
- 在现实约束下评估策略，包括适配工具的成本模型、容量限制和多重检验调整。
- 在第 6 章的迭代工作流中确定下一轮优先事项：标签重设计、集成、特征工程或 allocator 研究。
- 应用从数据与诊断、信号生成、策略构建到冻结 holdout 验证的从业者工作流。

## 章节脉络

| # | 标题 | 核心思想 |
|---|---|---|
| 20.1 | 九个案例研究的端到端视图 | 观察每个案例从信号到组合再到 holdout 的完整路径；必要时按 rank-1 集群解读。 |
| 20.2 | 跨案例设置与特征评估 | 用 FDR 控制做特征分诊；特征存活只是筛选器，不是策略存活预测器。 |
| 20.3 | 信号质量与预测不确定性 | 同时看 IC、稳定性、ICIR、正折占比和 checkpoint 敏感性，并回到标签工程。 |
| 20.4 | 从信号到策略 | 用 Fundamental Law 解释节奏、广度和胜率；模型家族排名会在管线后段改变。 |
| 20.5 | 跨案例组合分配 | 当信号广时 HRP 更可能占优；信号弱时 allocator 之间的差距扩大。 |
| 20.6 | 交易现实：成本、容量与执行 | 逐案例计算相对假设成本的盈亏平衡；按名义额计成本不适合某些期权策略。 |
| 20.7 | 风险覆盖层与跨 regime 稳定性 | 区分预测漂移、转换漂移和 regime 变化；覆盖层效果因策略而异。 |
| 20.8 | 因果可信度与混淆偏差 | 把 DML 估计和 refutation 当作脆弱性指标，而不是自动的“真因果”证明。 |
| 20.9 | 局限性与从业者工作流 | 汇总约束、集成机会、顺序化流程和逐案例下一步。 |

## Notebooks

| Notebook | 作用 |
|---|---|
| [`01_aggregate_synthesis`](01_aggregate_synthesis.ipynb) | 把逐案例注册表聚合到 `output/` 下的章级 parquet。 |
| [`02_feature_evaluation`](02_feature_evaluation.ipynb) | 构建跨案例特征分诊漏斗和“特征存活 vs 策略存活”图。 |
| [`03_signal_quality`](03_signal_quality.ipynb) | 生成逐案例、逐模型家族的平均 IC 表，并绘制 IC 与 Sharpe 散点。 |
| [`04_signal_to_strategy`](04_signal_to_strategy.ipynb) | 构建家族级结果级联表、Fundamental Law 诊断和 top-K 扫描。 |
| [`05_portfolio_allocation`](05_portfolio_allocation.ipynb) | 比较 allocator 胜者、最好-最差差距和 allocator 与信号的交互。 |
| [`06_cost_survival`](06_cost_survival.ipynb) | 汇总盈亏平衡记分卡、成本瀑布和 HTM 级联解读。 |
| [`07_regime_risk`](07_regime_risk.ipynb) | 比较验证集与 holdout 衰减，并量化风险覆盖层影响。 |
| [`08_recommendations`](08_recommendations.ipynb) | 汇总管线证据快照、逐案例下一步清单和集成机会。 |

## 运行 Notebook

```bash
# 在仓库根目录按依赖顺序执行
uv run python 20_strategy_synthesis/01_aggregate_synthesis.py
uv run python 20_strategy_synthesis/02_feature_evaluation.py
# ... 到 08_recommendations.py

# 无显示环境
MPLBACKEND=Agg PLOTLY_RENDERER=json uv run python 20_strategy_synthesis/03_signal_quality.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "20_strategy_synthesis"
```

## 依赖

上游：`case_studies/` 中的每个案例必须已有填充完成的 `run_log/registry.db`，包含训练、预测、回测，以及 §20.8 所需的 `causal_runs` 行。holdout 行由各案例自己的 `NN_holdout_predictions` 和 `NN_holdout_backtest` 生成；第 20 章只读取结果，不生成它们。

下游：无。第 20 章是管线的合成终点。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

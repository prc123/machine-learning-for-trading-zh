# 第 21 章：用于执行与对冲的强化学习

执行、做市和衍生品对冲本质上都是顺序决策问题：当前动作会改变库存、状态和后续选择。本章把这些任务表示为部分可观测 Markov Decision Process，比较 DQN 到 actor-critic 的算法，并检查模拟到现实的差距。

## 学习目标

- 把执行、做市和衍生品对冲表述为部分可观测 MDP，设计经济上一致的状态、动作、奖励和约束。
- 根据动作空间结构、样本效率需求和稳定性要求，把 value-based 与 actor-critic RL 方法匹配到金融任务。
- 在受控模拟和加密货币数据中，把 RL 执行策略与 TWAP、Almgren-Chriss 式日程比较，并谨慎解读表观收益。
- 在交易成本下，用 P&L 分布和尾部风险指标比较 deep hedging、delta hedging 和 Whalley-Wilmott 式基准。
- 区分 inverse reinforcement learning 与 behavior cloning，理解奖励推断能和不能从观察到的交易行为中恢复什么。
- 诊断决定可部署性的 simulation-to-reality 风险，包括非平稳性、reward hacking、市场冲击、部分可观测、延迟和基准错配。

## 章节脉络

### 21.1 金融中的顺序决策范式

交易动作不仅影响当期收益，还会改变库存、市场影响、后续状态和可选行动集。

### 21.2 金融市场作为 Markov Decision Processes

定义状态、动作、奖励、转移、折扣和约束，并处理部分可观测与非平稳性。

### 21.3 核心算法：从 DQN 到 Actor-Critic

比较离散动作 value methods 与连续/混合动作 policy gradient、actor-critic 和 PPO。

- [`algorithms_comparison`](01_algorithms_comparison.ipynb)：在相同交互预算下训练 DQN、PPO 和 A2C，并检查动作分布而不只看平均奖励。

### 21.4 应用一：最优交易执行

把清算节奏、冲击、时序风险和信号衰减放进统一环境。

- [`optimal_execution_ppo`](02_optimal_execution_ppo.ipynb)：训练 PPO 控制清算节奏，并与 TWAP、Almgren-Chriss 日程比较。
- [`crypto_execution_rl`](04_crypto_execution_rl.ipynb)：回放已收盘的永续合约小时 bar，把资金费率溢价和下一结算时间纳入状态。

### 21.5 应用二：做市

学习报价偏斜和价差宽度，同时面对库存风险与成交概率的权衡。

- [`market_making_ppo`](03_market_making_ppo.ipynb)：训练 PPO 选择 quote skew 和 spread width，并与三条固定规则比较。

### 21.6 应用三：衍生品的 Deep Hedging

当精确复制不可行时，目标变为选择可接受的 P&L 分布和尾部损失。

- [`deep_hedging_pfhedge`](05_deep_hedging_pfhedge.ipynb)：在离散再平衡和比例成本下对冲 short call，比较五种方法。

### 21.7 逆强化学习：从观察行为学习

给定交易记录，推断什么样的目标会使这些动作合理；推断结果必须可检验。

- [`inverse_reinforcement_learning`](06_inverse_reinforcement_learning.ipynb)：在已知真实目标的规则演示上比较 behavior cloning 和两种奖励推断方法。

### 21.8 模拟到现实的差距

现实市场有机制漂移、冲击反馈、延迟、数据延迟、部分可观测和规则约束；模拟得分不能直接等同可部署能力。

## 小结

- [`backtest_with_impact`](07_backtest_with_impact.ipynb)：在真实美股不同流动性层级上，用四种 square-root impact 强度检验纸面收益会损失多少。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 21_rl_execution_hedging/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "21_rl_execution_hedging"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

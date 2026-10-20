# 第 25 章：实盘交易系统

从盈利回测到实盘执行，是算法交易项目最容易失败的环节。失败常常不是因为策略没有优势，而是生产系统与研究环境在细节上分叉，慢慢侵蚀收益。本章用一个统一框架消除这种分叉：同一策略代码在回测、模拟盘和实盘模式下运行。

## 学习目标

1. 解释为什么研究环境与生产环境的技术分叉是主要失效模式，以及统一框架如何降低该风险。
2. 设计双模式、事件驱动交易架构，让确定性策略逻辑在回测、模拟盘和实盘中不变。
3. 按资产覆盖、执行质量和运维负担比较 broker、交易所和托管平台部署路径。
4. 把订单处理建模为显式状态机，支持部分成交、撤销、拒绝和幂等崩溃恢复。
5. 验证从原始数据、特征、预测、仓位到订单的全管线技术一致性。
6. 用 pre-flight 检查、shadow trading、kill switch 和对账流程规划分阶段实盘上线。

## 章节脉络

| 小节 | 标题 | 核心思想 |
|---|---|---|
| 25.1 | 统一的研究到生产框架 | 回测与实盘使用同一策略代码，消除双管线分叉缺陷。 |
| 25.2 | Interactive Brokers 集成 | IBKR 覆盖多资产，需要管理 TWS/Gateway 连接和状态对账。 |
| 25.3 | Alpaca 集成 | 为美股、ETF 和加密资产提供较低摩擦的 REST/WebSocket 部署。 |
| 25.4 | QuantConnect 与托管平台 | 自托管与托管平台在速度、灵活性和知识产权暴露上的权衡。 |
| 25.5 | 订单生命周期管理 | 实盘执行是有状态异步过程，需要状态机和幂等恢复。 |
| 25.6 | 管线验证保证技术一致性 | 分段测试数据、特征、预测和订单，区分缺陷与市场变化。 |
| 25.7 | 运营就绪 | 纵深防御把“代码能跑”变成“可以投入真实资金”。 |

## Notebooks

### 25.1 统一研究到生产框架

| # | Notebook | 教学重点 |
|---|---|---|
| 01 | [`01_unified_framework_demo`](01_unified_framework_demo.ipynb) | 同一 ETF 数据分别经过 `ml4t.backtest.Engine` 和 `ml4t.live.LiveEngine`，验证双均线策略信号完全一致。 |
| 02 | [`02_etfs_deployment_loop`](02_etfs_deployment_loop.ipynb) | 演示七步部署循环：刷新数据、重算特征、重拟合 Ridge、持久化部署产物、预测 live 窗口、离线回放和写入运行记录。 |

### 25.2 Interactive Brokers 集成

| # | Notebook | 教学重点 |
|---|---|---|
| 03 | [`03_ib_paper_trading_demo`](03_ib_paper_trading_demo.ipynb) | 通过 `IBBroker` 和 `SafeBroker` 连接 TWS/Gateway，启用 shadow mode、头寸/订单/日亏损限制、持久化 `RiskState` 和启动对账。 |
| 12 | [`12_ib_basket_rebalance_demo`](12_ib_basket_rebalance_demo.ipynb) | 在 20 只美股大市值 universe 上执行每日 basket 再平衡、异步提交、成交后状态轮询和滑点汇总。 |

### 25.3 Alpaca 集成

| # | Notebook | 教学重点 |
|---|---|---|
| 04 | [`04_alpaca_paper_trading_demo`](04_alpaca_paper_trading_demo.ipynb) | 完成 Alpaca paper trading 工作流，包括凭据检查、`SafeBroker` 包装、ETF 动量策略和订单类型演示。 |
| 05 | [`05_alpaca_crypto_live_demo`](05_alpaca_crypto_live_demo.ipynb) | 把 Binance USDT 永续研究 universe 映射到 Alpaca USD 现货，只保留可执行子集，并处理 UTC funding hour。 |

### 25.4 QuantConnect 与托管平台

| # | Notebook | 教学重点 |
|---|---|---|
| 06 | [`06_quantconnect_case_study`](06_quantconnect_case_study.ipynb) | 导出 QuantConnect 兼容 JSON 预测，演示“预测桥接”模式，避免在 LEAN 中重写特征工程。 |

### 25.5 订单生命周期管理

| # | Notebook | 教学重点 |
|---|---|---|
| 07 | [`07_order_state_machine`](07_order_state_machine.ipynb) | 实现 10 个状态、19 个合法状态-事件转换的订单状态机，并演示无效转换、撤销竞态和加权成交价。 |

### 25.6 管线一致性验证

| # | Notebook | 教学重点 |
|---|---|---|
| 08 | [`08_pipeline_verification`](08_pipeline_verification.ipynb) | 在确定性合成 tape 上执行 5 项 gated parity 测试和 1 项预期差异（feature warm-up），输出 CI 可用结果。 |
| 09 | [`09_crypto_funding_deployment_loop`](09_crypto_funding_deployment_loop.ipynb) | 用 OKX 作为数据面、Alpaca paper 作为执行面，训练 LightGBM 三分类方向模型并完成一个部署循环。 |
| 11 | [`11_fx_deployment_loop`](11_fx_deployment_loop.ipynb) | 用 IB paper 同时作为 FX 数据面和执行面，计算动量/carry/美元因子特征并执行每日 paper 再平衡。 |

### 25.7 运营就绪

| # | Notebook | 教学重点 |
|---|---|---|
| 10 | [`10_safety_risk_demo`](10_safety_risk_demo.ipynb) | 触发订单规模、头寸、频率、资产限制、kill switch 和 shadow mode 等安全控制的失败路径。 |
| 13 | [`13_runtime_safety_showcase`](13_runtime_safety_showcase.ipynb) | 演示过期数据拒绝、日亏损触发 kill switch、启动对账、运行健康状态转换和 `ml4t-live status`。 |

## 运行 Notebook

```bash
# 在仓库根目录：生产模式
uv run python 25_live_trading/01_unified_framework_demo.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "25_live_trading"

# 无显示环境
MPLBACKEND=Agg PLOTLY_RENDERER=json uv run python 25_live_trading/01_unified_framework_demo.py
```

## 必需环境变量

实盘 broker notebook 从环境变量读取凭据，通常由 `.env` 加载：

- `ALPACA_API_KEY`、`ALPACA_SECRET_KEY`：notebook 02、04、05、09 需要。
- IB TWS 或 Gateway 默认 paper 地址 `127.0.0.1:7497`：notebook 03、11、12 需要。应关闭 `Read-Only API`，并添加回环受信任 IP。每个 notebook 的 `CLIENT_ID` 已固定：03 用 10，11 用 11，12 用 12。
- OKX REST API 的 public 端点无需 key，notebook 09 使用。SDK 属于 `live` extra（`uv sync --extra live`），PyPI 名称是 `python-okx`。

## 延期或环境受限 Notebook

| Notebook | 限制 | 路径 |
|---|---|---|
| `03_ib_paper_trading_demo` | 需要 IB Gateway 启动，并处于美股 regular trading hour（纽约周一至周五 09:30–16:00）。 | 市场时间内运行，TWS 可达且端口为 7497。 |
| `12_ib_basket_rebalance_demo` | 需要 IB Gateway 启动和干净的状态文件对账；重演之间应删除 `~/.ml4t/live_state/basket_demo_*.json`。 | 与 03 相同，并重置状态文件。 |
| `11_fx_deployment_loop` | 需要 IB Gateway；FX 为 24/5，因此不受美股 RTH 限制。 | 常规重跑。 |
| `04_alpaca_paper_trading_demo` | 在 headless papermill 下自动切换 `LIVE_FEED=0` 走模拟路径；真实 WebSocket feed 请在 Jupyter 交互模式运行。 | 显式设置 `ML4T_HEADLESS_PAPERMILL=1`。 |
| `05_alpaca_crypto_live_demo` | 同样在 headless papermill 下自动切换 `LIVE_FEED`。 | 同上。 |

## 依赖

上游第 6–20 章提供案例研究预测；下游第 26 章建立在本章部署验证模式上。关键库包括 `ml4t-backtest`、`ml4t-live`、`alpaca-py`、`ib_async` 和 `python-okx`。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

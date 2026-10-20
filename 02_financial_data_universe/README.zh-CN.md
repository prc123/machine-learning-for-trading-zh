# 第 2 章：金融数据宇宙

本章在接触任何具体数据集之前先建立概念地图。重点不只是“市场数据 / 基本面数据 / 另类数据”的分类，而是说明：每个数据集都内嵌了时间戳、复权、标识符和修订的定义，这些定义决定了它在研究和交易中的真实含义。

## 学习目标

- 区分市场数据、基本面数据和另类数据，理解数据集定义如何影响其研究含义。
- 比较主要资产类别的可观测性、惯例和工程约束，理解市场结构如何改变可测量与可建模的内容。
- 使用金融数据质量框架诊断常见失效模式，重点是 Point-in-Time 违规、幸存者偏差、公司行动错误和标识符错配。
- 从数据质量、法律合规、技术和商业维度进行数据供应商尽调。
- 选择匹配研究与生产需求的存储和查询架构，判断何时使用分区文件、嵌入式分析数据库或服务型数据库。

## 章节脉络

### 2.1 现代金融数据分类

建立数据分类框架，并强调时间戳、复权、标识符与修订机制决定数据语义。

### 2.2 各资产类别的市场数据图景

比较股票、ETP、期货、期权、加密资产、外汇、固定收益、互换和大宗商品的市场结构差异。示例覆盖美股、公司行动、ETF、CME 期货、连续合约、期权、永续合约和外汇，包括 `01_us_equities_eda.ipynb` 到 `12_fx_pairs_eda.ipynb`。

### 2.3 数据采购的尽调框架

把数据风险控制转化为可执行规则：Point-in-Time 正确性、幸存者处理、公司行动方法、标识符完整性、法律权利和可复现版本管理。示例覆盖数据质量框架、Point-in-Time 验证、幸存者偏差检测和供应商比较，即 `13_data_quality_framework.ipynb` 到 `16_provider_comparison.ipynb`。

### 2.4 存储数据

根据访问模式、规模、并发和运维成熟度选择存储方案，并比较文件格式、嵌入式引擎和服务型数据库。示例覆盖端到端管线、数据管理、增量更新和存储基准测试，即 `17_complete_pipeline.ipynb` 到 `22_pandas_polars_benchmark.ipynb`。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 02_financial_data_universe/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "02_financial_data_universe"
```

### NB21 存储基准测试前置条件

`21_storage_benchmark_database` 会测试 DuckDB、SQLite、TimescaleDB、ClickHouse、QuestDB、PostgreSQL 和 Polars Parquet。DuckDB 和 SQLite 可本地运行；其余五个服务需要先启动基准服务栈：

```bash
docker compose --profile benchmark up -d
```

若服务未启动，NB21 会退回到 DuckDB + SQLite 两引擎子集。测试完成后使用 `docker compose --profile benchmark down` 关闭。

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

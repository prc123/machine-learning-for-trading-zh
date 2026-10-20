# 第 14 章：潜在因子模型

潜在因子方法从收益协方差、特征结构和定价误差中提取不可直接观测的风险维度。本章区分“解释协方差的因子”和“被定价的因子”，覆盖 PCA、eigenportfolio、收益率曲线分解、IPCA、RP-PCA、条件自编码器、SDF 和监督自编码器。

## 学习目标

- 区分解释协方差的因子与被定价的因子，并理解这一区别对预测、风险分解和交易的意义。
- 在收益面板上实现 PCA，把主成分读作风险维度或 eigenportfolio，并诊断协方差噪声、成分选择和 loading 不稳定性。
- 解释 IPCA 与 RP-PCA 如何分别通过特征条件化 beta 和定价误差惩罚扩展 PCA。
- 实现带验证选择 checkpoint 和集成分平均的条件自编码器，并区分重建质量与前向排序能力。
- 解释 adversarial SDF 估计如何施加无套利约束，以及它与重建目标的不同。
- 在不同面板和目标下比较潜在因子估计器，并正确解读置信区间重叠的结果。

## 章节脉络

### 14.1 为什么需要潜在因子

说明观测因子无法完全概括风险结构，而潜在方法可以从收益共动中提取维度。

### 14.2 用 PCA 提取潜在因子

介绍特征分解、成分数量、旋转不确定性、bootstrap 置信区间和滚动稳定性。

- [`01_pca_equity_sectors`](01_pca_equity_sectors.ipynb)：对行业 ETF 收益做 PCA，并给 loading 加 bootstrap 置信区间。

### 14.3 股票策略中的 Eigenportfolio

把主成分组合作为风险结构或组合构造对象，同时检查集中度、符号和子空间漂移。

- [`02_eigenportfolios`](02_eigenportfolios.ipynb)：对 500 只高流动性美股做 PCA，分析 sector loading、residual persistence 和两速协方差估计。

### 14.4 解码收益率曲线

用水平、斜率和曲率等成分解释国债收益率变动，并用于因子对冲。

- [`03_yield_curve_decomposition`](03_yield_curve_decomposition.ipynb)：对收益率曲线变化做描述性分解与因子对冲。

### 14.5 连接经济学与统计的高级模型

让特征、风险暴露和定价误差共同约束因子估计。

- [`04_ipca`](04_ipca.ipynb)：在已知 loading 的合成面板上验证子空间恢复，再接入三阶段预测适配器。
- [`05_rp_pca`](05_rp_pca.ipynb)：构造修正协方差矩阵并扫描定价误差权重。

### 14.6 条件自编码器

用特征决定 beta、用管理组合估计因子，并把重建模型与前向预测适配器分开。

- [`06_conditional_autoencoder`](06_conditional_autoencoder.ipynb)：实现 beta 网络与因子网络，并在资产预测层面做集成。

### 14.7 随机贴现因子与监督自编码器

比较无套利定价核学习与带监督 bottleneck 的表示学习。

- [`07_stochastic_discount_factor`](07_stochastic_discount_factor.ipynb)：训练 portfolio-weight network 和对抗 moment network，并分离定价误差与 rank IC。
- [`08_supervised_autoencoder`](08_supervised_autoencoder.ipynb)：共享 bottleneck 的重建头与分类头，使用 purged/embargoed 验证。

### 14.8 案例研究洞察

- [`09_case_study_insights`](09_case_study_insights.ipynb)：只读取案例注册表，不训练模型，并在相同时间戳-实体键上比较方法。

### 14.9 小结

潜在因子适合描述风险结构和生成候选信号，但其解释、旋转、稳定性和定价含义必须分别验证。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 14_latent_factors/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "14_latent_factors"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

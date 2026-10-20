# 第 12 章：梯度提升与高级表格模型

本章从决策树集成走向梯度提升机，并比较 XGBoost、LightGBM、CatBoost 和新兴表格深度学习模型。重点是财务表格数据中的目标选择、时间序列感知调优、TreeSHAP 解释和复杂度是否值得引入。

## 学习目标

- 解释 boosting 与 bagging 的区别，以及顺序误差修正为什么使 GBM 适合财务表格数据。
- 根据类别结构、计算环境、延迟需求、数据规模和可复现性在 XGBoost、LightGBM 和 CatBoost 之间选择。
- 为金融任务选择合适的 GBM 目标和约束，包括逐点回归、learning to rank 和单调约束。
- 用 Optuna 的 pruning、多目标搜索和时间序列感知验证高效调优 GBM。
- 用 TreeSHAP 分析特征效应、交互、不稳定性和部署后的漂移。
- 判断 TabPFN、TabM、TabR 等表格深度学习替代方案何时值得与 GBM 比较。
- 读取跨案例证据，决定非线性树模型的复杂度何时确实换来可验证收益。

## 章节脉络

### 12.1 从决策树到集成

解释高方差树如何通过 bagging 变稳定，再说明 boosting 为什么聚焦残差与难样本。

- [`01_ensemble_foundations`](01_ensemble_foundations.ipynb)：在学术公司特征面板上比较 RF 与 XGBoost、LightGBM、CatBoost。

### 12.2 Gradient Boosting Machines

比较库实现、预设、硬件、规模、排序目标和单调约束。

- [`02_gbm_comparison`](02_gbm_comparison.ipynb)：进行 4 库 × 3 预设 × CPU/GPU 的 ETF 面板基准，并做 500 万行规模测试；建议 GPU。

### 12.3 表格数据的深度学习替代方案

把 TabPFN、TabM 和小型 MLP 与 LightGBM 放在同一 walk-forward 协议下评估。

- [`03_dl_vs_gbm`](03_dl_vs_gbm.ipynb)：比较 walk-forward IC、训练时间和 early stopping 行为。

### 12.4 使用 Optuna 的高级超参数调优

用剪枝、多目标、Pareto front 和跨资产迁移减少无效搜索。

- [`04_optuna_tuning`](04_optuna_tuning.ipynb)：演示单折与 walk-forward HPO、pruning 和 fANOVA 重要性。
- [`05_cross_library_hpo`](05_cross_library_hpo.ipynb)：在相同搜索预算下比较三个 GBM 库。
- [`06_optuna_multi_asset`](06_optuna_multi_asset.ipynb)：多目标优化 IC 与 turnover，并探索跨资产参数迁移。
- [`07_hpo_comparison`](07_hpo_comparison.ipynb)：比较 grid search 与 Optuna TPE。

### 12.5 使用 SHAP 的模型可解释性

检查全局与局部解释、共识重要性、交互效应、漂移和 XAI 的不稳定边界。

- [`08_shap_analysis`](08_shap_analysis.ipynb)：TreeSHAP 全局/局部解释、交互分解和基于 SHAP 的特征选择。
- [`09_xai_limitations`](09_xai_limitations.ipynb)：展示相似预测可能有差异很大的 SHAP 解释。
- [`10_shap_nlp_sentiment`](10_shap_nlp_sentiment.ipynb)：对 FinBERT 情感分类做 token 级归因。
- [`11_conformal_gbm`](11_conformal_gbm.ipynb)：为 GBM 回测构建 split conformal、QR-conformal 和 CQR 区间。

### 12.6 案例研究洞察

- [`12_case_study_insights`](12_case_study_insights.ipynb)：汇总 HAC 推断下的日度合并 IC、网格结果、holdout 衰减和 Linear/GBM/TabM 比较。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 12_gradient_boosting/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "12_gradient_boosting"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

# 第 11 章：机器学习管线

本章建立从统计推断到交易预测的机器学习工作流。重点是正则化线性模型、walk-forward 超参数调优、分类式方向预测、SHAP 解释、conformal 不确定性估计，以及如何把线性模型当作严肃基线而不是过渡工具。

## 学习目标

- 根据预测结果如何转化为交易，在回归和分类两种建模方式之间做选择。
- 拟合无泄漏的 Ridge、LASSO、Elastic Net 和 logistic regression 等正则化线性模型。
- 使用 walk-forward 验证、时间缓冲和必要的嵌套验证调优并评估线性模型。
- 用 SHAP 诊断模型行为，评估特征重要性、经济合理性和稳定性。
- 构建并评估 conformal prediction interval 或 prediction set，监控覆盖率何时退化。
- 通过跨案例证据判断线性模型何时是强基线，弱线性信号何时仍值得进入下一阶段。

## 章节脉络

### 11.1 从推断到预测

先回顾 OLS 的经典推断视角，再转向面向交易决策的样本外预测目标。

- [`01_ols_inference`](01_ols_inference.ipynb)：展示经典统计推断如何定义系数、标准误、置信区间和假设检验。

### 11.2 正则化回归

用惩罚项控制方差、选择变量并提高样本外稳定性。

- [`02_regularization_paths`](02_regularization_paths.ipynb)：比较 OLS、Ridge、LASSO 和 Elastic Net 的正则化路径。
- [`04_nested_cv_hpo`](04_nested_cv_hpo.ipynb)：建立系统化超参数调优流程，避免验证信息泄漏进模型选择。

### 11.3 用 Logistic Regression 预测方向

把涨跌、阈值突破或事件结果建模为分类问题，并讨论类别不平衡与概率校准。

- [`03_logistic_classification`](03_logistic_classification.ipynb)：将 logistic regression 应用于方向预测任务。

### 11.4 用 SHAP 解释模型

把特征贡献从单一全局排名扩展到局部解释和交互结构。

- [`05_shap_analysis`](05_shap_analysis.ipynb)：用 SHAP 解释线性模型的重要特征和预测路径。

### 11.5 量化预测不确定性

用 conformal 方法给预测区间或预测集合赋予经验覆盖率。

- [`06_conformal_prediction`](06_conformal_prediction.ipynb)：演示 conformal prediction 的构建与覆盖诊断。

### 11.6 案例研究洞察

比较线性模型在多个资产和任务中的稳定性，并展示从预测到回测的衔接方式。

- [`07_case_study_insights`](07_case_study_insights.ipynb)：比较九个案例中的线性模型结果。
- [`08_ml_backtest_intro`](08_ml_backtest_intro.ipynb)：提供一个教学式 ML 回测起点。

## 运行 Notebook

```bash
# 在仓库根目录执行
uv run python 11_ml_pipeline/<notebook>.py

# 测试模式（通过 Papermill 减少数据量）
uv run pytest tests/test_chapter_notebooks.py -v -k "11_ml_pipeline"
```

## 参考文献

为便于文献检索，论文与文章标题保留英文；完整列表见 [`README.md`](README.md)。

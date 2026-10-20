# Notebook 中文导览

这份索引覆盖当前仓库的全部 Jupyter notebook，帮助你先判断每个文件在整本书工作流中的位置，再决定是否打开或翻译。

- Notebook 总数：**484**
- Markdown 说明 cell 总数：**9963**
- 原始 notebook 保持不变；代码、输出、图表和路径都以原文件为准。
- 链接从本文件跳到对应 notebook；`说明 cell` 数量越大，通常叙述内容越多。

## 阅读方式

1. 先读章节 `README.md`，确认章节目标和小节结构。
2. 再从下表选择 notebook。文件名通常按章节内顺序排列，`00_` 多为导入与基础概念。
3. 打开 notebook 后，优先看 Markdown 标题、导入库、配置参数和最后的结论 cell。
4. 如果只想运行，不改代码，从仓库根目录按章节 README 的命令执行。

---

## 第 1 章：流程就是你的优势

共 2 个 notebook，60 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [factor_regimes.ipynb](../../01_process_is_edge/factor_regimes.ipynb) | Factor-based regime detection | [中文版](../../01_process_is_edge/factor_regimes.zh-CN.ipynb) | 25 |
| [macro_regimes.ipynb](../../01_process_is_edge/macro_regimes.ipynb) | Macro-based regime detection | [中文版](../../01_process_is_edge/macro_regimes.zh-CN.ipynb) | 35 |

章节说明见 [`01_process_is_edge/README.md`](../../01_process_is_edge/README.md)。

## 第 2 章：金融数据全景

共 22 个 notebook，522 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_us_equities_eda.ipynb](../../02_financial_data_universe/01_us_equities_eda.ipynb) | US Equities — Exploratory Data Analysis | 未翻译 | 13 |
| [02_corporate_actions.ipynb](../../02_financial_data_universe/02_corporate_actions.ipynb) | Corporate Actions: Adjusting for Splits and Dividends | 未翻译 | 25 |
| [03_etfs_eda.ipynb](../../02_financial_data_universe/03_etfs_eda.ipynb) | ETFs — Exploratory Data Analysis | 未翻译 | 17 |
| [04_cme_futures_eda.ipynb](../../02_financial_data_universe/04_cme_futures_eda.ipynb) | CME Futures — Exploratory Data Analysis | [中文版](../../02_financial_data_universe/04_cme_futures_eda.zh-CN.ipynb) | 16 |
| [05_futures_session_aggregation.ipynb](../../02_financial_data_universe/05_futures_session_aggregation.ipynb) | Futures Session Aggregation: Hourly to Daily | 未翻译 | 20 |
| [06_futures_continuous.ipynb](../../02_financial_data_universe/06_futures_continuous.ipynb) | Constructing Continuous Futures Contracts | 未翻译 | 32 |
| [07_sp500_options_eda.ipynb](../../02_financial_data_universe/07_sp500_options_eda.ipynb) | S&P 500 Options Analytics | 未翻译 | 35 |
| [08_options_greeks_computation.ipynb](../../02_financial_data_universe/08_options_greeks_computation.ipynb) | Options Greeks: From Theory to Computation | 未翻译 | 38 |
| [09_options_continuous.ipynb](../../02_financial_data_universe/09_options_continuous.ipynb) | Constructing Continuous Options Series | 未翻译 | 27 |
| [10_crypto_perps_eda.ipynb](../../02_financial_data_universe/10_crypto_perps_eda.ipynb) | Crypto Perps: Exploratory Data Analysis | 未翻译 | 18 |
| [11_crypto_premium_analysis.ipynb](../../02_financial_data_universe/11_crypto_premium_analysis.ipynb) | Crypto Premium Index: Funding Rate Arbitrage Data | 未翻译 | 18 |
| [12_fx_pairs_eda.ipynb](../../02_financial_data_universe/12_fx_pairs_eda.ipynb) | FX Pairs: Exploratory Data Analysis | 未翻译 | 16 |
| [13_data_quality_framework.ipynb](../../02_financial_data_universe/13_data_quality_framework.ipynb) | Data Quality Framework: Validation, Anomalies, and Remediation | 未翻译 | 26 |
| [14_point_in_time_validation.ipynb](../../02_financial_data_universe/14_point_in_time_validation.ipynb) | Point-in-Time (PIT) Data Validation | 未翻译 | 18 |
| [15_survivorship_bias_detection.ipynb](../../02_financial_data_universe/15_survivorship_bias_detection.ipynb) | Survivorship Bias Detection and Quantification | 未翻译 | 26 |
| [16_provider_comparison.ipynb](../../02_financial_data_universe/16_provider_comparison.ipynb) | Provider Comparison: Multi-Source Data Acquisition | 未翻译 | 16 |
| [17_complete_pipeline.ipynb](../../02_financial_data_universe/17_complete_pipeline.ipynb) | Complete Data Pipeline: Multi-Source Acquisition to ML-Ready Data | 未翻译 | 21 |
| [18_data_management.ipynb](../../02_financial_data_universe/18_data_management.ipynb) | Data Management: From Download to Production Pipeline | 未翻译 | 26 |
| [19_incremental_updates.ipynb](../../02_financial_data_universe/19_incremental_updates.ipynb) | Incremental Updates: Keeping Market Data Fresh | 未翻译 | 14 |
| [20_storage_benchmark_file.ipynb](../../02_financial_data_universe/20_storage_benchmark_file.ipynb) | File-Format Storage Benchmark | 未翻译 | 14 |
| [21_storage_benchmark_database.ipynb](../../02_financial_data_universe/21_storage_benchmark_database.ipynb) | Storage Benchmark: Database Engines | 未翻译 | 37 |
| [22_pandas_polars_benchmark.ipynb](../../02_financial_data_universe/22_pandas_polars_benchmark.ipynb) | pandas vs Polars: DataFrame Library Benchmark | 未翻译 | 49 |

章节说明见 [`02_financial_data_universe/README.md`](../../02_financial_data_universe/README.md)。

## 第 3 章：市场微观结构

共 18 个 notebook，334 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_itch_parser.ipynb](../../03_market_microstructure/01_itch_parser.ipynb) | NASDAQ TotalView-ITCH: Order Book Data Parsing | 未翻译 | 14 |
| [02_itch_lob_reconstruction.ipynb](../../03_market_microstructure/02_itch_lob_reconstruction.ipynb) | Order Book Reconstruction from NASDAQ ITCH Messages | 未翻译 | 21 |
| [03_itch_lob_analysis.ipynb](../../03_market_microstructure/03_itch_lob_analysis.ipynb) | LOB Analysis: Stylized Facts and Predictive Patterns | 未翻译 | 24 |
| [04_itch_order_lifecycle_analysis.ipynb](../../03_market_microstructure/04_itch_order_lifecycle_analysis.ipynb) | Order Lifecycle Analysis: From Submission to Cancellation or Execution | 未翻译 | 30 |
| [05_itch_trading_activity.ipynb](../../03_market_microstructure/05_itch_trading_activity.ipynb) | Trading Activity Overview: NASDAQ Market Structure | 未翻译 | 20 |
| [06_itch_intraday_patterns.ipynb](../../03_market_microstructure/06_itch_intraday_patterns.ipynb) | Intraday Patterns: Volume and Volatility Dynamics | 未翻译 | 8 |
| [07_itch_stylized_facts.ipynb](../../03_market_microstructure/07_itch_stylized_facts.ipynb) | Microstructure Stylized Facts: Bid-Ask Bounce and Liquidity | 未翻译 | 13 |
| [08_databento_lob_reconstruction.ipynb](../../03_market_microstructure/08_databento_lob_reconstruction.ipynb) | DataBento MBO: Limit Order Book Reconstruction | 未翻译 | 25 |
| [09_databento_mbo_analysis.ipynb](../../03_market_microstructure/09_databento_mbo_analysis.ipynb) | DataBento MBO: Order Flow Predictability | 未翻译 | 16 |
| [10_iex_lob_reconstruction.ipynb](../../03_market_microstructure/10_iex_lob_reconstruction.ipynb) | IEX LOB Reconstruction: Free Market Data Alternative | 未翻译 | 17 |
| [11_algoseek_taq_eda.ipynb](../../03_market_microstructure/11_algoseek_taq_eda.ipynb) | AlgoSeek TAQ: Anatomy of a Market Crash | 未翻译 | 18 |
| [12_algoseek_taq_lob_reconstruction.ipynb](../../03_market_microstructure/12_algoseek_taq_lob_reconstruction.ipynb) | TAQ LOB Reconstruction: Measuring Trade Aggression | 未翻译 | 15 |
| [13_algoseek_minute_bars_eda.ipynb](../../03_market_microstructure/13_algoseek_minute_bars_eda.ipynb) | NASDAQ-100 Minute Bars - Exploratory Data Analysis | 未翻译 | 26 |
| [14_itch_bar_sampling.ipynb](../../03_market_microstructure/14_itch_bar_sampling.ipynb) | Information-Driven Bars: Beyond Time Sampling | 未翻译 | 19 |
| [15_itch_lee_ready.ipynb](../../03_market_microstructure/15_itch_lee_ready.ipynb) | Lee-Ready Trade Classification Validation | 未翻译 | 12 |
| [16_itch_information_bars.ipynb](../../03_market_microstructure/16_itch_information_bars.ipynb) | Information-Driven Bars: Formulas and Parameter Study | 未翻译 | 10 |
| [17_databento_bar_sampling.ipynb](../../03_market_microstructure/17_databento_bar_sampling.ipynb) | DataBento MBO: Multi-Day Bar Calibration Study | 未翻译 | 31 |
| [18_algoseek_jump_detection.ipynb](../../03_market_microstructure/18_algoseek_jump_detection.ipynb) | Detecting Price Jumps in Intraday Returns | 未翻译 | 15 |

章节说明见 [`03_market_microstructure/README.md`](../../03_market_microstructure/README.md)。

## 第 4 章：基本面与另类数据

共 14 个 notebook，243 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_academic_characteristics.ipynb](../../04_fundamental_alternative_data/01_academic_characteristics.ipynb) | Chen-Pelger-Zhu Academic Asset Pricing Dataset | 未翻译 | 19 |
| [02_sec_filing_explorer.ipynb](../../04_fundamental_alternative_data/02_sec_filing_explorer.ipynb) | EdgarTools: Interactive SEC Filing Analysis | 未翻译 | 21 |
| [03_sec_form4_insider_transactions.ipynb](../../04_fundamental_alternative_data/03_sec_form4_insider_transactions.ipynb) | SEC Form 4: Insider Transaction Analysis | 未翻译 | 13 |
| [04_sec_xbrl_fundamentals.ipynb](../../04_fundamental_alternative_data/04_sec_xbrl_fundamentals.ipynb) | SEC XBRL Fundamentals | 未翻译 | 15 |
| [05_entity_resolution.ipynb](../../04_fundamental_alternative_data/05_entity_resolution.ipynb) | Entity Resolution: Matching Company Names to Identifiers | 未翻译 | 21 |
| [06_fred_macro_eda.ipynb](../../04_fundamental_alternative_data/06_fred_macro_eda.ipynb) | Macro Data Loading: FRED Economic Series | 未翻译 | 21 |
| [07_macro_data_alignment.ipynb](../../04_fundamental_alternative_data/07_macro_data_alignment.ipynb) | Macro Data Alignment: Multi-Frequency Integration | 未翻译 | 18 |
| [08_futures_positioning.ipynb](../../04_fundamental_alternative_data/08_futures_positioning.ipynb) | Futures Positioning: CFTC Commitment of Traders Analysis | 未翻译 | 16 |
| [09_onchain_fundamentals.ipynb](../../04_fundamental_alternative_data/09_onchain_fundamentals.ipynb) | On-Chain Fundamentals: DeFi TVL as Alternative Data | 未翻译 | 17 |
| [10_institutional_holdings_13f.ipynb](../../04_fundamental_alternative_data/10_institutional_holdings_13f.ipynb) | Institutional Holdings from SEC 13F Bulk Data | 未翻译 | 17 |
| [11_defi_tvl_evaluation.ipynb](../../04_fundamental_alternative_data/11_defi_tvl_evaluation.ipynb) | Alternative Data Evaluation: DeFi TVL Case Study | 未翻译 | 17 |
| [12_kalshi_prediction_markets.ipynb](../../04_fundamental_alternative_data/12_kalshi_prediction_markets.ipynb) | Kalshi Prediction Markets: Regulated Event Contracts | 未翻译 | 16 |
| [13_polymarket_prediction_markets.ipynb](../../04_fundamental_alternative_data/13_polymarket_prediction_markets.ipynb) | Polymarket Prediction Markets: Crypto-Settled Event Contracts | 未翻译 | 17 |
| [14_text_data_extraction.ipynb](../../04_fundamental_alternative_data/14_text_data_extraction.ipynb) | Text Data Extraction: Structuring Unstructured Financial Documents | 未翻译 | 15 |

章节说明见 [`04_fundamental_alternative_data/README.md`](../../04_fundamental_alternative_data/README.md)。

## 第 5 章：合成金融数据

共 8 个 notebook，262 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [00_classical_simulation.ipynb](../../05_synthetic_data/00_classical_simulation.ipynb) | Chapter 5: Classical Simulation Methods | 未翻译 | 46 |
| [01_timegan.ipynb](../../05_synthetic_data/01_timegan.ipynb) | TimeGAN: Time-series Generative Adversarial Networks | 未翻译 | 23 |
| [02_tailgan_tail_risk.ipynb](../../05_synthetic_data/02_tailgan_tail_risk.ipynb) | Tail-GAN: Learning to Generate Tail-Risk Preserving Scenarios | 未翻译 | 27 |
| [03_sigcwgan_signatures.ipynb](../../05_synthetic_data/03_sigcwgan_signatures.ipynb) | Chapter 5: Sig-WGAN - Signature-Based Wasserstein GANs | 未翻译 | 44 |
| [04_gtgan_irregular.ipynb](../../05_synthetic_data/04_gtgan_irregular.ipynb) | Chapter 5: GT-GAN - Neural ODEs for Irregular Time Series | 未翻译 | 37 |
| [05_diffusion_ts.ipynb](../../05_synthetic_data/05_diffusion_ts.ipynb) | Diffusion-TS: Interpretable Diffusion with Conditional Generation | 未翻译 | 43 |
| [06_llm_tabular_great.ipynb](../../05_synthetic_data/06_llm_tabular_great.ipynb) | Chapter 5: LLM-Based Tabular Data Generation (GReaT Framework) | 未翻译 | 20 |
| [07_dp_gan.ipynb](../../05_synthetic_data/07_dp_gan.ipynb) | Chapter 5: Differential Privacy for Generative Models | 未翻译 | 22 |

章节说明见 [`05_synthetic_data/README.md`](../../05_synthetic_data/README.md)。

## 第 6 章：策略研究框架

共 3 个 notebook，74 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_where_ideas_come_from.ipynb](../../06_strategy_definition/01_where_ideas_come_from.ipynb) | Where a trading idea meets the data — cross-asset momentum EDA | 未翻译 | 12 |
| [02_cv_foundations.ipynb](../../06_strategy_definition/02_cv_foundations.ipynb) | Cross-Validation for Financial Machine Learning | 未翻译 | 38 |
| [03_case_study_overview.ipynb](../../06_strategy_definition/03_case_study_overview.ipynb) | Case Study Overview: Cross-Strategy Summary | 未翻译 | 24 |

章节说明见 [`06_strategy_definition/README.md`](../../06_strategy_definition/README.md)。

## 第 7 章：定义学习任务

共 9 个 notebook，283 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_data_quality_diagnostics.ipynb](../../07_defining_the_learning_task/01_data_quality_diagnostics.ipynb) | Data Quality Diagnostics | 未翻译 | 35 |
| [02_preprocessing_pipeline.ipynb](../../07_defining_the_learning_task/02_preprocessing_pipeline.ipynb) | Preprocessing Pipeline | 未翻译 | 40 |
| [03_label_methods.ipynb](../../07_defining_the_learning_task/03_label_methods.ipynb) | **Docker image**: `ml4t` | 未翻译 | 40 |
| [04_maximum_favorable_adverse_excursion.ipynb](../../07_defining_the_learning_task/04_maximum_favorable_adverse_excursion.ipynb) | Maximum Favorable/Adverse Excursion (MFE/MAE) Analysis | 未翻译 | 27 |
| [05_signal_evaluation.ipynb](../../07_defining_the_learning_task/05_signal_evaluation.ipynb) | Signal Evaluation: IC, Quantiles, and Spreads | 未翻译 | 40 |
| [06_ic_inference.ipynb](../../07_defining_the_learning_task/06_ic_inference.ipynb) | IC Inference: HAC Adjustment and Block Bootstrap | 未翻译 | 16 |
| [07_multiple_testing.ipynb](../../07_defining_the_learning_task/07_multiple_testing.ipynb) | Multiple Testing and Selection Bias | 未翻译 | 29 |
| [08_causal_sanity_checks.ipynb](../../07_defining_the_learning_task/08_causal_sanity_checks.ipynb) | Mechanism Plausibility Checks for Feature Triage | 未翻译 | 36 |
| [10_ml4t_library_ecosystem.ipynb](../../07_defining_the_learning_task/10_ml4t_library_ecosystem.ipynb) | The ml4t Library Ecosystem | 未翻译 | 20 |

章节说明见 [`07_defining_the_learning_task/README.md`](../../07_defining_the_learning_task/README.md)。

## 第 8 章：金融特征工程

共 8 个 notebook，202 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_price_volume_features.ipynb](../../08_financial_features/01_price_volume_features.ipynb) | Price and Volume Feature Families | 未翻译 | 51 |
| [02_microstructure_features.ipynb](../../08_financial_features/02_microstructure_features.ipynb) | Microstructure Features | 未翻译 | 20 |
| [03_structural_cross_instrument_features.ipynb](../../08_financial_features/03_structural_cross_instrument_features.ipynb) | Structural and Cross-Instrument Features | 未翻译 | 30 |
| [04_fundamentals_macro_calendar.ipynb](../../08_financial_features/04_fundamentals_macro_calendar.ipynb) | Slow Features and Context: Fundamentals, Macro, Calendar | 未翻译 | 30 |
| [05_feature_selection.ipynb](../../08_financial_features/05_feature_selection.ipynb) | Feature Selection and Deduplication | 未翻译 | 22 |
| [06_robustness_sensitivity.ipynb](../../08_financial_features/06_robustness_sensitivity.ipynb) | Robustness and Sensitivity Analysis | 未翻译 | 19 |
| [07_event_studies.ipynb](../../08_financial_features/07_event_studies.ipynb) | Event Studies | 未翻译 | 21 |
| [case_study_feature_summary.ipynb](../../08_financial_features/case_study_feature_summary.ipynb) | Cross-Case-Study Feature Evaluation Summary | 未翻译 | 9 |

章节说明见 [`08_financial_features/README.md`](../../08_financial_features/README.md)。

## 第 9 章：基于模型的特征提取

共 15 个 notebook，309 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_visual_diagnostics.ipynb](../../09_model_based_features/01_visual_diagnostics.ipynb) | Visual Diagnostics and Stationarity Testing | 未翻译 | 19 |
| [02_structural_breaks.ipynb](../../09_model_based_features/02_structural_breaks.ipynb) | Structural Break Detection | 未翻译 | 28 |
| [03_fractional_differencing.ipynb](../../09_model_based_features/03_fractional_differencing.ipynb) | Fractional Differencing | 未翻译 | 22 |
| [04_kalman_filter.ipynb](../../09_model_based_features/04_kalman_filter.ipynb) | Kalman Filters for Financial Feature Extraction | 未翻译 | 21 |
| [05_spectral_features.ipynb](../../09_model_based_features/05_spectral_features.ipynb) | Spectral and Wavelet Features | 未翻译 | 25 |
| [06_path_signatures.ipynb](../../09_model_based_features/06_path_signatures.ipynb) | Path Signatures for Time Series Feature Engineering | 未翻译 | 21 |
| [07_arima_features.ipynb](../../09_model_based_features/07_arima_features.ipynb) | ARIMA as a Feature Extractor | 未翻译 | 14 |
| [08_garch_volatility.ipynb](../../09_model_based_features/08_garch_volatility.ipynb) | GARCH Volatility Features | 未翻译 | 18 |
| [09_har_rough_volatility.ipynb](../../09_model_based_features/09_har_rough_volatility.ipynb) | HAR and Rough Volatility | 未翻译 | 31 |
| [10_uncertainty_features.ipynb](../../09_model_based_features/10_uncertainty_features.ipynb) | Uncertainty Features | 未翻译 | 18 |
| [11_hmm_regimes.ipynb](../../09_model_based_features/11_hmm_regimes.ipynb) | Regime Detection with Hidden Markov Models | 未翻译 | 22 |
| [12_wasserstein_regimes.ipynb](../../09_model_based_features/12_wasserstein_regimes.ipynb) | Wasserstein Regime Clustering | 未翻译 | 24 |
| [13_regime_as_feature.ipynb](../../09_model_based_features/13_regime_as_feature.ipynb) | Regime as Feature | 未翻译 | 16 |
| [14_panel_features.ipynb](../../09_model_based_features/14_panel_features.ipynb) | Panel Features | 未翻译 | 22 |
| [case_study_temporal_summary.ipynb](../../09_model_based_features/case_study_temporal_summary.ipynb) | Cross-Case-Study Temporal Feature Inventory | 未翻译 | 8 |

章节说明见 [`09_model_based_features/README.md`](../../09_model_based_features/README.md)。

## 第 10 章：文本特征工程

共 9 个 notebook，147 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_word2vec_training.ipynb](../../10_text_feature_engineering/01_word2vec_training.ipynb) | Word2Vec: what a word's neighbors can and cannot tell you | 未翻译 | 14 |
| [02_asset_embeddings.ipynb](../../10_text_feature_engineering/02_asset_embeddings.ipynb) | Asset Embeddings: Word2Vec Applied to Portfolios | 未翻译 | 23 |
| [03_sentiment_evolution.ipynb](../../10_text_feature_engineering/03_sentiment_evolution.ipynb) | Three generations of text features on one task | 未翻译 | 14 |
| [04_bert_finetuning.ipynb](../../10_text_feature_engineering/04_bert_finetuning.ipynb) | Fine-tuning a transformer, and checking what its checkpoint already saw | 未翻译 | 14 |
| [05_financial_ner_finetuning.ipynb](../../10_text_feature_engineering/05_financial_ner_finetuning.ipynb) | Financial Named Entity Recognition (NER) Fine-Tuning | 未翻译 | 12 |
| [06_finbert_cross_dataset.ipynb](../../10_text_feature_engineering/06_finbert_cross_dataset.ipynb) | A model scored against labels that mean something else | 未翻译 | 10 |
| [07_news_return_signals.ipynb](../../10_text_feature_engineering/07_news_return_signals.ipynb) | News-Based Alpha Signals: From Text to Factors | 未翻译 | 26 |
| [08_text_feature_evaluation.ipynb](../../10_text_feature_engineering/08_text_feature_evaluation.ipynb) | Does any of this predict anything? | 未翻译 | 13 |
| [09_filing_text_signals.ipynb](../../10_text_feature_engineering/09_filing_text_signals.ipynb) | SEC Filing Signals: From 10-Q Text to Alpha Factors | 未翻译 | 21 |

章节说明见 [`10_text_feature_engineering/README.md`](../../10_text_feature_engineering/README.md)。

## 第 11 章：机器学习流水线

共 8 个 notebook，238 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_ols_inference.ipynb](../../11_ml_pipeline/01_ols_inference.ipynb) | OLS and the Inferential Toolkit | 未翻译 | 26 |
| [02_regularization_paths.ipynb](../../11_ml_pipeline/02_regularization_paths.ipynb) | Regularized Regression for Return Prediction | 未翻译 | 36 |
| [03_logistic_classification.ipynb](../../11_ml_pipeline/03_logistic_classification.ipynb) | Logistic Regression for Return Direction Prediction | 未翻译 | 47 |
| [04_nested_cv_hpo.ipynb](../../11_ml_pipeline/04_nested_cv_hpo.ipynb) | Hyperparameter Selection and Validation Bias | 未翻译 | 27 |
| [05_shap_analysis.ipynb](../../11_ml_pipeline/05_shap_analysis.ipynb) | SHAP Interpretability for Linear Models | 未翻译 | 34 |
| [06_conformal_prediction.ipynb](../../11_ml_pipeline/06_conformal_prediction.ipynb) | Conformal Prediction for Uncertainty-Aware Trading | 未翻译 | 27 |
| [07_case_study_insights.ipynb](../../11_ml_pipeline/07_case_study_insights.ipynb) | Case Study Insights: Linear Models | 未翻译 | 30 |
| [08_ml_backtest_intro.ipynb](../../11_ml_pipeline/08_ml_backtest_intro.ipynb) | From Signals to Returns: The Reality Check | 未翻译 | 11 |

章节说明见 [`11_ml_pipeline/README.md`](../../11_ml_pipeline/README.md)。

## 第 12 章：梯度提升与高级表格模型

共 12 个 notebook，254 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_ensemble_foundations.ipynb](../../12_gradient_boosting/01_ensemble_foundations.ipynb) | Ensemble Foundations: Random Forests vs Gradient Boosting | 未翻译 | 14 |
| [02_gbm_comparison.ipynb](../../12_gradient_boosting/02_gbm_comparison.ipynb) | GBM Library Benchmark: sklearn vs XGBoost vs LightGBM vs CatBoost | 未翻译 | 23 |
| [03_dl_vs_gbm.ipynb](../../12_gradient_boosting/03_dl_vs_gbm.ipynb) | Deep Learning vs GBMs for Tabular Financial Data | 未翻译 | 19 |
| [04_optuna_tuning.ipynb](../../12_gradient_boosting/04_optuna_tuning.ipynb) | Hyperparameter Tuning with Optuna | 未翻译 | 18 |
| [05_cross_library_hpo.ipynb](../../12_gradient_boosting/05_cross_library_hpo.ipynb) | Cross-Library HPO: XGBoost vs LightGBM vs CatBoost | 未翻译 | 22 |
| [06_optuna_multi_asset.ipynb](../../12_gradient_boosting/06_optuna_multi_asset.ipynb) | Multi-Objective HPO and Cross-Asset Transfer | 未翻译 | 16 |
| [07_hpo_comparison.ipynb](../../12_gradient_boosting/07_hpo_comparison.ipynb) | Grid Search vs Optuna: HPO Method Comparison | 未翻译 | 19 |
| [08_shap_analysis.ipynb](../../12_gradient_boosting/08_shap_analysis.ipynb) | SHAP Analysis: Model Explainability and Drift Detection | 未翻译 | 25 |
| [09_xai_limitations.ipynb](../../12_gradient_boosting/09_xai_limitations.ipynb) | XAI Limitations: Explanation Instability | 未翻译 | 10 |
| [10_shap_nlp_sentiment.ipynb](../../12_gradient_boosting/10_shap_nlp_sentiment.ipynb) | Interpreting Financial NLP Models with SHAP | 未翻译 | 10 |
| [11_conformal_gbm.ipynb](../../12_gradient_boosting/11_conformal_gbm.ipynb) | Conformal Prediction for Gradient Boosting Models | 未翻译 | 33 |
| [12_case_study_insights.ipynb](../../12_gradient_boosting/12_case_study_insights.ipynb) | Case Study Insights: Gradient Boosting | 未翻译 | 45 |

章节说明见 [`12_gradient_boosting/README.md`](../../12_gradient_boosting/README.md)。

## 第 13 章：深度学习时间序列

共 12 个 notebook，264 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_core_architectures.ipynb](../../13_dl_time_series/01_core_architectures.ipynb) | Core Deep Learning Architectures for Time Series | 未翻译 | 28 |
| [02_nbeats_interpretable.ipynb](../../13_dl_time_series/02_nbeats_interpretable.ipynb) | Interpretable Forecasting with N-BEATS | 未翻译 | 18 |
| [03_great_debate.ipynb](../../13_dl_time_series/03_great_debate.ipynb) | Linear Baselines Against a Transformer | 未翻译 | 18 |
| [04_transformers.ipynb](../../13_dl_time_series/04_transformers.ipynb) | Transformer Architectures for Time Series | 未翻译 | 22 |
| [05_tcn.ipynb](../../13_dl_time_series/05_tcn.ipynb) | Temporal Convolutional Network | 未翻译 | 15 |
| [06_tsmixer.ipynb](../../13_dl_time_series/06_tsmixer.ipynb) | TSMixer: mixing one axis at a time | 未翻译 | 15 |
| [07_mamba_ssm.ipynb](../../13_dl_time_series/07_mamba_ssm.ipynb) | A selective state space model, written out step by step | 未翻译 | 18 |
| [08_cnn_image_encoding.ipynb](../../13_dl_time_series/08_cnn_image_encoding.ipynb) | Turning a window into a picture: GAF and MTF encodings | 未翻译 | 20 |
| [09_foundation_models.ipynb](../../13_dl_time_series/09_foundation_models.ipynb) | Time series foundation models, applied to a panel they never saw | 未翻译 | 18 |
| [10_uncertainty.ipynb](../../13_dl_time_series/10_uncertainty.ipynb) | From a point forecast to an interval: MC Dropout, deep ensembles, conformal | 未翻译 | 36 |
| [11_library_landscape.ipynb](../../13_dl_time_series/11_library_landscape.ipynb) | The same forecast, written six ways | 未翻译 | 25 |
| [12_case_study_insights.ipynb](../../13_dl_time_series/12_case_study_insights.ipynb) | What the architectures did across the book's case studies | 未翻译 | 31 |

章节说明见 [`13_dl_time_series/README.md`](../../13_dl_time_series/README.md)。

## 第 14 章：潜因子模型

共 9 个 notebook，210 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_pca_equity_sectors.ipynb](../../14_latent_factors/01_pca_equity_sectors.ipynb) | PCA on Sector ETFs with Bootstrap Loading Stability | 未翻译 | 28 |
| [02_eigenportfolios.ipynb](../../14_latent_factors/02_eigenportfolios.ipynb) | Eigenportfolios from US Equities | 未翻译 | 37 |
| [03_yield_curve_decomposition.ipynb](../../14_latent_factors/03_yield_curve_decomposition.ipynb) | Yield Curve Decomposition: Level, Slope, and Curvature | 未翻译 | 24 |
| [04_ipca.ipynb](../../14_latent_factors/04_ipca.ipynb) | Instrumented PCA: Conditional Betas and Factor Forecasts | 未翻译 | 15 |
| [05_rp_pca.ipynb](../../14_latent_factors/05_rp_pca.ipynb) | Risk-Premium PCA: Pricing Information in Latent Factors | 未翻译 | 12 |
| [06_conditional_autoencoder.ipynb](../../14_latent_factors/06_conditional_autoencoder.ipynb) | Conditional Autoencoders: Nonlinear Factor Loadings | 未翻译 | 28 |
| [07_stochastic_discount_factor.ipynb](../../14_latent_factors/07_stochastic_discount_factor.ipynb) | Adversarial Stochastic Discount Factors | 未翻译 | 29 |
| [08_supervised_autoencoder.ipynb](../../14_latent_factors/08_supervised_autoencoder.ipynb) | Supervised Autoencoders: Prediction-Shaped Representations | 未翻译 | 18 |
| [09_case_study_insights.ipynb](../../14_latent_factors/09_case_study_insights.ipynb) | Case Study Insights: Latent Factors | 未翻译 | 19 |

章节说明见 [`14_latent_factors/README.md`](../../14_latent_factors/README.md)。

## 第 15 章：因果机器学习

共 11 个 notebook，235 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_library_overview.ipynb](../../15_causal_estimation/01_library_overview.ipynb) | Causal Inference Library Decision Guide | 未翻译 | 16 |
| [02_dowhy_causal_graph.ipynb](../../15_causal_estimation/02_dowhy_causal_graph.ipynb) | Outcome Choice and Causal Credibility in Crypto Funding Premiums | 未翻译 | 37 |
| [03_econml_dml.ipynb](../../15_causal_estimation/03_econml_dml.ipynb) | Double Machine Learning for Momentum Causal Effect | 未翻译 | 22 |
| [04_dml_crypto_regime.ipynb](../../15_causal_estimation/04_dml_crypto_regime.ipynb) | Double Machine Learning on Crypto Premium Index with Regime Conditioning | 未翻译 | 19 |
| [05_momentum_causal_trading.ipynb](../../15_causal_estimation/05_momentum_causal_trading.ipynb) | Causal Analysis for Trading Decisions: A Momentum Case Study | 未翻译 | 23 |
| [06_fed_announcement_bsts.ipynb](../../15_causal_estimation/06_fed_announcement_bsts.ipynb) | Fed Announcement Event Study with BSTS | 未翻译 | 20 |
| [07_tigramite_time_series.ipynb](../../15_causal_estimation/07_tigramite_time_series.ipynb) | Time Series Causal Discovery with PCMCI | 未翻译 | 17 |
| [08_neural_causal_discovery.ipynb](../../15_causal_estimation/08_neural_causal_discovery.ipynb) | Continuous and Time-Series Causal Discovery | 未翻译 | 28 |
| [09_adia_causal_benchmark.ipynb](../../15_causal_estimation/09_adia_causal_benchmark.ipynb) | Causal Discovery Under a Simulator: Lessons from the ADIA Lab Challenge | 未翻译 | 25 |
| [10_case_study_insights.ipynb](../../15_causal_estimation/10_case_study_insights.ipynb) | Case Study Insights: Causal Estimation | 未翻译 | 12 |
| [11_factor_zoo_validation.ipynb](../../15_causal_estimation/11_factor_zoo_validation.ipynb) | Factor Zoo Validation via Post-Double-Selection LASSO | 未翻译 | 16 |

章节说明见 [`15_causal_estimation/README.md`](../../15_causal_estimation/README.md)。

## 第 16 章：策略模拟

共 18 个 notebook，388 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_backtest_first_principles.ipynb](../../16_strategy_simulation/01_backtest_first_principles.ipynb) | Backtesting First Principles: From Returns to Portfolio Simulation | 未翻译 | 23 |
| [02_futures_backtesting.ipynb](../../16_strategy_simulation/02_futures_backtesting.ipynb) | Futures Backtesting with Contract Specifications | 未翻译 | 29 |
| [03_single_asset_vectorbt.ipynb](../../16_strategy_simulation/03_single_asset_vectorbt.ipynb) | Single Asset Backtest with VectorBT | 未翻译 | 24 |
| [04_single_asset_ml4t_backtest.ipynb](../../16_strategy_simulation/04_single_asset_ml4t_backtest.ipynb) | Single Asset Backtest with ml4t-backtest | 未翻译 | 26 |
| [05_stateful_strategies.ipynb](../../16_strategy_simulation/05_stateful_strategies.ipynb) | Stateful Strategy Patterns | 未翻译 | 40 |
| [06_framework_parity.ipynb](../../16_strategy_simulation/06_framework_parity.ipynb) | ETF momentum: the same strategy run two ways | 未翻译 | 18 |
| [07_engine_divergence_anatomy.ipynb](../../16_strategy_simulation/07_engine_divergence_anatomy.ipynb) | Anatomy of engine divergence | 未翻译 | 24 |
| [08_signal_method_comparison.ipynb](../../16_strategy_simulation/08_signal_method_comparison.ipynb) | Turning prediction scores into trading signals | 未翻译 | 29 |
| [09_performance_reporting.ipynb](../../16_strategy_simulation/09_performance_reporting.ipynb) | Reporting a backtest so somebody else can audit it | 未翻译 | 26 |
| [10_regime_backtest_analysis.ipynb](../../16_strategy_simulation/10_regime_backtest_analysis.ipynb) | Regime-Sliced Performance for the Section 16.4 ETF Baseline | 未翻译 | 19 |
| [11_sharpe_ratio_inference.ipynb](../../16_strategy_simulation/11_sharpe_ratio_inference.ipynb) | How much do you actually know from a Sharpe ratio? | 未翻译 | 29 |
| [12_dsr_validation.ipynb](../../16_strategy_simulation/12_dsr_validation.ipynb) | Correcting a Sharpe ratio for the search that found it | 未翻译 | 28 |
| [13_ras_protocol.ipynb](../../16_strategy_simulation/13_ras_protocol.ipynb) | Charging a strategy for the class it was chosen from | 未翻译 | 21 |
| [14_cost_sensitivity.ipynb](../../16_strategy_simulation/14_cost_sensitivity.ipynb) | How wrong can the cost assumption be before the strategy stops working? | 未翻译 | 13 |
| [15_lean_engine_parity.ipynb](../../16_strategy_simulation/15_lean_engine_parity.ipynb) | LEAN Parity on Current Case-Study Strategies | 未翻译 | 8 |
| [16_case_study_lean_parity.ipynb](../../16_strategy_simulation/16_case_study_lean_parity.ipynb) | Real-Strategy Cross-Framework Audit | 未翻译 | 11 |
| [17_backtrader_zipline_engine_parity.ipynb](../../16_strategy_simulation/17_backtrader_zipline_engine_parity.ipynb) | Backtrader and Zipline on Current Case-Study Strategies | 未翻译 | 10 |
| [18_vectorbt_engine_parity.ipynb](../../16_strategy_simulation/18_vectorbt_engine_parity.ipynb) | VectorBT Pro and OSS on Current Case-Study Strategies | 未翻译 | 10 |

章节说明见 [`16_strategy_simulation/README.md`](../../16_strategy_simulation/README.md)。

## 第 17 章：组合构建

共 12 个 notebook，462 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_portfolio_metrics.ipynb](../../17_portfolio_construction/01_portfolio_metrics.ipynb) | Portfolio Performance Analysis | 未翻译 | 31 |
| [02_mean_variance_optimization.ipynb](../../17_portfolio_construction/02_mean_variance_optimization.ipynb) | Mean-variance optimization, and why its answer is so unstable | 未翻译 | 47 |
| [03_robust_optimization.ipynb](../../17_portfolio_construction/03_robust_optimization.ipynb) | Allocations that estimate less | 未翻译 | 29 |
| [04_kelly_criterion.ipynb](../../17_portfolio_construction/04_kelly_criterion.ipynb) | How much to bet, and why the answer is unusable as given | 未翻译 | 30 |
| [05_factor_allocation_evidence.ipynb](../../17_portfolio_construction/05_factor_allocation_evidence.ipynb) | Which return sources actually diversify each other | 未翻译 | 49 |
| [06_hierarchical_risk_parity.ipynb](../../17_portfolio_construction/06_hierarchical_risk_parity.ipynb) | Hierarchical Risk Parity (HRP) | 未翻译 | 42 |
| [07_conformal_position_sizing.ipynb](../../17_portfolio_construction/07_conformal_position_sizing.ipynb) | Conformal Prediction Position Sizing: Two Case Studies | 未翻译 | 23 |
| [08_library_comparison.ipynb](../../17_portfolio_construction/08_library_comparison.ipynb) | Portfolio Optimization Library Comparison | 未翻译 | 59 |
| [09_allocator_comparison.ipynb](../../17_portfolio_construction/09_allocator_comparison.ipynb) | Portfolio Allocator Comparison | 未翻译 | 51 |
| [11_dl_portfolio_allocation.ipynb](../../17_portfolio_construction/11_dl_portfolio_allocation.ipynb) | Deep Learning for Portfolio Optimization | 未翻译 | 35 |
| [12_vlstm_portfolio.ipynb](../../17_portfolio_construction/12_vlstm_portfolio.ipynb) | VLSTM: Variable-Selection + LSTM for End-to-End Portfolio Learning | 未翻译 | 36 |
| [13_deepm_regime_robust.ipynb](../../17_portfolio_construction/13_deepm_regime_robust.ipynb) | DeePM: Regime-Robust Deep Portfolio Management | 未翻译 | 30 |

章节说明见 [`17_portfolio_construction/README.md`](../../17_portfolio_construction/README.md)。

## 第 18 章：交易成本

共 12 个 notebook，359 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_cost_taxonomy.ipynb](../../18_transaction_costs/01_cost_taxonomy.ipynb) | Cost Taxonomy and Fee Schedules | 未翻译 | 29 |
| [02_spread_estimation.ipynb](../../18_transaction_costs/02_spread_estimation.ipynb) | Spread Estimation from Market Data | 未翻译 | 23 |
| [03_market_impact_calibration.ipynb](../../18_transaction_costs/03_market_impact_calibration.ipynb) | Market Impact Scenarios and Capacity Analysis | 未翻译 | 31 |
| [04_vwap_twap_execution.ipynb](../../18_transaction_costs/04_vwap_twap_execution.ipynb) | VWAP and TWAP Execution Algorithms | 未翻译 | 38 |
| [05_almgren_chriss_optimal_execution.ipynb](../../18_transaction_costs/05_almgren_chriss_optimal_execution.ipynb) | Almgren-Chriss Optimal Execution | 未翻译 | 29 |
| [06_ml4t_execution_demo.ipynb](../../18_transaction_costs/06_ml4t_execution_demo.ipynb) | ML4T Library: Market Impact Models | 未翻译 | 35 |
| [07_ml4t_volume_participation.ipynb](../../18_transaction_costs/07_ml4t_volume_participation.ipynb) | ML4T Library: Volume Participation Limits | 未翻译 | 27 |
| [08_ml_dynamic_execution.ipynb](../../18_transaction_costs/08_ml_dynamic_execution.ipynb) | Reinforcement Learning for Trade Execution | 未翻译 | 22 |
| [09_frequency_tradeoff.ipynb](../../18_transaction_costs/09_frequency_tradeoff.ipynb) | Frequency-Dependent Transaction Costs | 未翻译 | 26 |
| [10_gross_vs_net_performance.ipynb](../../18_transaction_costs/10_gross_vs_net_performance.ipynb) | Gross vs Net Performance Analysis | 未翻译 | 31 |
| [11_cost_cliff.ipynb](../../18_transaction_costs/11_cost_cliff.ipynb) | The Cost Cliff: Intraday Strategy Reality Check | 未翻译 | 29 |
| [12_commission_slippage_comparison.ipynb](../../18_transaction_costs/12_commission_slippage_comparison.ipynb) | Commission & Slippage Model Comparison | 未翻译 | 39 |

章节说明见 [`18_transaction_costs/README.md`](../../18_transaction_costs/README.md)。

## 第 19 章：风险管理

共 11 个 notebook，423 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_var_cvar.ipynb](../../19_risk_management/01_var_cvar.ipynb) | Value at Risk and Conditional Value at Risk | 未翻译 | 35 |
| [02_exit_strategies.ipynb](../../19_risk_management/02_exit_strategies.ipynb) | Exit Strategies for Risk Management | 未翻译 | 53 |
| [03_position_sizing_mae_mfe.ipynb](../../19_risk_management/03_position_sizing_mae_mfe.ipynb) | Position Sizing and MAE/MFE Analysis | 未翻译 | 43 |
| [04_factor_exposure.ipynb](../../19_risk_management/04_factor_exposure.ipynb) | Factor Exposure Analysis | 未翻译 | 32 |
| [05_trade_shap_diagnostics.ipynb](../../19_risk_management/05_trade_shap_diagnostics.ipynb) | Trade SHAP Diagnostics: Model-to-Trading Feedback | 未翻译 | 19 |
| [06_stress_testing.ipynb](../../19_risk_management/06_stress_testing.ipynb) | Stress Testing and Scenario Analysis | 未翻译 | 40 |
| [07_drift_detection.ipynb](../../19_risk_management/07_drift_detection.ipynb) | Feature Drift Detection for Production ML Strategies | 未翻译 | 68 |
| [08_ml_exit_signals.ipynb](../../19_risk_management/08_ml_exit_signals.ipynb) | ML-Based Exit Signals: Two-Model Architecture | 未翻译 | 36 |
| [09_deep_hedging.ipynb](../../19_risk_management/09_deep_hedging.ipynb) | Deep Hedging: From Rules to Learned Risk Controls | 未翻译 | 42 |
| [10_ml4t_backtest_risk_demo.ipynb](../../19_risk_management/10_ml4t_backtest_risk_demo.ipynb) | Composable Exit Rules and Portfolio Limits | 未翻译 | 39 |
| [11_systematic_risk_sweep.ipynb](../../19_risk_management/11_systematic_risk_sweep.ipynb) | Systematic Risk Parameter Sweep | 未翻译 | 16 |

章节说明见 [`19_risk_management/README.md`](../../19_risk_management/README.md)。

## 第 20 章：策略合成

共 8 个 notebook，127 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_aggregate_synthesis.ipynb](../../20_strategy_synthesis/01_aggregate_synthesis.ipynb) | Aggregate Synthesis | 未翻译 | 36 |
| [02_feature_evaluation.ipynb](../../20_strategy_synthesis/02_feature_evaluation.ipynb) | Feature Evaluation Across Case Studies | 未翻译 | 8 |
| [03_signal_quality.ipynb](../../20_strategy_synthesis/03_signal_quality.ipynb) | Signal Evidence: Is the Chosen Signal Trustworthy? | 未翻译 | 11 |
| [04_signal_to_strategy.ipynb](../../20_strategy_synthesis/04_signal_to_strategy.ipynb) | Translation to Strategy: The Central Conversion Story | 未翻译 | 11 |
| [05_portfolio_allocation.ipynb](../../20_strategy_synthesis/05_portfolio_allocation.ipynb) | Portfolio Allocation Across the Case Studies | 未翻译 | 21 |
| [06_cost_survival.ipynb](../../20_strategy_synthesis/06_cost_survival.ipynb) | Friction Survival: Where the Edge Dies | 未翻译 | 11 |
| [07_regime_risk.ipynb](../../20_strategy_synthesis/07_regime_risk.ipynb) | Risk Overlays and Stability Across Regimes | 未翻译 | 13 |
| [08_recommendations.ipynb](../../20_strategy_synthesis/08_recommendations.ipynb) | Strategy Recommendations | 未翻译 | 16 |

章节说明见 [`20_strategy_synthesis/README.md`](../../20_strategy_synthesis/README.md)。

## 第 21 章：用于执行与对冲的强化学习

共 7 个 notebook，145 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_algorithms_comparison.ipynb](../../21_rl_execution_hedging/01_algorithms_comparison.ipynb) | RL Algorithm Comparison: DQN, PPO and A2C on One Trading Environment | 未翻译 | 22 |
| [02_optimal_execution_ppo.ipynb](../../21_rl_execution_hedging/02_optimal_execution_ppo.ipynb) | Optimal Execution with PPO | 未翻译 | 20 |
| [03_market_making_ppo.ipynb](../../21_rl_execution_hedging/03_market_making_ppo.ipynb) | Market Making with PPO | 未翻译 | 16 |
| [04_crypto_execution_rl.ipynb](../../21_rl_execution_hedging/04_crypto_execution_rl.ipynb) | Reinforcement Learning for Crypto Execution | 未翻译 | 18 |
| [05_deep_hedging_pfhedge.ipynb](../../21_rl_execution_hedging/05_deep_hedging_pfhedge.ipynb) | Deep Hedging under Transaction Costs | 未翻译 | 23 |
| [06_inverse_reinforcement_learning.ipynb](../../21_rl_execution_hedging/06_inverse_reinforcement_learning.ipynb) | Inverse Reinforcement Learning for Execution | 未翻译 | 29 |
| [07_backtest_with_impact.ipynb](../../21_rl_execution_hedging/07_backtest_with_impact.ipynb) | Market Impact and Liquidity in Backtests | 未翻译 | 17 |

章节说明见 [`21_rl_execution_hedging/README.md`](../../21_rl_execution_hedging/README.md)。

## 第 22 章：金融研究中的 RAG

共 8 个 notebook，227 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_sec_filing_pipeline.ipynb](../../22_rag_financial_research/01_sec_filing_pipeline.ipynb) | Profiling a Filing Corpus Before You Index It | 未翻译 | 12 |
| [02_domain_embeddings_comparison.ipynb](../../22_rag_financial_research/02_domain_embeddings_comparison.ipynb) | Domain-Specific Embeddings for Financial RAG | 未翻译 | 29 |
| [03_hybrid_retrieval.ipynb](../../22_rag_financial_research/03_hybrid_retrieval.ipynb) | Hybrid Retrieval with Reciprocal Rank Fusion | 未翻译 | 44 |
| [04_ragas_evaluation.ipynb](../../22_rag_financial_research/04_ragas_evaluation.ipynb) | Financial RAG Evaluation Harness | 未翻译 | 26 |
| [05_10k_rag_assistant.ipynb](../../22_rag_financial_research/05_10k_rag_assistant.ipynb) | 10-K Due Diligence Assistant: RAG with Verifiable Citations | 未翻译 | 33 |
| [06_esg_rag_vs_finetune.ipynb](../../22_rag_financial_research/06_esg_rag_vs_finetune.ipynb) | ESG Screening and RAG: Implemented Classifier vs Interface Contract | 未翻译 | 21 |
| [07_institutional_holdings_graph.ipynb](../../22_rag_financial_research/07_institutional_holdings_graph.ipynb) | Institutional Holdings Graph: Point-in-Time 13F Features | 未翻译 | 38 |
| [08_rag_security.ipynb](../../22_rag_financial_research/08_rag_security.ipynb) | Security for Financial Document RAG | 未翻译 | 24 |

章节说明见 [`22_rag_financial_research/README.md`](../../22_rag_financial_research/README.md)。

## 第 23 章：知识图谱

共 10 个 notebook，309 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_sp100_sec_download.ipynb](../../23_knowledge_graphs/01_sp100_sec_download.ipynb) | S&P 100 SEC Filings: Data Overview | 未翻译 | 11 |
| [02_supply_chain_kg_construction.ipynb](../../23_knowledge_graphs/02_supply_chain_kg_construction.ipynb) | Building a Supply Chain Knowledge Graph at Scale | 未翻译 | 67 |
| [03_graph_rag_qa.ipynb](../../23_knowledge_graphs/03_graph_rag_qa.ipynb) | Graph RAG: Safe Text-to-Cypher Question Answering | 未翻译 | 19 |
| [04_rag_comparison_benchmark.ipynb](../../23_knowledge_graphs/04_rag_comparison_benchmark.ipynb) | Vector RAG vs Graph RAG: Real Holdings Benchmark | 未翻译 | 23 |
| [05_institutional_holdings_kg.ipynb](../../23_knowledge_graphs/05_institutional_holdings_kg.ipynb) | Institutional Holdings Knowledge Graph from SEC 13F Filings | 未翻译 | 40 |
| [06_gnn_feature_engineering.ipynb](../../23_knowledge_graphs/06_gnn_feature_engineering.ipynb) | GNN Feature Engineering for Hybrid Models | 未翻译 | 23 |
| [07_dynamic_kg_temporal.ipynb](../../23_knowledge_graphs/07_dynamic_kg_temporal.ipynb) | Temporal Knowledge Graphs with Leakage Controls | 未翻译 | 16 |
| [08_8k_event_extraction.ipynb](../../23_knowledge_graphs/08_8k_event_extraction.ipynb) | Corporate Event Extraction from SEC 8-K Filings at Scale | 未翻译 | 35 |
| [09_knowledge_graph_features.ipynb](../../23_knowledge_graphs/09_knowledge_graph_features.ipynb) | Knowledge Graph Features for Machine Learning | 未翻译 | 41 |
| [10_network_portfolio_construction.ipynb](../../23_knowledge_graphs/10_network_portfolio_construction.ipynb) | Financial Networks for Portfolio Construction | 未翻译 | 34 |

章节说明见 [`23_knowledge_graphs/README.md`](../../23_knowledge_graphs/README.md)。

## 第 24 章：自治智能体

共 11 个 notebook，214 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_react_reasoning.ipynb](../../24_autonomous_agents/01_react_reasoning.ipynb) | LLM Providers and the ReAct Loop | 未翻译 | 14 |
| [02_tool_contracts.ipynb](../../24_autonomous_agents/02_tool_contracts.ipynb) | Tool Contracts and Provenance | 未翻译 | 19 |
| [03_state_and_memory.ipynb](../../24_autonomous_agents/03_state_and_memory.ipynb) | Agent State, Memory, and Quality Gates | 未翻译 | 27 |
| [04_research_agent.ipynb](../../24_autonomous_agents/04_research_agent.ipynb) | The Research Agent | 未翻译 | 27 |
| [05_aggregation_math.ipynb](../../24_autonomous_agents/05_aggregation_math.ipynb) | From Opinions to Probabilities | 未翻译 | 20 |
| [06_multi_agent_research.ipynb](../../24_autonomous_agents/06_multi_agent_research.ipynb) | Multi-Agent Research | 未翻译 | 16 |
| [07_adversarial_debate.ipynb](../../24_autonomous_agents/07_adversarial_debate.ipynb) | Bull vs Bear Debate | 未翻译 | 19 |
| [08_forecasting_pipeline.ipynb](../../24_autonomous_agents/08_forecasting_pipeline.ipynb) | Full Forecasting Pipeline | 未翻译 | 18 |
| [09_evaluation_and_governance.ipynb](../../24_autonomous_agents/09_evaluation_and_governance.ipynb) | Scoring, Replay, and Security | 未翻译 | 23 |
| [10_framework_comparison.ipynb](../../24_autonomous_agents/10_framework_comparison.ipynb) | Framework Comparison: Native SDK vs CrewAI vs LangGraph | 未翻译 | 9 |
| [11_research_operator.ipynb](../../24_autonomous_agents/11_research_operator.ipynb) | The ML4T Research Operator: one autonomous iteration on a real case study | 未翻译 | 22 |

章节说明见 [`24_autonomous_agents/README.md`](../../24_autonomous_agents/README.md)。

## 第 25 章：实盘交易系统

共 13 个 notebook，322 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_unified_framework_demo.ipynb](../../25_live_trading/01_unified_framework_demo.ipynb) | Unified Framework Demo: Same Strategy, Backtest to Live | 未翻译 | 20 |
| [02_etfs_deployment_loop.ipynb](../../25_live_trading/02_etfs_deployment_loop.ipynb) | ETFs Deployment Loop | 未翻译 | 19 |
| [03_ib_paper_trading_demo.ipynb](../../25_live_trading/03_ib_paper_trading_demo.ipynb) | Interactive Brokers Paper Trading Demo | 未翻译 | 21 |
| [04_alpaca_paper_trading_demo.ipynb](../../25_live_trading/04_alpaca_paper_trading_demo.ipynb) | Alpaca Paper Trading Demo | 未翻译 | 19 |
| [05_alpaca_crypto_live_demo.ipynb](../../25_live_trading/05_alpaca_crypto_live_demo.ipynb) | Alpaca Crypto Live Trading Demo | 未翻译 | 14 |
| [06_quantconnect_case_study.ipynb](../../25_live_trading/06_quantconnect_case_study.ipynb) | QuantConnect Deployment: Prediction Export Bridge | 未翻译 | 17 |
| [07_order_state_machine.ipynb](../../25_live_trading/07_order_state_machine.ipynb) | Order Lifecycle State Machine | 未翻译 | 20 |
| [08_pipeline_verification.ipynb](../../25_live_trading/08_pipeline_verification.ipynb) | Pipeline Verification: Backtest vs Live Parity | 未翻译 | 39 |
| [09_crypto_funding_deployment_loop.ipynb](../../25_live_trading/09_crypto_funding_deployment_loop.ipynb) | Crypto Funding Deployment Loop | 未翻译 | 44 |
| [10_safety_risk_demo.ipynb](../../25_live_trading/10_safety_risk_demo.ipynb) | SafeBroker Risk Controls Demo | 未翻译 | 29 |
| [11_fx_deployment_loop.ipynb](../../25_live_trading/11_fx_deployment_loop.ipynb) | FX Pairs Deployment Loop | 未翻译 | 28 |
| [12_ib_basket_rebalance_demo.ipynb](../../25_live_trading/12_ib_basket_rebalance_demo.ipynb) | Interactive Brokers Basket Rebalance Demo | 未翻译 | 34 |
| [13_runtime_safety_showcase.ipynb](../../25_live_trading/13_runtime_safety_showcase.ipynb) | Runtime Safety Showcase: Stale Data, Kill Switch, Reconciliation, Health | 未翻译 | 18 |

章节说明见 [`25_live_trading/README.md`](../../25_live_trading/README.md)。

## 第 26 章：MLOps 与治理

共 7 个 notebook，148 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_drift_monitoring.ipynb](../../26_mlops_governance/01_drift_monitoring.ipynb) | Drift Monitoring on Real Case-Study Artifacts | 未翻译 | 21 |
| [02_online_drift_detection.ipynb](../../26_mlops_governance/02_online_drift_detection.ipynb) | Online Drift Detection on Real Validation Streams | 未翻译 | 19 |
| [03_safe_model_rollout.ipynb](../../26_mlops_governance/03_safe_model_rollout.ipynb) | Safe Model Rollout: a Promotion Gate a Challenger Has to Clear | 未翻译 | 26 |
| [04_circuit_breakers.ipynb](../../26_mlops_governance/04_circuit_breakers.ipynb) | Circuit Breakers for Trading Systems | 未翻译 | 27 |
| [05_feast_feature_store.ipynb](../../26_mlops_governance/05_feast_feature_store.ipynb) | Feature Store Patterns on Real Case-Study Artifacts | 未翻译 | 15 |
| [05b_feast_live.ipynb](../../26_mlops_governance/05b_feast_live.ipynb) | Feature Store with Feast: Live Integration | 未翻译 | 15 |
| [06_mlflow_experiments.ipynb](../../26_mlops_governance/06_mlflow_experiments.ipynb) | Experiment Tracking with MLflow and the Case-Study Registry | 未翻译 | 25 |

章节说明见 [`26_mlops_governance/README.md`](../../26_mlops_governance/README.md)。

## 案例研究：CME 期货

共 21 个 notebook，267 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/cme_futures/01_feasibility_analysis.ipynb) | CME Futures: Feasibility Analysis | 未翻译 | 19 |
| [02_labels.ipynb](../../case_studies/cme_futures/02_labels.ipynb) | CME Futures: Label Engineering | 未翻译 | 24 |
| [03_financial_features.ipynb](../../case_studies/cme_futures/03_financial_features.ipynb) | CME Futures: Feature Engineering | 未翻译 | 31 |
| [04_model_based_features.ipynb](../../case_studies/cme_futures/04_model_based_features.ipynb) | CME Futures: Features That Are Themselves Model Output | 未翻译 | 53 |
| [05_evaluation.ipynb](../../case_studies/cme_futures/05_evaluation.ipynb) | Feature Evaluation - CME Futures | 未翻译 | 32 |
| [06_linear.ipynb](../../case_studies/cme_futures/06_linear.ipynb) | CME futures: regularizing a design matrix built in blocks | 未翻译 | 14 |
| [07_gbm.ipynb](../../case_studies/cme_futures/07_gbm.ipynb) | CME futures: capacity, loss function, and when to stop adding trees | 未翻译 | 16 |
| [08_tabular_dl.ipynb](../../case_studies/cme_futures/08_tabular_dl.ipynb) | CME Futures: Tabular Deep Learning | 未翻译 | 4 |
| [09_dl_lstm.ipynb](../../case_studies/cme_futures/09_dl_lstm.ipynb) | CME Futures: Sequence Models | 未翻译 | 4 |
| [10_latent_factors.ipynb](../../case_studies/cme_futures/10_latent_factors.ipynb) | CME Futures: Latent-Factor Requests | 未翻译 | 2 |
| [10a_pca.ipynb](../../case_studies/cme_futures/10a_pca.ipynb) | CME Futures: Principal-Component Factors | 未翻译 | 4 |
| [10b_stochastic_discount_factor.ipynb](../../case_studies/cme_futures/10b_stochastic_discount_factor.ipynb) | CME Futures: Stochastic Discount-Factor Features | 未翻译 | 4 |
| [11_causal_dml.ipynb](../../case_studies/cme_futures/11_causal_dml.ipynb) | CME Futures: Double Machine Learning | 未翻译 | 4 |
| [12_model_analysis.ipynb](../../case_studies/cme_futures/12_model_analysis.ipynb) | CME Futures: Model Analysis | 未翻译 | 8 |
| [13_backtest.ipynb](../../case_studies/cme_futures/13_backtest.ipynb) | CME Futures: Equal-Weight Signal Backtests | 未翻译 | 7 |
| [14_portfolio_management.ipynb](../../case_studies/cme_futures/14_portfolio_management.ipynb) | CME Futures: Portfolio Allocation | 未翻译 | 7 |
| [15_risk_management.ipynb](../../case_studies/cme_futures/15_risk_management.ipynb) | CME Futures: Risk Overlays | 未翻译 | 6 |
| [16_costs.ipynb](../../case_studies/cme_futures/16_costs.ipynb) | CME Futures: Transaction-Cost Sensitivity | 未翻译 | 6 |
| [17_holdout_predictions.ipynb](../../case_studies/cme_futures/17_holdout_predictions.ipynb) | CME Futures: Holdout Predictions | 未翻译 | 8 |
| [18_holdout_backtest.ipynb](../../case_studies/cme_futures/18_holdout_backtest.ipynb) | CME Futures: Holdout Backtest | 未翻译 | 6 |
| [19_strategy_analysis.ipynb](../../case_studies/cme_futures/19_strategy_analysis.ipynb) | CME Futures: Strategy Analysis | 未翻译 | 8 |

章节说明见 [`case_studies/cme_futures/README.md`](../../case_studies/cme_futures/README.md)。

## 案例研究：加密货币永续合约资金费率

共 20 个 notebook，267 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/crypto_perps_funding/01_feasibility_analysis.ipynb) | Crypto Perpetuals Funding: Feasibility Analysis | 未翻译 | 18 |
| [02_labels.ipynb](../../case_studies/crypto_perps_funding/02_labels.ipynb) | Crypto Perpetuals: Label Engineering | 未翻译 | 24 |
| [03_financial_features.ipynb](../../case_studies/crypto_perps_funding/03_financial_features.ipynb) | Crypto Perps Funding: Feature Engineering | 未翻译 | 31 |
| [04_model_based_features.ipynb](../../case_studies/crypto_perps_funding/04_model_based_features.ipynb) | Crypto perpetuals: features that are themselves model output | 未翻译 | 34 |
| [05_evaluation.ipynb](../../case_studies/crypto_perps_funding/05_evaluation.ipynb) | Feature Evaluation - Crypto Perpetuals Funding | 未翻译 | 21 |
| [06_linear.ipynb](../../case_studies/crypto_perps_funding/06_linear.ipynb) | Crypto perpetuals: a design matrix that is mostly one number | 未翻译 | 12 |
| [07_gbm.ipynb](../../case_studies/crypto_perps_funding/07_gbm.ipynb) | Crypto perpetuals: 400 candidate models from two validation years | 未翻译 | 15 |
| [08_tabular_dl.ipynb](../../case_studies/crypto_perps_funding/08_tabular_dl.ipynb) | TabM on the funding panel, and what a network adds that a tree does not | 未翻译 | 5 |
| [09_dl_lstm.ipynb](../../case_studies/crypto_perps_funding/09_dl_lstm.ipynb) | Does the premium's path carry more than its summaries? | 未翻译 | 6 |
| [10_dl_tcn.ipynb](../../case_studies/crypto_perps_funding/10_dl_tcn.ipynb) | A third way to read the same window | 未翻译 | 5 |
| [11_causal_dml.ipynb](../../case_studies/crypto_perps_funding/11_causal_dml.ipynb) | A different question from the one every other model here asks | 未翻译 | 5 |
| [12_model_analysis.ipynb](../../case_studies/crypto_perps_funding/12_model_analysis.ipynb) | What the fitted models can and cannot tell you about funding | 未翻译 | 7 |
| [13_backtest.ipynb](../../case_studies/crypto_perps_funding/13_backtest.ipynb) | Crypto perpetuals: the baseline that turns a ranking into a book | 未翻译 | 13 |
| [14_portfolio_management.ipynb](../../case_studies/crypto_perps_funding/14_portfolio_management.ipynb) | Crypto perpetuals: six ways to size a position the ranking already chose | 未翻译 | 11 |
| [15_risk_management.ipynb](../../case_studies/crypto_perps_funding/15_risk_management.ipynb) | Crypto perpetuals: fourteen ways to leave a position early | 未翻译 | 10 |
| [16_costs.ipynb](../../case_studies/crypto_perps_funding/16_costs.ipynb) | Crypto perpetuals: how much friction the surviving configuration absorbs | 未翻译 | 11 |
| [17_holdout_predictions.ipynb](../../case_studies/crypto_perps_funding/17_holdout_predictions.ipynb) | Crypto Perpetuals Funding: Holdout Predictions | 未翻译 | 8 |
| [18_holdout_backtest.ipynb](../../case_studies/crypto_perps_funding/18_holdout_backtest.ipynb) | Crypto Perpetuals Funding: Holdout Backtest | 未翻译 | 6 |
| [19_strategy_analysis.ipynb](../../case_studies/crypto_perps_funding/19_strategy_analysis.ipynb) | Crypto perpetuals: what the search actually found | 未翻译 | 13 |
| [11_autoencoder.ipynb](../../case_studies/crypto_perps_funding/_archive/11_autoencoder.ipynb) | Autoencoder on Crypto Returns | 未翻译 | 12 |

章节说明见 [`case_studies/crypto_perps_funding/README.md`](../../case_studies/crypto_perps_funding/README.md)。

## 案例研究：ETF

共 26 个 notebook，443 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/etfs/01_feasibility_analysis.ipynb) | ETFs: Feasibility Analysis | 未翻译 | 19 |
| [02_labels.ipynb](../../case_studies/etfs/02_labels.ipynb) | ETFs: Label Engineering | 未翻译 | 23 |
| [03_financial_features.ipynb](../../case_studies/etfs/03_financial_features.ipynb) | ETFs: Feature Engineering | 未翻译 | 32 |
| [04_model_based_features.ipynb](../../case_studies/etfs/04_model_based_features.ipynb) | ETFs: model-based features | 未翻译 | 34 |
| [05_evaluation.ipynb](../../case_studies/etfs/05_evaluation.ipynb) | ETFs: which features carry information about the forward return | 未翻译 | 31 |
| [06_linear.ipynb](../../case_studies/etfs/06_linear.ipynb) | ETFs: how much regularization does a collinear feature set need | 未翻译 | 14 |
| [07_gbm.ipynb](../../case_studies/etfs/07_gbm.ipynb) | ETFs: what trees can find that a penalty cannot, and what they give up to look | 未翻译 | 17 |
| [08_tabular_dl.ipynb](../../case_studies/etfs/08_tabular_dl.ipynb) | ETFs: a neural network on the same flat table, and what an ensemble of them costs | 未翻译 | 13 |
| [09_dl_lstm.ipynb](../../case_studies/etfs/09_dl_lstm.ipynb) | LSTM for ETF Cross-Asset Momentum | 未翻译 | 12 |
| [10_dl_tsmixer.ipynb](../../case_studies/etfs/10_dl_tsmixer.ipynb) | TSMixer as a Global ETF Sequence Model | 未翻译 | 12 |
| [10a_dl_nlinear.ipynb](../../case_studies/etfs/10a_dl_nlinear.ipynb) | NLinear as a Global ETF Sequence Model | 未翻译 | 14 |
| [11_latent_factors.ipynb](../../case_studies/etfs/11_latent_factors.ipynb) | ETFs: what the latent-factor family is, and who publishes what | 未翻译 | 7 |
| [11a_pca.ipynb](../../case_studies/etfs/11a_pca.ipynb) | ETFs: factors taken from the return panel alone | 未翻译 | 15 |
| [11b_ipca.ipynb](../../case_studies/etfs/11b_ipca.ipynb) | ETFs: letting the features set the exposures | 未翻译 | 15 |
| [11c_conditional_autoencoder.ipynb](../../case_studies/etfs/11c_conditional_autoencoder.ipynb) | ETFs: the same factor structure with a network in place of the linear map | 未翻译 | 13 |
| [11d_stochastic_discount_factor.ipynb](../../case_studies/etfs/11d_stochastic_discount_factor.ipynb) | ETFs: a model that prices the cross-section instead of predicting it | 未翻译 | 14 |
| [11e_supervised_autoencoder.ipynb](../../case_studies/etfs/11e_supervised_autoencoder.ipynb) | ETFs: a conditioned network with no factor structure | 未翻译 | 13 |
| [12_causal_dml.ipynb](../../case_studies/etfs/12_causal_dml.ipynb) | ETF momentum: a causal estimate, not a forecast | 未翻译 | 10 |
| [13_model_analysis.ipynb](../../case_studies/etfs/13_model_analysis.ipynb) | ETF models compared: which of these signals is real | 未翻译 | 50 |
| [14_backtest.ipynb](../../case_studies/etfs/14_backtest.ipynb) | ETF rotation: from a predicted ranking to a traded strategy | 未翻译 | 14 |
| [15_portfolio_management.ipynb](../../case_studies/etfs/15_portfolio_management.ipynb) | ETF allocation: how much is the signal, and how much is the weighting | 未翻译 | 13 |
| [16_risk_management.ipynb](../../case_studies/etfs/16_risk_management.ipynb) | ETF risk overlays: what a stop costs when the holding period is a month | 未翻译 | 9 |
| [17_costs.ipynb](../../case_studies/etfs/17_costs.ipynb) | ETF costs: where the edge runs out | 未翻译 | 8 |
| [18_holdout_predictions.ipynb](../../case_studies/etfs/18_holdout_predictions.ipynb) | ETFs: Holdout Predictions | 未翻译 | 8 |
| [19_holdout_backtest.ipynb](../../case_studies/etfs/19_holdout_backtest.ipynb) | ETFs: Holdout Backtest | 未翻译 | 6 |
| [20_strategy_analysis.ipynb](../../case_studies/etfs/20_strategy_analysis.ipynb) | ETFs - Strategy Analysis | 未翻译 | 27 |

章节说明见 [`case_studies/etfs/README.md`](../../case_studies/etfs/README.md)。

## 案例研究：外汇货币对

共 20 个 notebook，272 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/fx_pairs/01_feasibility_analysis.ipynb) | FX Pairs: Feasibility Analysis | 未翻译 | 21 |
| [02_labels.ipynb](../../case_studies/fx_pairs/02_labels.ipynb) | FX Pairs: Label Engineering | 未翻译 | 21 |
| [03_financial_features.ipynb](../../case_studies/fx_pairs/03_financial_features.ipynb) | FX Pairs: Feature Engineering | 未翻译 | 27 |
| [04_model_based_features.ipynb](../../case_studies/fx_pairs/04_model_based_features.ipynb) | FX Pairs: Features Built From Fitted Models | 未翻译 | 59 |
| [05_evaluation.ipynb](../../case_studies/fx_pairs/05_evaluation.ipynb) | FX Pairs: Feature Evaluation | 未翻译 | 26 |
| [06_linear.ipynb](../../case_studies/fx_pairs/06_linear.ipynb) | FX pairs: regularizing when the cross-section itself is dependent | 未翻译 | 15 |
| [07_gbm.ipynb](../../case_studies/fx_pairs/07_gbm.ipynb) | FX pairs: what a tree can express that a weighted sum cannot | 未翻译 | 16 |
| [08_tabular_dl.ipynb](../../case_studies/fx_pairs/08_tabular_dl.ipynb) | Tabular Deep Learning - FX Pairs | 未翻译 | 7 |
| [09_dl_tcn.ipynb](../../case_studies/fx_pairs/09_dl_tcn.ipynb) | Temporal Convolutional Network - FX Pairs | 未翻译 | 6 |
| [10_dl_nlinear.ipynb](../../case_studies/fx_pairs/10_dl_nlinear.ipynb) | NLinear - FX Pairs | 未翻译 | 6 |
| [10a_dl_lstm.ipynb](../../case_studies/fx_pairs/10a_dl_lstm.ipynb) | LSTM - FX Pairs | 未翻译 | 6 |
| [11_causal_dml.ipynb](../../case_studies/fx_pairs/11_causal_dml.ipynb) | Causal DML - FX Momentum | 未翻译 | 6 |
| [12_model_analysis.ipynb](../../case_studies/fx_pairs/12_model_analysis.ipynb) | Model Analysis - FX Pairs | 未翻译 | 11 |
| [13_backtest.ipynb](../../case_studies/fx_pairs/13_backtest.ipynb) | Equal-Weight Backtest - FX Pairs | 未翻译 | 6 |
| [14_portfolio_management.ipynb](../../case_studies/fx_pairs/14_portfolio_management.ipynb) | Portfolio Allocation - FX Pairs | 未翻译 | 6 |
| [15_risk_management.ipynb](../../case_studies/fx_pairs/15_risk_management.ipynb) | Position Risk Controls - FX Pairs | 未翻译 | 6 |
| [16_costs.ipynb](../../case_studies/fx_pairs/16_costs.ipynb) | Transaction-Cost Sensitivity - FX Pairs | 未翻译 | 5 |
| [17_holdout_predictions.ipynb](../../case_studies/fx_pairs/17_holdout_predictions.ipynb) | Holdout Predictions - FX Pairs | 未翻译 | 5 |
| [18_holdout_backtest.ipynb](../../case_studies/fx_pairs/18_holdout_backtest.ipynb) | Holdout Backtest - FX Pairs | 未翻译 | 5 |
| [19_strategy_analysis.ipynb](../../case_studies/fx_pairs/19_strategy_analysis.ipynb) | Strategy Analysis - FX Pairs | 未翻译 | 12 |

章节说明见 [`case_studies/fx_pairs/README.md`](../../case_studies/fx_pairs/README.md)。

## 案例研究：NASDAQ-100 微观结构

共 20 个 notebook，361 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/nasdaq100_microstructure/01_feasibility_analysis.ipynb) | NASDAQ-100 Microstructure: Feasibility Analysis | 未翻译 | 18 |
| [02_labels.ipynb](../../case_studies/nasdaq100_microstructure/02_labels.ipynb) | NASDAQ-100 Microstructure: Label Engineering | 未翻译 | 22 |
| [03_financial_features.ipynb](../../case_studies/nasdaq100_microstructure/03_financial_features.ipynb) | NASDAQ-100 Microstructure: Feature Engineering | 未翻译 | 32 |
| [04_model_based_features.ipynb](../../case_studies/nasdaq100_microstructure/04_model_based_features.ipynb) | NASDAQ-100 microstructure: features a model has to be fitted to produce | 未翻译 | 38 |
| [05_evaluation.ipynb](../../case_studies/nasdaq100_microstructure/05_evaluation.ipynb) | Feature Evaluation: NASDAQ-100 Microstructure | 未翻译 | 34 |
| [06_linear.ipynb](../../case_studies/nasdaq100_microstructure/06_linear.ipynb) | NASDAQ-100 microstructure: what a linear map of order flow is worth | 未翻译 | 12 |
| [07_gbm.ipynb](../../case_studies/nasdaq100_microstructure/07_gbm.ipynb) | NASDAQ-100 microstructure: what trees find in order flow that a linear map cannot | 未翻译 | 14 |
| [08_dl_nlinear.ipynb](../../case_studies/nasdaq100_microstructure/08_dl_nlinear.ipynb) | NLinear - NASDAQ-100 Microstructure | 未翻译 | 9 |
| [09_dl_lstm.ipynb](../../case_studies/nasdaq100_microstructure/09_dl_lstm.ipynb) | LSTM - NASDAQ-100 Microstructure | 未翻译 | 9 |
| [10_dl_tcn.ipynb](../../case_studies/nasdaq100_microstructure/10_dl_tcn.ipynb) | Temporal convolutional network - NASDAQ-100 Microstructure | 未翻译 | 9 |
| [11_dl_patchtst.ipynb](../../case_studies/nasdaq100_microstructure/11_dl_patchtst.ipynb) | PatchTST - NASDAQ-100 Microstructure | 未翻译 | 9 |
| [12_causal_dml.ipynb](../../case_studies/nasdaq100_microstructure/12_causal_dml.ipynb) | NASDAQ-100 Microstructure - Order Flow: Causal DML Estimation | 未翻译 | 9 |
| [13_model_analysis.ipynb](../../case_studies/nasdaq100_microstructure/13_model_analysis.ipynb) | Model Analysis: NASDAQ-100 Microstructure | 未翻译 | 46 |
| [14_backtest.ipynb](../../case_studies/nasdaq100_microstructure/14_backtest.ipynb) | NASDAQ-100 Microstructure: Backtest & Signal Evaluation | 未翻译 | 20 |
| [15_portfolio_management.ipynb](../../case_studies/nasdaq100_microstructure/15_portfolio_management.ipynb) | NASDAQ-100 Microstructure: Portfolio: Allocator Sweep | 未翻译 | 9 |
| [16_risk_management.ipynb](../../case_studies/nasdaq100_microstructure/16_risk_management.ipynb) | NASDAQ-100 Microstructure: Risk Controls | 未翻译 | 8 |
| [17_costs.ipynb](../../case_studies/nasdaq100_microstructure/17_costs.ipynb) | NASDAQ-100 Microstructure: Costs | 未翻译 | 15 |
| [18_holdout_predictions.ipynb](../../case_studies/nasdaq100_microstructure/18_holdout_predictions.ipynb) | NASDAQ-100 Microstructure: Holdout Predictions | 未翻译 | 8 |
| [19_holdout_backtest.ipynb](../../case_studies/nasdaq100_microstructure/19_holdout_backtest.ipynb) | NASDAQ-100 Microstructure: Holdout Backtest | 未翻译 | 6 |
| [20_strategy_analysis.ipynb](../../case_studies/nasdaq100_microstructure/20_strategy_analysis.ipynb) | NASDAQ-100 Microstructure — Strategy Analysis | 未翻译 | 34 |

章节说明见 [`case_studies/nasdaq100_microstructure/README.md`](../../case_studies/nasdaq100_microstructure/README.md)。

## 案例研究：S&P 500 股票与期权分析

共 25 个 notebook，420 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/sp500_equity_option_analytics/01_feasibility_analysis.ipynb) | S&P 500 Equity + Option Analytics: Feasibility Analysis | 未翻译 | 19 |
| [02_labels.ipynb](../../case_studies/sp500_equity_option_analytics/02_labels.ipynb) | S&P 500 Equity + Option Analytics: Label Engineering | 未翻译 | 25 |
| [03_financial_features.ipynb](../../case_studies/sp500_equity_option_analytics/03_financial_features.ipynb) | S&P 500 Equity + Option Analytics: Feature Engineering | 未翻译 | 27 |
| [04_model_based_features.ipynb](../../case_studies/sp500_equity_option_analytics/04_model_based_features.ipynb) | S&P 500 Equity + Option Analytics: Model-Based Features | 未翻译 | 27 |
| [05_evaluation.ipynb](../../case_studies/sp500_equity_option_analytics/05_evaluation.ipynb) | S&P 500 Equity Option Analytics: Feature Evaluation | 未翻译 | 22 |
| [06_linear.ipynb](../../case_studies/sp500_equity_option_analytics/06_linear.ipynb) | Option analytics: can what the options market prices rank the stock | 未翻译 | 12 |
| [07_gbm.ipynb](../../case_studies/sp500_equity_option_analytics/07_gbm.ipynb) | Option analytics: conditioning one forecast on another | 未翻译 | 13 |
| [08_tabular_dl.ipynb](../../case_studies/sp500_equity_option_analytics/08_tabular_dl.ipynb) | Option analytics: an ensemble that fits in one network | 未翻译 | 13 |
| [09_dl_lstm.ipynb](../../case_studies/sp500_equity_option_analytics/09_dl_lstm.ipynb) | S&P 500 Equity+Options: Sequence Models | 未翻译 | 12 |
| [10_dl_patchtst.ipynb](../../case_studies/sp500_equity_option_analytics/10_dl_patchtst.ipynb) | S&P 500 Equity+Options: Patched Attention | 未翻译 | 8 |
| [11_latent_factors.ipynb](../../case_studies/sp500_equity_option_analytics/11_latent_factors.ipynb) | Option analytics: five ways to say the cross-section moves together | 未翻译 | 6 |
| [11a_pca.ipynb](../../case_studies/sp500_equity_option_analytics/11a_pca.ipynb) | Option analytics: the factors the returns have, before anything is conditioned on | 未翻译 | 13 |
| [11b_ipca.ipynb](../../case_studies/sp500_equity_option_analytics/11b_ipca.ipynb) | Option analytics: letting the option surface choose the exposures | 未翻译 | 13 |
| [11c_conditional_autoencoder.ipynb](../../case_studies/sp500_equity_option_analytics/11c_conditional_autoencoder.ipynb) | Option analytics: letting a network decide what the exposures depend on | 未翻译 | 13 |
| [11d_stochastic_discount_factor.ipynb](../../case_studies/sp500_equity_option_analytics/11d_stochastic_discount_factor.ipynb) | Option analytics: pricing the cross-section instead of describing it | 未翻译 | 12 |
| [11e_supervised_autoencoder.ipynb](../../case_studies/sp500_equity_option_analytics/11e_supervised_autoencoder.ipynb) | Option analytics: the factor model that is allowed to see the target | 未翻译 | 13 |
| [12_causal_dml.ipynb](../../case_studies/sp500_equity_option_analytics/12_causal_dml.ipynb) | S&P 500 Equity+Option - IV-RV Spread: Causal DML Sensitivity Analysis | 未翻译 | 10 |
| [13_model_analysis.ipynb](../../case_studies/sp500_equity_option_analytics/13_model_analysis.ipynb) | Model Analysis: S&P 500 Equity + Option Analytics | 未翻译 | 59 |
| [14_backtest.ipynb](../../case_studies/sp500_equity_option_analytics/14_backtest.ipynb) | S&P 500 Equity+Options: Backtest and Signal Evaluation | 未翻译 | 18 |
| [15_portfolio_management.ipynb](../../case_studies/sp500_equity_option_analytics/15_portfolio_management.ipynb) | S&P 500 Equity+Options: Portfolio Allocation | 未翻译 | 15 |
| [16_risk_management.ipynb](../../case_studies/sp500_equity_option_analytics/16_risk_management.ipynb) | S&P 500 Equity+Options: Risk Controls | 未翻译 | 17 |
| [17_costs.ipynb](../../case_studies/sp500_equity_option_analytics/17_costs.ipynb) | S&P 500 Equity+Options: Transaction Costs | 未翻译 | 12 |
| [18_holdout_predictions.ipynb](../../case_studies/sp500_equity_option_analytics/18_holdout_predictions.ipynb) | S&P 500 Equity+Options: Holdout Predictions | 未翻译 | 11 |
| [19_holdout_backtest.ipynb](../../case_studies/sp500_equity_option_analytics/19_holdout_backtest.ipynb) | S&P 500 Equity+Options: Holdout Backtest | 未翻译 | 10 |
| [20_strategy_analysis.ipynb](../../case_studies/sp500_equity_option_analytics/20_strategy_analysis.ipynb) | S&P 500 Equity+Options: Strategy Assessment | 未翻译 | 20 |

章节说明见 [`case_studies/sp500_equity_option_analytics/README.md`](../../case_studies/sp500_equity_option_analytics/README.md)。

## 案例研究：S&P 500 期权

共 21 个 notebook，329 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/sp500_options/01_feasibility_analysis.ipynb) | S&P 500 Options: Feasibility Analysis | 未翻译 | 19 |
| [02_labels.ipynb](../../case_studies/sp500_options/02_labels.ipynb) | S&P 500 Options: Label Engineering | 未翻译 | 26 |
| [03_financial_features.ipynb](../../case_studies/sp500_options/03_financial_features.ipynb) | S&P 500 Options: Feature Engineering | 未翻译 | 30 |
| [04_model_based_features.ipynb](../../case_studies/sp500_options/04_model_based_features.ipynb) | S&P 500 options: features that are model outputs | 未翻译 | 40 |
| [05_evaluation.ipynb](../../case_studies/sp500_options/05_evaluation.ipynb) | S&P 500 Options: Feature Evaluation | 未翻译 | 49 |
| [06_linear.ipynb](../../case_studies/sp500_options/06_linear.ipynb) | Short straddles: when the loss you minimize is not the metric you are judged on | 未翻译 | 14 |
| [07_gbm.ipynb](../../case_studies/sp500_options/07_gbm.ipynb) | Short straddles: three loss functions against one rank metric | 未翻译 | 14 |
| [08_tabular_dl.ipynb](../../case_studies/sp500_options/08_tabular_dl.ipynb) | S&P 500 Options: Tabular Deep Learning | 未翻译 | 9 |
| [09_deep_learning.ipynb](../../case_studies/sp500_options/09_deep_learning.ipynb) | S&P 500 Options: NLinear | 未翻译 | 5 |
| [09a_lstm.ipynb](../../case_studies/sp500_options/09a_lstm.ipynb) | S&P 500 Options: LSTM | 未翻译 | 5 |
| [09b_patchtst.ipynb](../../case_studies/sp500_options/09b_patchtst.ipynb) | S&P 500 Options: PatchTST | 未翻译 | 5 |
| [10_causal_dml.ipynb](../../case_studies/sp500_options/10_causal_dml.ipynb) | S&P 500 Options: Causal DML Execution | 未翻译 | 4 |
| [11_model_analysis.ipynb](../../case_studies/sp500_options/11_model_analysis.ipynb) | S&P 500 Options: Model Analysis | 未翻译 | 6 |
| [12_backtest.ipynb](../../case_studies/sp500_options/12_backtest.ipynb) | S&P 500 Options: Equal-Weight Baseline Backtests | 未翻译 | 10 |
| [13_portfolio_management.ipynb](../../case_studies/sp500_options/13_portfolio_management.ipynb) | S&P 500 Options: Portfolio Construction | 未翻译 | 8 |
| [14_risk_management.ipynb](../../case_studies/sp500_options/14_risk_management.ipynb) | S&P 500 Options: The Risk-Overlay Boundary | 未翻译 | 6 |
| [15_costs.ipynb](../../case_studies/sp500_options/15_costs.ipynb) | S&P 500 Options: Cost Sensitivity | 未翻译 | 7 |
| [16_holdout_predictions.ipynb](../../case_studies/sp500_options/16_holdout_predictions.ipynb) | S&P 500 Options: Holdout Predictions | 未翻译 | 8 |
| [17_holdout_backtest.ipynb](../../case_studies/sp500_options/17_holdout_backtest.ipynb) | S&P 500 Options: Holdout Backtest | 未翻译 | 7 |
| [18_strategy_analysis.ipynb](../../case_studies/sp500_options/18_strategy_analysis.ipynb) | S&P 500 Options - Strategy Analysis | 未翻译 | 48 |
| [90_ic_diagnostic.ipynb](../../case_studies/sp500_options/90_ic_diagnostic.ipynb) | S&P 500 Options: IC Mechanism Diagnostic | 未翻译 | 9 |

章节说明见 [`case_studies/sp500_options/README.md`](../../case_studies/sp500_options/README.md)。

## 案例研究：美国股票面板

共 24 个 notebook，361 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/us_equities_panel/01_feasibility_analysis.ipynb) | US Equities Panel: Feasibility Analysis | 未翻译 | 21 |
| [02_labels.ipynb](../../case_studies/us_equities_panel/02_labels.ipynb) | US Equities Panel: Label Engineering | 未翻译 | 23 |
| [03_financial_features.ipynb](../../case_studies/us_equities_panel/03_financial_features.ipynb) | US Equities Panel: Feature Engineering | 未翻译 | 31 |
| [04_model_based_features.ipynb](../../case_studies/us_equities_panel/04_model_based_features.ipynb) | US Equities Panel: Model-Based Features | 未翻译 | 34 |
| [05_evaluation.ipynb](../../case_studies/us_equities_panel/05_evaluation.ipynb) | US Equities Panel: Feature Evaluation | 未翻译 | 31 |
| [06_linear.ipynb](../../case_studies/us_equities_panel/06_linear.ipynb) | US equities panel: what a penalized linear map of the cross-section is worth | 未翻译 | 13 |
| [07_gbm.ipynb](../../case_studies/us_equities_panel/07_gbm.ipynb) | US equities panel: capacity, loss function, and when to stop adding trees | 未翻译 | 14 |
| [08_tabular_dl.ipynb](../../case_studies/us_equities_panel/08_tabular_dl.ipynb) | US equities panel: a neural network on the same flat table, and what an ensemble of them costs | 未翻译 | 14 |
| [09_dl_nlinear.ipynb](../../case_studies/us_equities_panel/09_dl_nlinear.ipynb) | US equities panel: the simplest thing that reads a window | 未翻译 | 14 |
| [10_dl_lstm.ipynb](../../case_studies/us_equities_panel/10_dl_lstm.ipynb) | US equities panel: a model that carries state across the window | 未翻译 | 14 |
| [11_dl_tsmixer.ipynb](../../case_studies/us_equities_panel/11_dl_tsmixer.ipynb) | US equities panel: mixing along time and across features instead of recurring | 未翻译 | 14 |
| [12_dl_weekly.ipynb](../../case_studies/us_equities_panel/12_dl_weekly.ipynb) | US equities panel: predicting a week ahead instead of five days ahead | 未翻译 | 10 |
| [13_latent_factors.ipynb](../../case_studies/us_equities_panel/13_latent_factors.ipynb) | US equities panel: finding the few things three thousand stocks have in common | 未翻译 | 4 |
| [13a_pca.ipynb](../../case_studies/us_equities_panel/13a_pca.ipynb) | US equities panel: the few movements the whole panel shares | 未翻译 | 13 |
| [13b_ipca.ipynb](../../case_studies/us_equities_panel/13b_ipca.ipynb) | US equities panel: loadings that depend on what a stock is | 未翻译 | 13 |
| [14_causal_dml.ipynb](../../case_studies/us_equities_panel/14_causal_dml.ipynb) | US equities panel: a different question - does momentum cause the return, or predict it? | 未翻译 | 8 |
| [15_model_analysis.ipynb](../../case_studies/us_equities_panel/15_model_analysis.ipynb) | US equities panel: what the fitted models are worth before any of them is traded | 未翻译 | 11 |
| [16_backtest.ipynb](../../case_studies/us_equities_panel/16_backtest.ipynb) | US equities panel: from a ranking to a book, at equal weight | 未翻译 | 10 |
| [17_portfolio_management.ipynb](../../case_studies/us_equities_panel/17_portfolio_management.ipynb) | US equities panel: the same names, sized differently | 未翻译 | 12 |
| [18_risk_management.ipynb](../../case_studies/us_equities_panel/18_risk_management.ipynb) | US equities panel: rules that close a position early | 未翻译 | 11 |
| [19_costs.ipynb](../../case_studies/us_equities_panel/19_costs.ipynb) | US equities panel: how much friction the strategy can absorb | 未翻译 | 9 |
| [20_holdout_predictions.ipynb](../../case_studies/us_equities_panel/20_holdout_predictions.ipynb) | US equities panel: refitting the selected configuration for the holdout | 未翻译 | 8 |
| [21_holdout_backtest.ipynb](../../case_studies/us_equities_panel/21_holdout_backtest.ipynb) | US equities panel: trading the holdout predictions | 未翻译 | 6 |
| [22_strategy_analysis.ipynb](../../case_studies/us_equities_panel/22_strategy_analysis.ipynb) | US equities panel: what the one holdout was spent on, and what it bought | 未翻译 | 23 |

章节说明见 [`case_studies/us_equities_panel/README.md`](../../case_studies/us_equities_panel/README.md)。

## 案例研究：美国公司特征

共 21 个 notebook，352 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [01_feasibility_analysis.ipynb](../../case_studies/us_firm_characteristics/01_feasibility_analysis.ipynb) | US Firm Characteristics: Feasibility Analysis | 未翻译 | 18 |
| [02_labels.ipynb](../../case_studies/us_firm_characteristics/02_labels.ipynb) | US Firm Characteristics: Label Engineering | 未翻译 | 22 |
| [03_financial_features.ipynb](../../case_studies/us_firm_characteristics/03_financial_features.ipynb) | US Firm Characteristics: Feature Engineering | 未翻译 | 23 |
| [04_evaluation.ipynb](../../case_studies/us_firm_characteristics/04_evaluation.ipynb) | US Firm Characteristics: Feature Evaluation | 未翻译 | 27 |
| [05_linear.ipynb](../../case_studies/us_firm_characteristics/05_linear.ipynb) | Firm characteristics: strong features, and a target that decides the fit | 未翻译 | 13 |
| [06_gbm.ipynb](../../case_studies/us_firm_characteristics/06_gbm.ipynb) | Firm characteristics: changing the objective without changing the target | 未翻译 | 14 |
| [07_tabular_dl.ipynb](../../case_studies/us_firm_characteristics/07_tabular_dl.ipynb) | Firm characteristics: a neural network under the objective that already failed | 未翻译 | 16 |
| [08_latent_factors.ipynb](../../case_studies/us_firm_characteristics/08_latent_factors.ipynb) | Firm characteristics: what the latent-factor family is, and who publishes what | 未翻译 | 6 |
| [08a_ipca.ipynb](../../case_studies/us_firm_characteristics/08a_ipca.ipynb) | Firm characteristics: letting the characteristics choose the factors | 未翻译 | 14 |
| [08b_conditional_autoencoder.ipynb](../../case_studies/us_firm_characteristics/08b_conditional_autoencoder.ipynb) | Firm characteristics: the same factor structure with a nonlinear map | 未翻译 | 14 |
| [08c_stochastic_discount_factor.ipynb](../../case_studies/us_firm_characteristics/08c_stochastic_discount_factor.ipynb) | Firm characteristics: pricing the cross-section instead of forecasting it | 未翻译 | 14 |
| [08d_supervised_autoencoder.ipynb](../../case_studies/us_firm_characteristics/08d_supervised_autoencoder.ipynb) | Firm characteristics: dropping the factor structure and keeping the bottleneck | 未翻译 | 14 |
| [09_causal_dml.ipynb](../../case_studies/us_firm_characteristics/09_causal_dml.ipynb) | Causal DML for US Firm Characteristics | 未翻译 | 9 |
| [10_model_analysis.ipynb](../../case_studies/us_firm_characteristics/10_model_analysis.ipynb) | Model Analysis: US Firm Characteristics | 未翻译 | 44 |
| [11_backtest.ipynb](../../case_studies/us_firm_characteristics/11_backtest.ipynb) | US Firm Characteristics: Backtest and Equal-Weight Baseline | 未翻译 | 10 |
| [12_portfolio_management.ipynb](../../case_studies/us_firm_characteristics/12_portfolio_management.ipynb) | US Firm Characteristics: Allocator Sweep | 未翻译 | 11 |
| [13_risk_management.ipynb](../../case_studies/us_firm_characteristics/13_risk_management.ipynb) | US Firm Characteristics: Risk Overlay Applicability | 未翻译 | 10 |
| [14_costs.ipynb](../../case_studies/us_firm_characteristics/14_costs.ipynb) | US Firm Characteristics: Cost Sensitivity | 未翻译 | 9 |
| [15_holdout_predictions.ipynb](../../case_studies/us_firm_characteristics/15_holdout_predictions.ipynb) | US Firm Characteristics: Holdout Predictions | 未翻译 | 8 |
| [16_holdout_backtest.ipynb](../../case_studies/us_firm_characteristics/16_holdout_backtest.ipynb) | US Firm Characteristics: Holdout Backtest | 未翻译 | 6 |
| [17_strategy_analysis.ipynb](../../case_studies/us_firm_characteristics/17_strategy_analysis.ipynb) | US Firm Characteristics - Strategy Analysis | 未翻译 | 50 |

章节说明见 [`case_studies/us_firm_characteristics/README.md`](../../case_studies/us_firm_characteristics/README.md)。

## 数据集说明 notebook

共 9 个 notebook，130 个 Markdown 说明 cell。

| Notebook | 原标题 | 中文版 | 说明 cell |
|---|---|---|---: |
| [crypto/market/dataset_card.ipynb](../../data/crypto/market/dataset_card.ipynb) | Crypto Premium Index Dataset | 未翻译 | 15 |
| [equities/firm_characteristics/dataset_card.ipynb](../../data/equities/firm_characteristics/dataset_card.ipynb) | Firm Characteristics Dataset | 未翻译 | 12 |
| [equities/market/microstructure/dataset_card.ipynb](../../data/equities/market/microstructure/dataset_card.ipynb) | Tick Data Dataset | 未翻译 | 17 |
| [equities/market/us_equities/dataset_card.ipynb](../../data/equities/market/us_equities/dataset_card.ipynb) | US Equities Dataset | 未翻译 | 14 |
| [etfs/market/dataset_card.ipynb](../../data/etfs/market/dataset_card.ipynb) | ETF Universe Dataset | 未翻译 | 14 |
| [factors/dataset_card.ipynb](../../data/factors/dataset_card.ipynb) | Academic Factor Data Dataset | 未翻译 | 15 |
| [futures/market/dataset_card.ipynb](../../data/futures/market/dataset_card.ipynb) | CME Futures Dataset | 未翻译 | 14 |
| [fx/market/dataset_card.ipynb](../../data/fx/market/dataset_card.ipynb) | FX Pairs Dataset | 未翻译 | 15 |
| [macro/dataset_card.ipynb](../../data/macro/dataset_card.ipynb) | FRED Macro Indicators Dataset | 未翻译 | 14 |

数据源、授权和下载细节见 [`data/README.md`](../../data/README.md)。

---

## 翻译约定

- 代码、库名、函数名、参数名、文件路径和环境变量不翻译。
- `walk-forward validation` 译为“walk-forward 验证”，保留英文原词以便检索。
- `regime` 视上下文译为“市场状态 / regime”。
- `leakage` 译为“数据泄漏”，`lookahead bias` 译为“前视偏差”。
- 模型名、数据集名和机构名保留英文。

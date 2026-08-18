# Project FORESIGHT

## Retail Demand Forecasting & Inventory Risk Analysis using Machine Learning

---

## 1. Project Overview

Project FORESIGHT is an end-to-end Machine Learning and Data Analytics project designed to forecast retail product demand and analyze inventory risk.

The project uses historical sales, product, calendar, and inventory data to:

* Forecast product demand
* Analyze sales and revenue performance
* Evaluate product and category performance
* Identify inventory risk
* Generate business insights
* Generate business recommendations
* Support inventory planning
* Support replenishment decisions
* Provide interactive analytics through a Streamlit dashboard

The complete solution covers Data Engineering, Exploratory Data Analysis, Feature Engineering, Machine Learning, Model Evaluation, Inventory Risk Scoring, Business Analytics, Dashboard Development, Final Validation, and Documentation.

---

## 2. Problem Statement

Retail businesses often face challenges in maintaining appropriate inventory levels because customer demand changes over time.

Poor demand forecasting can lead to:

* Overstocking
* Understocking
* Stockout risk
* Excess inventory
* Increased operational costs
* Lost sales
* Poor inventory planning

Project FORESIGHT addresses these challenges by using historical retail data and Machine Learning to forecast demand and identify inventory-related risk.

---

## 3. Project Objectives

The main objectives of Project FORESIGHT are:

* Forecast retail product demand
* Analyze historical sales trends
* Analyze revenue performance
* Identify high-performing products and categories
* Identify inventory risk
* Improve inventory planning
* Support replenishment decisions
* Generate business insights
* Generate business recommendations
* Build an interactive dashboard
* Support data-driven business decisions

---

## 4. Project Features

The project includes:

* Data Understanding
* Data Collection
* Data Cleaning
* Data Engineering
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Baseline Forecasting
* Machine Learning Forecasting
* Model Evaluation
* Inventory Risk Scoring
* Final Data Validation
* Final ML Model Validation
* End-to-End Project Testing
* Final Business Insights
* Final Business Recommendations
* Streamlit Dashboard
* Deployment Preparation
* Project Documentation

---

## 5. Dataset Information

The project uses retail datasets containing sales, product, calendar, and inventory information.

### Source Datasets

* `sales_daily.csv`
* `inventory_snapshots.csv`
* `sku_master.csv`
* `calender.csv`

> Note: The project uses the existing `calender.csv` filename in the dataset structure.

### Processed Datasets

* `master_dataset.csv`
* `cleaned_master_dataset.csv`
* `feature_engineered_dataset.csv`
* `feature_engineered_dataset_final.csv`

---

## 6. Dataset Summary

The final feature-engineered dataset contains:

* **73,000 records**
* **200 unique SKUs**
* **365 days of data per SKU**
* Analysis period: **2024**
* **24 columns**

Date range:

```text
2024-01-01 to 2024-12-30
```

---

## 7. Project Structure

```text
FORESIGHT/
│
├── data/
│   ├── raw/
│   │   ├── calender.csv
│   │   ├── inventory_snapshots.csv
│   │   ├── sales_daily.csv
│   │   └── sku_master.csv
│   │
│   └── processed/
│       ├── master_dataset.csv
│       ├── cleaned_master_dataset.csv
│       ├── feature_engineered_dataset.csv
│       └── feature_engineered_dataset_final.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_data_engineering.ipynb
│   ├── 04_eda.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_baseline_forecasting.ipynb
│   ├── 07_model_evaluation.ipynb
│   ├── 08_risk_scoring.ipynb
│   ├── 09_final_data_validation.ipynb
│   ├── 10_final_ml_model_validation.ipynb
│   ├── 11_end_to_end_project_testing.ipynb
│   ├── 12_final_business_insights.ipynb
│   └── 13_final_business_recommendations.ipynb
│
├── models/
│   ├── baseline_random_forest.pkl
│   └── final_random_forest.pkl
│
├── reports/
│   ├── baseline_predictions.csv
│   ├── model_evaluation_metrics.csv
│   ├── final_model_validation_metrics.csv
│   ├── risk_scoring.csv
│   └── Final_Project_Report.docx
│
├── dashboard/
│   └── app.py
│
├── README.md
└── requirements.txt
```

---

## 8. Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn
* Random Forest Regressor

### Model Evaluation

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Dashboard Development

* Streamlit
* Plotly

### Development Environment

* Jupyter Notebook
* Visual Studio Code
* Python Virtual Environment

### Deployment and Version Control

* Streamlit
* Docker
* Git
* GitHub

---

## 9. Machine Learning Workflow

The Machine Learning workflow consists of:

1. Data Preparation
2. Feature Engineering
3. Train-Test Split
4. Baseline Random Forest Model
5. Model Evaluation
6. Final Random Forest Model
7. Final Model Validation
8. Demand Prediction
9. Inventory Risk Scoring
10. Business Insights
11. Business Recommendations
12. Dashboard Integration

---

## 10. Final Model

The final forecasting model is a:

**Random Forest Regressor**

Saved model:

```text
models/final_random_forest.pkl
```

Model configuration:

* Number of estimators: **50**
* Maximum depth: **15**
* Minimum samples per leaf: **2**
* Random state: **42**
* Parallel processing: enabled

---

## 11. Model Features

The final Random Forest model uses 15 input features:

* `unit_price`
* `promo_flag`
* `unit_cost`
* `list_price`
* `week`
* `month`
* `is_holiday`
* `day`
* `day_of_week`
* `quarter`
* `year`
* `on_hand_units`
* `on_order_units`
* `lead_time_days`
* `reorder_point`

---

## 12. Final Model Validation

The final model was validated using a time-based train-test split.

### Training Data

* Training rows: **58,400**
* Training period: **2024-01-01 to 2024-10-18**

### Testing Data

* Testing rows: **14,600**
* Testing period: **2024-10-19 to 2024-12-30**

### Final Test Metrics

| Metric |  Value |
| ------ | -----: |
| MAE    | 3.2449 |
| RMSE   | 4.0551 |
| R²     | 0.0946 |

The final model was saved successfully as:

```text
models/final_random_forest.pkl
```

Validation metrics were saved as:

```text
reports/final_model_validation_metrics.csv
```

---

## 13. Inventory Risk Scoring

The project calculates inventory risk using:

* Predicted demand
* Available inventory
* Inventory gap
* Inventory coverage
* Risk score
* Risk level

Risk levels:

* High
* Medium
* Low

Final risk scoring output:

* **73,000 records**
* **29 columns**

Saved output:

```text
reports/risk_scoring.csv
```

---

## 14. Final Business Insights

The final business analysis identified substantial inventory risk across the evaluated retail dataset.

### Risk Distribution

* High Risk: **63,400 records (86.85%)**
* Medium Risk: **51 records (0.07%)**
* Low Risk: **9,549 records (13.08%)**

### Category Analysis

The four analyzed categories are:

* Appliances
* Decor
* Furniture
* Kitchen

All four categories show substantial high-risk exposure and should be monitored through category-level inventory and demand analysis.

### Inventory Risk

High-priority records show:

* Zero on-hand inventory
* Zero inventory coverage
* Negative inventory gap relative to predicted demand
* Risk scores reaching **100**

These records require immediate inventory and replenishment attention.

---

## 15. Final Business Recommendations

Based on the final business analysis:

1. Immediately prioritize high-risk SKUs with zero on-hand inventory.
2. Review reorder points for frequently high-risk products.
3. Review pending purchase orders and on-order quantities.
4. Use predicted demand to support replenishment planning.
5. Monitor inventory coverage continuously.
6. Give additional attention to high-risk categories.
7. Prepare inventory before promotional and high-risk periods.
8. Integrate demand forecasts and risk scores into operational dashboards.
9. Review high-risk inventory regularly.
10. Adjust replenishment plans according to predicted demand and inventory conditions.

---

## 16. Dashboard

The project includes an interactive Streamlit dashboard.

Dashboard file:

```text
dashboard/app.py
```

Dashboard data source:

```text
reports/risk_scoring.csv
```

The dashboard provides:

* Dataset preview
* Actual demand
* Predicted demand
* Inventory gap
* Inventory coverage
* Risk score
* Risk level
* Inventory risk analysis

The dashboard runtime was successfully tested using Streamlit.

---

## 17. Project Validation

The project was validated through multiple final validation stages.

### Final Data Validation

* Final dataset exists
* Required columns validated
* Missing values checked
* Duplicate records checked
* Final dataset validated successfully

### Final ML Model Validation

* Final model exists
* Final model loads successfully
* Model features validated
* Predictions generated successfully
* Prediction completeness validated
* Final validation metrics saved

### End-to-End Project Testing

The complete project pipeline was tested.

Validation confirmed:

* Final dataset available
* Final dataset has no missing values
* Final dataset has no duplicate rows
* Final model predictions complete
* Risk predictions complete
* Risk scores complete
* Risk levels complete
* Risk score values valid
* Required risk columns available
* Final model and risk scoring outputs are connected
* Required project files are present and non-empty
* Dashboard runtime starts successfully

Final core pipeline result:

```text
PASS: END-TO-END PROJECT TESTING SUCCESSFUL.
The core project pipeline is working correctly.
```

---

## 18. Final Project Outputs

Major project outputs include:

```text
models/final_random_forest.pkl
reports/final_model_validation_metrics.csv
reports/risk_scoring.csv
reports/baseline_predictions.csv
reports/model_evaluation_metrics.csv
reports/Final_Project_Report.docx
dashboard/app.py
README.md
requirements.txt
```

---

## 19. Installation

Create and activate the project virtual environment, then install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 20. Running the Dashboard

From the project root:

```bash
streamlit run dashboard/app.py
```

The dashboard can then be opened in a web browser using the Streamlit URL displayed in the terminal.

---

## 21. Conclusion

Project FORESIGHT provides an end-to-end retail demand forecasting and inventory risk analysis solution.

The project combines:

* Historical retail data
* Data Engineering
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning
* Demand Forecasting
* Inventory Risk Scoring
* Business Insights
* Business Recommendations
* Interactive Dashboard
* Final Validation

The solution can support:

* Inventory planning
* Demand analysis
* Replenishment planning
* Risk monitoring
* Stockout-risk identification
* Data-driven business decision-making

---

## 22. Project Status

**Core Project Pipeline: COMPLETED**

Completed components:

* Data Pipeline
* EDA
* Feature Engineering
* Baseline Forecasting
* Model Evaluation
* Final ML Model
* Risk Scoring
* Final Data Validation
* Final ML Model Validation
* End-to-End Testing
* Business Insights
* Business Recommendations
* Dashboard Runtime Validation
* README
* Requirements

Remaining project-finalization activities are limited to:

* Final Project Report finalization
* Final Project Folder Cleanup
* GitHub Final Check and Push
* Final Project Presentation
* Final Deployment Verification
* Project Handover Documentation

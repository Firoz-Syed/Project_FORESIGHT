# Project FORESIGHT
## Retail Demand Forecasting & Inventory Risk Analysis using Machine Learning

# Project Overview

Project FORESIGHT is an end-to-end Machine Learning project that predicts retail product demand and analyzes inventory risk. The project helps retailers forecast future sales, identify high-risk inventory items, and improve inventory management using historical sales and inventory data.

The project combines Data Engineering, Data Analysis, Feature Engineering, Machine Learning, Risk Scoring, Streamlit Dashboard, and Power BI Dashboard into one complete solution.
---

# Problem Statement

Retail businesses often struggle with inventory management due to uncertain customer demand. Poor forecasting can result in overstocking, understocking, increased operational costs, and lost sales.

Project FORESIGHT solves this problem by forecasting future product demand and identifying inventory risk using Machine Learning.
---

# Project Objectives

- Forecast future product demand
- Analyze historical sales trends
- Reduce inventory risk
- Improve inventory planning
- Generate business insights
- Build an interactive dashboard
- Support data-driven business decisions
---

# Project Features

- Data Cleaning
- Data Engineering
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Forecasting
- Model Evaluation
- Inventory Risk Scoring
- Streamlit Dashboard
- Power BI Dashboard
- Business Reports
---

# Dataset Information

Datasets used in this project:

- sales_daily.csv
- inventory_snapshots.csv
- sku_master.csv
- calendar.csv

Processed datasets:

- master_dataset.csv
- cleaned_master_dataset.csv
- feature_engineered_dataset.csv
---

# Project Workflow

## Phase 1 – Data Understanding

- Load datasets
- Check dataset structure
- Identify data types
- Check missing values
- Understand business problem
---

## Phase 2 – Data Cleaning

- Remove duplicates
- Handle missing values
- Convert data types
- Clean inconsistent records
- Prepare clean dataset
---

## Phase 3 – Data Engineering

- Merge datasets
- Join sales data
- Join inventory data
- Join SKU information
- Join calendar data
- Create master dataset
---

## Phase 4 – Exploratory Data Analysis (EDA)

- Sales Analysis
- Revenue Analysis
- Monthly Trend
- Weekly Trend
- Category Analysis
- Promotion Analysis
- Holiday Analysis
- Inventory Analysis
- Correlation Analysis
- Outlier Detection
---

## Phase 5 – Feature Engineering

Created new features:

- Day
- Month
- Week
- Quarter
- Year
- Day of Week
- Holiday Flag
- Promotion Flag
- Inventory Features
- Pricing Features

Output:

feature_engineered_dataset.csv
---

## Phase 6 – Baseline Forecasting

Machine Learning Model:

Random Forest Regressor

Target Variable:

units_sold

Generated:

- Demand Prediction
- Forecast Results
- Trained Model

Outputs:

baseline_random_forest.pkl

baseline_predictions.csv
---

## Phase 7 – Model Evaluation

Evaluation Metrics:

- MAE
- RMSE
- R² Score
- MAPE

Generated:

model_evaluation_metrics.csv
---

## Phase 8 – Inventory Risk Scoring

Generated:

- Risk Score
- Risk Level

Risk Levels:

- Low
- Medium
- High

Output:

risk_scoring.csv
---

## Phase 9 – Streamlit Dashboard

Dashboard Features:

- Dataset Preview
- KPI Cards
- Forecast Results
- Risk Analysis
- Inventory Overview
- Business Insights
---

## Phase 10 – Power BI Dashboard

Interactive Dashboard includes:

- KPI Cards
- Sales Trend
- Revenue Trend
- Predicted Sales
- Risk Analysis
- Inventory Analysis
- Category Analysis
- Product Analysis
- Interactive Filters
---

## Phase 11 – Final Documentation

Project Documentation includes:

- README.md
- Reports
- Dashboard
- Model Files
- Source Code
- Project Structure
---

# Machine Learning Algorithm

Random Forest Regressor

Advantages:

- High Accuracy
- Handles Large Dataset
- Handles Nonlinear Relationships
- Fast Prediction
- Easy Feature Importance Analysis
---

# Technologies Used

Programming Language

- Python

Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

Visualization

- Streamlit
- Power BI

Development Tools

- Visual Studio Code
- Jupyter Notebook
---

# Project Folder Structure

```
Project_FORESIGHT/

│
├── app/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── images/
├── models/
├── notebooks/
├── reports/
├── src/
├── README.md
├── requirements.txt
└── venv/
```
---
# Generated Files

Processed Data

- cleaned_master_dataset.csv
- master_dataset.csv
- feature_engineered_dataset.csv

Models

- baseline_random_forest.pkl

Reports

- baseline_predictions.csv
- model_evaluation_metrics.csv
- risk_scoring.csv
---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd Project_FORESIGHT
```

Create virtual environment

```bash
python -m venv venv
```
Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
---

# How to Run the Project

## Step 1

Open VS Code
---

## Step 2

Activate virtual environment

```bash
venv\Scripts\activate
```
---

## Step 3

Open Jupyter Notebook

```bash
jupyter notebook
```

or

```bash
jupyter lab
```
---

## Step 4

Run notebooks in the following order:

1. 01_data_understanding.ipynb

2. 02_data_cleaning.ipynb

3. 03_data_engineering.ipynb

4. 04_eda.ipynb

5. 05_feature_engineering.ipynb

6. 06_baseline_forecasting.ipynb

7. 07_model_evaluation.ipynb

8. 08_risk_scoring.ipynb
---

## Step 5

Start Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Open browser:

```
http://localhost:8501
```
---

## Step 6

Open Power BI Desktop

Import

```
reports/risk_scoring.csv
```

Create dashboard using charts, KPI cards, slicers, and tables.
---

# Project Outputs

Generated Outputs:

- Forecasted Sales
- Inventory Risk Score
- Business Reports
- Trained Machine Learning Model
- Streamlit Dashboard
- Power BI Dashboard
---

# Business Benefits

- Better Demand Forecasting
- Improved Inventory Planning
- Reduced Overstock
- Reduced Understock
- Lower Operational Cost
- Better Supply Chain Decisions
- Faster Business Insights
- Improved Customer Satisfaction
---

# Future Enhancements

- XGBoost Forecasting
- LightGBM
- LSTM Forecasting
- Real-Time Prediction
- Database Integration
- Cloud Deployment
- API Development
- Automated Data Pipeline
- Email Alerts
- Inventory Recommendation System
---

# Conclusion

Project FORESIGHT demonstrates a complete end-to-end Machine Learning workflow for Retail Demand Forecasting and Inventory Risk Analysis. The project covers the complete data science lifecycle, including data understanding, preprocessing, feature engineering, machine learning, model evaluation, inventory risk analysis, interactive dashboards, and business reporting. The final solution enables retailers to forecast demand accurately, monitor inventory risk, and make informed business decisions through powerful visual analytics.
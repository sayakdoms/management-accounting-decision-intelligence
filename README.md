# Management Accounting Decision Intelligence Dashboard

A recruiter-friendly analytics project that converts a management accounting case into a structured Python-based decision-support dashboard.

## Live Project Idea

This repository demonstrates how management accounting tools can support strategic decisions around pricing, product mix, cost control, responsibility accounting, and budgetary agility.

## What This Project Does

- Converts case appendix exhibits into structured CSV datasets
- Performs variance diagnosis
- Models CVP and break-even sensitivity
- Compares Activity-Based Costing with traditional overhead allocation
- Builds a Streamlit dashboard for decision intelligence
- Provides GitHub Pages-ready project showcase files

## Core Modules

### 1. Variance Diagnosis Engine
Classifies cost and sales variances as favourable, unfavourable, or neutral, and recommends managerial action.

### 2. CVP Simulator
Allows users to change selling price, variable cost, quantity, and fixed cost to observe impact on profit, break-even units, and margin of safety.

### 3. ABC Costing Intelligence
Compares ABC overhead per unit with traditional overhead per unit to reveal costing distortion.

### 4. Strategic Decision Matrix
Ranks strategic alternatives based on accuracy gain, feasibility, strategic value, speed of insight, and overall recommendation strength.

## Repository Structure

```text
management-accounting-decision-intelligence/
│
├── README.md
├── index.html
├── requirements.txt
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── standard_vs_actual_cost.csv
│   ├── variance_summary.csv
│   ├── detailed_variances.csv
│   ├── cvp_scenarios.csv
│   ├── abc_cost_pools.csv
│   ├── abc_activity_usage.csv
│   ├── abc_vs_traditional.csv
│   └── decision_matrix.csv
│
├── src/
│   ├── abc_model.py
│   ├── cvp_model.py
│   ├── variance_engine.py
│   └── generate_charts.py
│
├── charts/
│   ├── variance_impact_summary.png
│   ├── cvp_profit_scenarios.png
│   ├── abc_costing_distortion.png
│   ├── abc_difference_by_sku.png
│   └── decision_matrix_score.png
│
└── reports/
    ├── sanitized_case_summary.md
    └── executive_insights.md
```

## How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app/streamlit_app.py
```

Regenerate charts:

```bash
python src/generate_charts.py
```

## Portfolio Positioning

This project should be positioned as:

> A Python-based management accounting decision-intelligence dashboard applying variance analysis, CVP modelling, and Activity-Based Costing to support pricing, cost-control, and strategic decision-making.

## Public-Safety Note

The original academic PDF is not included. This repository contains only sanitized and restructured analytical material for public portfolio use.

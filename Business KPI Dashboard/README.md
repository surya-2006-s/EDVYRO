# Customer Churn Business KPI Dashboard

## Overview

This project presents an interactive Business KPI Dashboard for a fictional subscription business.

The dashboard analyzes customer churn and helps identify customer groups that should receive retention attention.

The dashboard was developed using Python, Pandas, Streamlit, and Plotly.

## Business Question

Which customer groups should a fictional subscription team contact first to reduce avoidable churn?

## Dataset

The project uses a synthetic customer churn dataset containing:

- 15 customers
- Customer demographics
- Customer tenure
- Subscription type
- Monthly charges
- Total charges
- Contract type
- Support ticket count
- Payment method
- Churn status

## Key KPIs

The dashboard displays:

- Total Customers
- Churned Customers
- Overall Churn Rate
- Total Customer Value
- Average Customer Tenure
- Filtered Customer Count
- Filtered Churn Count
- Filtered Churn Rate
- Average Monthly Charge

## Dashboard Features

### Interactive Filters

Users can filter the dashboard by:

- Subscription Type
- Contract Type
- Gender

### Visualizations

The dashboard includes:

- Churn Rate by Contract Type
- Churn Rate by Subscription Type
- Churn Rate vs Support Tickets
- Churn Rate by Customer Tenure
- Customer Churn Distribution

### Priority Customer Segment

The dashboard highlights customers who:

- Have churned
- Have a Month-to-Month contract
- Have 3 or more support tickets

These customers are identified as a priority group for retention review.

## Key Findings

The sample shows:

- Overall churn rate: 46.67%
- Month-to-Month customers: 100% observed churn
- Basic subscription: 71.43% observed churn
- Customers with 3 or more support tickets: 100% observed churn
- Customers with shorter tenure show higher observed churn in this sample

## Business Recommendation

The fictional subscription team should prioritize customers with Month-to-Month contracts and higher support-ticket activity for retention review.

Newer customers should also receive additional attention because shorter-tenure groups show higher observed churn in this sample.

Possible retention actions include:

- Reviewing unresolved support issues
- Improving early-customer support
- Offering suitable retention incentives
- Reviewing contract options with customers

## Technology Stack

- Python
- Pandas
- Streamlit
- Plotly
- CSV
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
Business KPI Dashboard/
│
├── customer_churn_sample.csv
├── dashboard.py
└── README.md


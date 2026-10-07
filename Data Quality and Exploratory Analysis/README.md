# Customer Churn Data Quality and Exploratory Analysis

## Overview

This project performs data quality checks and exploratory analysis on a synthetic customer churn dataset.

The objective is to identify customer groups that may require attention to help reduce avoidable churn.

The analysis covers data quality validation, churn patterns across customer segments, and a final business recommendation based on the observed data.

## Dataset

The dataset contains 15 synthetic customer records and 11 columns.

### Main Fields

- CustomerID
- Gender
- Age
- TenureMonths
- SubscriptionType
- MonthlyCharges
- TotalCharges
- ContractType
- SupportTickets
- PaymentMethod
- Churn

## Data Quality Checks

The following quality checks were performed:

1. Missing value detection
2. Duplicate record detection
3. Numeric range inspection
4. Extreme-value detection using the IQR method
5. Categorical-value validation

### Data Quality Results

- Total records: 15
- Total columns: 11
- Missing values: 0
- Duplicate rows: 0
- Extreme values: 0
- Rows removed: 0

The dataset passed the performed quality checks, so no customer records were removed.

## Exploratory Analysis

The following churn patterns were analyzed:

- Overall churn rate
- Churn by contract type
- Churn by support tickets
- Churn by subscription type
- Churn by gender
- Churn by tenure
- Churn by monthly charges
- Churn by payment method

## Key Findings

### Overall Churn

- Total customers: 15
- Churned customers: 7
- Overall churn rate: 46.67%

### Contract Type

- Month-to-Month: 100% churn
- One Year: 0% churn
- Two Year: 0% churn

### Support Tickets

- 0–2 support tickets: 0% churn
- 3–6 support tickets: 100% churn

### Subscription Type

- Basic: 71.43% churn
- Pro: 50.00% churn
- Enterprise: 0.00% churn

### Gender

- Female: 50.00% churn
- Male: 42.86% churn

The difference between the two groups is relatively small in this sample.

### Tenure

- 0–6 months: 100% churn
- 7–12 months: 100% churn
- 13–24 months: 20% churn
- 25+ months: 0% churn

### Monthly Charges

- ₹0–60: 71.43% churn
- ₹61–100: 50.00% churn
- ₹101–130: No customers in the sample
- ₹131+: 0% churn

### Payment Method

- Bank Transfer: 0% churn
- Credit Card: 33.33% churn
- Debit Card: 100% churn
- UPI: 75% churn

The Debit Card result is based on only two customers, so it should be interpreted cautiously.

## Priority Customer Group

The analysis identified customers who:

- Have churned
- Have a Month-to-Month contract
- Have 3 or more support tickets

The identified customers are:

- CUST-1001
- CUST-1003
- CUST-1005
- CUST-1007
- CUST-1010
- CUST-1012
- CUST-1014

Total priority customers: 7

## Business Recommendation

The fictional subscription team should prioritize customers with Month-to-Month contracts and higher support-ticket activity, while giving special attention to newer customers.

Possible actions include reviewing unresolved support issues, improving early-customer support, and considering retention offers or contract options for customers showing multiple risk indicators.

## Limitations

This analysis uses a small synthetic dataset containing only 15 customers.

Therefore, the observed percentages should be treated as descriptive findings from this sample rather than general predictions about a larger customer population.

The analysis does not establish that any particular factor causes churn. Further analysis using a larger dataset would be required to validate these patterns.

## Methodology

The analysis was performed using Python and pandas.

Main steps:

1. Load the customer churn CSV dataset.
2. Inspect the dataset structure.
3. Check missing values.
4. Check duplicate records.
5. Inspect numeric ranges.
6. Detect extreme values using the IQR method.
7. Validate categorical values.
8. Calculate the overall churn rate.
9. Compare churn across customer segments.
10. Identify a priority customer group.
11. Develop a business recommendation.

## Technologies Used

- Python
- Pandas
- CSV
- Visual Studio Code
- Git
- GitHub

## Project Files

```text
Data Quality and Exploratory Analysis/
│
├── customer_churn_sample.csv
├── analysis.py
└── README.md

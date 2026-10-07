import pandas as pd

df = pd.read_csv("customer_churn_sample.csv")

print("CUSTOMER CHURN ANALYSIS SUMMARY")
print("===============================")

# Overall churn
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
overall_churn_rate = churned_customers / total_customers * 100

print(f"\nTotal customers: {total_customers}")
print(f"Churned customers: {churned_customers}")
print(f"Overall churn rate: {overall_churn_rate:.2f}%")

# Contract type
contract_churn_rate = df.groupby("ContractType")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by contract type:")
print(contract_churn_rate.round(2))

# Support tickets
support_churn_rate = df.groupby("SupportTickets")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by support tickets:")
print(support_churn_rate.round(2))

# Subscription type
subscription_churn_rate = df.groupby("SubscriptionType")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by subscription type:")
print(subscription_churn_rate.round(2))

# Tenure group
df["TenureGroup"] = pd.cut(
    df["TenureMonths"],
    bins=[0, 6, 12, 24, 100],
    labels=["0-6 months", "7-12 months", "13-24 months", "25+ months"]
)

tenure_churn_rate = df.groupby(
    "TenureGroup",
    observed=False
)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by tenure group:")
print(tenure_churn_rate.round(2))

# Priority customers
priority_customers = df[
    (df["Churn"] == "Yes") &
    (df["ContractType"] == "Month-to-Month") &
    (df["SupportTickets"] >= 3)
]

print("\nPriority churn customers:")
print(priority_customers["CustomerID"].tolist())

print(f"\nPriority customer count: {len(priority_customers)}")

print("\nRECOMMENDATION")
print("==============")
print(
    "Prioritize churn-risk customers with Month-to-Month contracts "
    "and 3 or more support tickets, while giving special attention "
    "to newer customers."
)
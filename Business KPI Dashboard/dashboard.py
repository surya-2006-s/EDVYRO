import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn KPI Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("customer_churn_sample.csv")

# -----------------------------
# KPI calculations
# -----------------------------
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
churn_rate = churned_customers / total_customers * 100

total_revenue = df["TotalCharges"].sum()
avg_monthly_charge = df["MonthlyCharges"].mean()
avg_tenure = df["TenureMonths"].mean()

month_to_month = df[df["ContractType"] == "Month-to-Month"]
month_to_month_churn = (
    (month_to_month["Churn"] == "Yes").mean() * 100
)

# -----------------------------
# Dashboard title
# -----------------------------
st.title("📊 Customer Churn Business KPI Dashboard")
st.markdown(
    "### Customer retention analysis for a fictional subscription business"
)

st.divider()

# -----------------------------
# KPI cards
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Customers",
    f"{total_customers}"
)

col2.metric(
    "Churned Customers",
    f"{churned_customers}"
)

col3.metric(
    "Overall Churn Rate",
    f"{churn_rate:.2f}%"
)

col4.metric(
    "Total Customer Value",
    f"₹{total_revenue:,.2f}"
)

col5.metric(
    "Avg. Tenure",
    f"{avg_tenure:.1f} months"
)

st.divider()

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Dashboard Filters")

subscription_filter = st.sidebar.multiselect(
    "Subscription Type",
    options=df["SubscriptionType"].unique(),
    default=df["SubscriptionType"].unique()
)

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["ContractType"].unique(),
    default=df["ContractType"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["SubscriptionType"].isin(subscription_filter)) &
    (df["ContractType"].isin(contract_filter)) &
    (df["Gender"].isin(gender_filter))
]

# -----------------------------
# Filtered KPIs
# -----------------------------
filtered_total = len(filtered_df)
filtered_churned = (filtered_df["Churn"] == "Yes").sum()

if filtered_total > 0:
    filtered_churn_rate = filtered_churned / filtered_total * 100
else:
    filtered_churn_rate = 0

st.subheader("Filtered Customer Overview")

f1, f2, f3, f4 = st.columns(4)

f1.metric(
    "Filtered Customers",
    filtered_total
)

f2.metric(
    "Filtered Churned",
    filtered_churned
)

f3.metric(
    "Filtered Churn Rate",
    f"{filtered_churn_rate:.2f}%"
)

f4.metric(
    "Avg Monthly Charge",
    f"₹{filtered_df['MonthlyCharges'].mean():.2f}"
    if filtered_total > 0 else "₹0"
)

st.divider()

# -----------------------------
# Churn by Contract Type
# -----------------------------
contract_churn = (
    df.groupby("ContractType")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
)

fig_contract = px.bar(
    contract_churn,
    x="ContractType",
    y="ChurnRate",
    title="Churn Rate by Contract Type",
    text="ChurnRate"
)

fig_contract.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_contract.update_layout(
    yaxis_title="Churn Rate (%)",
    xaxis_title="Contract Type",
    yaxis_range=[0, 110]
)

# -----------------------------
# Churn by Subscription
# -----------------------------
subscription_churn = (
    df.groupby("SubscriptionType")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
)

fig_subscription = px.bar(
    subscription_churn,
    x="SubscriptionType",
    y="ChurnRate",
    title="Churn Rate by Subscription Type",
    text="ChurnRate"
)

fig_subscription.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_subscription.update_layout(
    yaxis_title="Churn Rate (%)",
    xaxis_title="Subscription Type",
    yaxis_range=[0, 110]
)

chart1, chart2 = st.columns(2)

with chart1:
    st.plotly_chart(fig_contract, use_container_width=True)

with chart2:
    st.plotly_chart(fig_subscription, use_container_width=True)

# -----------------------------
# Churn by Support Tickets
# -----------------------------
support_churn = (
    df.groupby("SupportTickets")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
)

fig_support = px.line(
    support_churn,
    x="SupportTickets",
    y="ChurnRate",
    markers=True,
    title="Churn Rate vs Support Tickets"
)

fig_support.update_layout(
    xaxis_title="Support Tickets",
    yaxis_title="Churn Rate (%)"
)

# -----------------------------
# Churn by Tenure
# -----------------------------
df["TenureGroup"] = pd.cut(
    df["TenureMonths"],
    bins=[0, 6, 12, 24, 100],
    labels=[
        "0-6 months",
        "7-12 months",
        "13-24 months",
        "25+ months"
    ]
)

tenure_churn = (
    df.groupby("TenureGroup", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
)

fig_tenure = px.bar(
    tenure_churn,
    x="TenureGroup",
    y="ChurnRate",
    title="Churn Rate by Customer Tenure",
    text="ChurnRate"
)

fig_tenure.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_tenure.update_layout(
    yaxis_title="Churn Rate (%)",
    xaxis_title="Tenure Group",
    yaxis_range=[0, 110]
)

chart3, chart4 = st.columns(2)

with chart3:
    st.plotly_chart(fig_support, use_container_width=True)

with chart4:
    st.plotly_chart(fig_tenure, use_container_width=True)

# -----------------------------
# Churn distribution
# -----------------------------
churn_counts = df["Churn"].value_counts().reset_index()
churn_counts.columns = ["Churn", "Customers"]

fig_churn = px.pie(
    churn_counts,
    names="Churn",
    values="Customers",
    title="Customer Churn Distribution",
    hole=0.4
)

st.plotly_chart(fig_churn, use_container_width=True)

# -----------------------------
# Priority customers
# -----------------------------
st.divider()

st.subheader("🚨 Priority Customer Segment")

priority_customers = df[
    (df["Churn"] == "Yes") &
    (df["ContractType"] == "Month-to-Month") &
    (df["SupportTickets"] >= 3)
]

st.write(
    "Customers with Month-to-Month contracts and at least "
    "3 support tickets are highlighted for retention review."
)

p1, p2 = st.columns(2)

with p1:
    st.metric(
        "Priority Customers",
        len(priority_customers)
    )

with p2:
    st.metric(
        "Priority Segment Churn Rate",
        f"{(priority_customers['Churn'] == 'Yes').mean() * 100:.2f}%"
        if len(priority_customers) > 0 else "0%"
    )

st.dataframe(
    priority_customers[
        [
            "CustomerID",
            "SubscriptionType",
            "ContractType",
            "SupportTickets",
            "TenureMonths",
            "MonthlyCharges",
            "Churn"
        ]
    ],
    use_container_width=True
)

# -----------------------------
# Business recommendation
# -----------------------------
st.divider()

st.subheader("💡 Business Recommendation")

st.info(
    "Prioritize customers with Month-to-Month contracts and higher "
    "support-ticket activity for retention review. Newer customers "
    "should receive additional attention because shorter-tenure "
    "groups show higher observed churn in this sample."
)

st.caption(
    "Note: This dashboard uses a small synthetic dataset. "
    "The observed patterns are descriptive and should not be "
    "interpreted as proof of causation or as predictions for a "
    "larger customer population."
)

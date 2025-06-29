import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="Finance Insights Dashboard", layout="wide")
st.title("💰 Finance Insights Dashboard")

# --- Define ML functions ---
def cluster_spending_patterns(df, n_clusters=3):
    pivot_df = df.pivot_table(index="Date", columns="Category", values="Amount", fill_value=0)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    pivot_df["Cluster"] = kmeans.fit_predict(pivot_df)
    return pivot_df, kmeans

def forecast_next_month(df):
    df = df.copy()
    df['Month'] = df['Date'].dt.to_period("M")
    df['MonthNum'] = df['Date'].dt.month
    monthly = df.groupby("MonthNum")["Amount"].sum().reset_index()
    X = monthly[['MonthNum']]
    y = monthly['Amount']
    model = LinearRegression()
    model.fit(X, y)
    next_month = np.array([[df['MonthNum'].max() + 1]])
    prediction = model.predict(next_month)[0]
    return round(prediction, 2)

# --- Tabs ---
tab1, tab2 = st.tabs(["📤 Upload Transactions", "📊 Finance Insights"])

# --- Upload Tab ---
with tab1:
    uploaded = st.file_uploader("Upload your bank transaction CSV (must include Date, Category, Amount)", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        df["Date"] = pd.to_datetime(df["Date"])
        st.success("✅ File uploaded successfully!")
        st.dataframe(df.head())

# --- Analysis Tab ---
with tab2:
    if not uploaded:
        st.info("Please upload a CSV file first in the 'Upload Transactions' tab.")
    else:
        # Summary Cards
        st.subheader("💡 Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Spend", f"₹{df['Amount'].sum():,.2f}")
        with col2:
            avg = df.groupby("Date")["Amount"].sum().mean()
            st.metric("Average Daily Spend", f"₹{avg:,.2f}")

        # Charts
        st.subheader("📂 Spend by Category")
        category_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        st.bar_chart(category_totals)

        st.subheader("📈 Monthly Spending Trend")
        df["Month"] = df["Date"].dt.to_period("M")
        monthly_trend = df.groupby("Month")["Amount"].sum()
        st.line_chart(monthly_trend)

        # ML - Clustering
        st.subheader("🔍 Spending Behavior Clustering")
        pivot_df, kmeans = cluster_spending_patterns(df)
        last_cluster = pivot_df["Cluster"].iloc[-1]
        st.write(f"You fall into **Cluster {last_cluster}** based on your spending habits.")

        # ML - Forecasting
        st.subheader("🔮 Forecast: Next Month's Expenses")
        forecast = forecast_next_month(df)
        st.write(f"Based on your current spending pattern, your projected expenses for next month are approximately **₹{forecast}**.")

        # Smart Insight Section
        st.subheader("📘 Spending Overview")

        top_category = df.groupby("Category")["Amount"].sum().idxmax()
        avg_daily = df.groupby("Date")["Amount"].sum().mean()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Top Spending Category**")
            st.write(f"{top_category}")

            st.markdown("**You Belong to Cluster**")
            st.write(f"Cluster {last_cluster}")

        with col2:
            st.markdown("**Average Daily Spend**")
            st.write(f"₹{avg_daily:.2f}")

            st.markdown("**Forecasted Next Month’s Spend**")
            st.write(f"₹{forecast:,.2f}")

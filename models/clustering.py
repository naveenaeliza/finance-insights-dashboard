# models/clustering.py

import pandas as pd
from sklearn.cluster import KMeans

def cluster_spending_patterns(df, n_clusters=3):
    pivot_df = df.pivot_table(index="Date", columns="Category", values="Amount", fill_value=0)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    pivot_df["Cluster"] = kmeans.fit_predict(pivot_df)
    return pivot_df, kmeans

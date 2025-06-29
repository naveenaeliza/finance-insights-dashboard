# models/forecasting.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_next_month(df):
    df = df.copy()
    df['Month'] = df['Date'].dt.to_period("M")
    df['MonthNum'] = df['Date'].dt.month

    monthly = df.groupby("MonthNum")["Amount"].sum().reset_index()

    # Model
    X = monthly[['MonthNum']]
    y = monthly['Amount']
    model = LinearRegression()
    model.fit(X, y)

    # Predict next month
    next_month = np.array([[df['MonthNum'].max() + 1]])
    prediction = model.predict(next_month)[0]

    return round(prediction, 2)

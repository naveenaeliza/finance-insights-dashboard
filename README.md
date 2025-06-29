# 💰 Finance Insights Dashboard

A smart personal finance dashboard that analyzes spending patterns, predicts future expenses, and classifies users based on behavior — all from your uploaded bank transaction history.

---

## 🚀 Features

- 📤 Upload your own bank transaction CSV
- 📊 View total spend, average daily spend, and top categories
- 🔍 KMeans clustering to classify spending behavior
- 🔮 Linear Regression to forecast next month's expenses
- 📘 Smart summary insights
- 🧩 ML-powered insights — no manual tagging needed
- 🎛️ Built with Streamlit — responsive and interactive

---

## 📁 Folder Structure

```txt finance-insights-dashboard/ ├── app.py # Main Streamlit app ├── requirements.txt # Dependencies ├── README.md # This file ├── notebooks/ │ └── exploration.ipynb # Initial analysis & plotting ├── models/ │ ├── clustering.py # Clustering function (KMeans) │ └── forecasting.py # Forecasting model (Linear Regression) └── sample_finance.csv # (Optional) Sample transaction file ```


---

## 🧠 Tech Stack

- **Python 3.12+**
- **Streamlit** for UI
- **Pandas, NumPy** for data processing
- **Scikit-learn** for clustering & forecasting
- **Matplotlib/Seaborn** for plotting (exploration)

---

## 📊 Sample Input Format

The uploaded CSV must include these columns:

| Date       | Category   | Amount  |
|------------|------------|---------|
| 2025-05-01 | Food       | 480.00  |
| 2025-05-03 | Transport  | 220.00  |
| 2025-05-04 | Shopping   | 1350.00 |

- `Date` in `YYYY-MM-DD` format  
- `Amount` should be numeric  
- `Category` should be present (auto-tagging is an upcoming feature)

---

## 💻 Run Locally

```bash
git clone https://github.com/<your-username>/finance-insights-dashboard.git
cd finance-insights-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## 📸 Screenshots

### Upload Interface
This is where users upload their transaction CSV file.

![Upload Screenshot](screens/upload.png)

---

### Dashboard Overview
Once the data is uploaded, the dashboard displays various insights:

#### 🧾 Spend Summary & Metrics
![Dashboard Summary](screens/dashboard1 (1).png)

#### 📊 Charts & Visuals
![Dashboard Charts](screens/dashboard2.png)

#### 🔍 Clustering & Forecasting
![Dashboard Forecast](screens/dashboard3.png)

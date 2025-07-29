# 📉 project_stocks

A personal Python project that tracks daily stock price movements for a set of companies and detects unusual drops or downward trends. The system fetches historical stock data for selected tickers, saves them locally, and prepares for downstream analysis and alerting.

---

## 🚀 Project Goal

Monitor stock prices daily and:
- ✅ Identify stocks that drop **≥ 50 points for two consecutive days**
- ✅ Identify stocks that **consistently fall for 10 days straight**
- 🔔 (Coming soon) Trigger email alerts with attached graphs for affected stocks

---

## 📦 Tech Stack

| Component       | Technology              |
|----------------|--------------------------|
| Language        | Python 3.11+             |
| Data Source     | yfinance (Yahoo Finance) |
| Storage         | CSV (local per ticker)   |
| Visualization   | matplotlib / seaborn     |
| Scheduler       | schedule / cron          |
| Notifications   | SMTP (Gmail) or SendGrid |
| IDE             | VS Code                  |

---

## 📂 Project Structure

project_stocks/
├── config/
│ └── tickers.csv # List of 100 stock tickers to monitor
├── data/ # Daily price CSVs (AAPL.csv, MSFT.csv, ...)
├── plots/ # Graphs for email alerts (in progress)
├── alerts/ # Log of sent alerts (in progress)
├── src/
│ ├── fetch_data.py # ✅ Fetches last 15 days of stock prices
│ ├── analyze.py # 🔜 Detects 50-pt drops & 10-day downtrend
│ ├── visualize.py # 🔜 Generates graphs for alerts
│ └── send_email.py # 🔜 Email alerts with inline plots
├── requirements.txt # Required Python packages
└── README.md # Project overview


---

## ✅ What’s Done So Far

- [x] Created a dynamic `tickers.csv` with 100 major company symbols
- [x] Built `fetch_data.py` to read tickers and download stock history
- [x] Saved data in `/data` folder as individual CSVs
- [x] Verified data integrity (understanding Open, Close, Volume, etc.)
- [x] Set up project structure and Python environment

---

## 🛠 How to Run It

### 1. 📁 Clone the repo

git clone https://github.com/<your-username>/project_stocks.git
cd project_stocks

### 2. 🐍 Set up environment

pip install -r requirements.txt


### 3. 🏃‍♂️ Run data fetch script

python src/fetch_data.py
# This will fetch the last 15 days of stock prices for all tickers and save them under /data.


📈 Sample Output

Fetching AAPL ticker...
Saved to /data/AAPL.csv

Fetching MSFT ticker...
Saved to /data/MSFT.csv

...

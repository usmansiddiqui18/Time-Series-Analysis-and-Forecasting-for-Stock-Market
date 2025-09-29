import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Stock Forecasting Demo", layout="wide")
st.title("📈 Time Series Stock Forecasting — Demo")

DATA_DIR = Path("data/processed")

stocks = ["TCS", "Apple", "Reliance", "Infosys"]
stock = st.selectbox("Choose a stock", stocks)

file_path = DATA_DIR / f"{stock}.csv"
if file_path.exists():
    df = pd.read_csv(file_path, parse_dates=['Date'])
    st.write(f"Showing last 100 rows for **{stock}**")
    st.line_chart(df.set_index('Date')['Close'].last('365D'))
else:
    st.warning("Processed data not found. Please run notebooks to preprocess or download raw data using data_download.py.")

st.markdown("""---
### How to continue
- Use notebooks in `/notebooks` to preprocess data, train models, and save processed CSVs to `data/processed`.
- After training, save models into `/models` and load them here for predictions.
""")

# Time Series Stock Forecasting Project

This is a starter template for the **Time Series Stock Forecasting** internship project.
It includes a folder structure, starter scripts, simple Jupyter notebook templates, and a Streamlit app starter.

Stocks included in the download script: **TCS.NS, AAPL, RELIANCE.NS, INFY.NS**

## Folder structure
- data/raw: raw CSVs downloaded via yfinance
- data/processed: cleaned data ready for modeling
- notebooks: step-by-step Jupyter notebooks
- models: saved trained models
- app: Streamlit app starter
- reports: report and presentation templates

## How to use
1. Create a virtual environment and install requirements:
   ```
   python -m venv venv
   source venv/bin/activate    # on Windows: venv\Scripts\activate
   pip install -r app/requirements.txt
   ```

2. Download stock data:
   ```
   python data_download.py
   ```

3. Open notebooks in `notebooks/` and follow the numbered notebooks.

4. Run Streamlit demo:
   ```
   streamlit run app/main.py
   ```


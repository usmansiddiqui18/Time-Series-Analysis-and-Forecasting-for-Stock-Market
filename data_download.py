import yfinance as yf
from pathlib import Path
import pandas as pd

stocks = {
    "TCS": "TCS.NS",
    "Apple": "AAPL",
    "Reliance": "RELIANCE.NS",
    "Infosys": "INFY.NS"
}

out_dir = Path("data/raw")
out_dir.mkdir(parents=True, exist_ok=True)

def download_all(start="2018-01-01", end=None):
    for name, ticker in stocks.items():
        print(f"Downloading {name} -> {ticker}")
        df = yf.download(ticker, start=start, end=end)
        if df.empty:
            print(f"Warning: no data for {ticker}. Check ticker or connectivity.")
        df.reset_index(inplace=True)
        df.to_csv(out_dir / f"{name}.csv", index=False)
    print("Done. Files saved to data/raw/")

if __name__ == '__main__':
    download_all()

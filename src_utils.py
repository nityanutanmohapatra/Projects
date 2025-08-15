import pandas as pd
import yfinance as yf

def download_data(ticker, start, end, interval="1d"):
    df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)

    # Flatten multi-index columns (yfinance quirk)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]

    df = df.rename(columns=str.title)  # 'close' → 'Close'
    return df

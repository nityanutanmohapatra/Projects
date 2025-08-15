import numpy as np
import pandas as pd

def add_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_obv(df, obv_sma=20):
    df['close_diff'] = df['Close'].diff()
    df['direction'] = np.sign(df['close_diff']).fillna(0)
    df['OBV'] = (df['direction'] * df['Volume']).cumsum()
    df['OBV_SMA'] = df['OBV'].rolling(window=obv_sma, min_periods=1).mean()
    return df

def generate_signals(df, rsi_buy=30, rsi_sell=70):
    df['Signal'] = 0
    df.loc[(df['RSI'] < rsi_buy) & (df['OBV'] > df['OBV_SMA']), 'Signal'] = 1  # Buy
    df.loc[(df['RSI'] > rsi_sell) & (df['OBV'] < df['OBV_SMA']), 'Signal'] = -1  # Sell
    return df

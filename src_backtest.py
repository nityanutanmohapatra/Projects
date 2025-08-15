def backtest(df):
    df['Position'] = df['Signal'].shift()
    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Position'] * df['Returns']
    
    total_return = (1 + df['Strategy_Returns'].fillna(0)).prod() - 1
    return total_return

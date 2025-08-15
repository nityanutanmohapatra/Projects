from datetime import datetime
from src.utils import download_data
from src.strategy import add_rsi, add_obv, generate_signals
from src.backtest import backtest

TICKER = "AAPL"
START = "2023-01-01"
END = datetime.now().strftime("%Y-%m-%d")

# 1. Get Data
df = download_data(TICKER, START, END)

# 2. Apply Indicators
df = add_rsi(df, period=14)
df = add_obv(df, obv_sma=20)

# 3. Generate Buy/Sell Signals
df = generate_signals(df)

# 4. Backtest
total_return = backtest(df)
print(f"Total Return: {total_return*100:.2f}%")

# 5. Save results
df.to_csv("data/results.csv")

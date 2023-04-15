#!/usr/bin/env python3
import pandas as pd
import yfinance as yf


# download the 'AAPL' data
df = yf.download("AAPL", start="2011-01-01", end="2021-12-31", progress=False)
print(df.info())

# head
print(df.head())

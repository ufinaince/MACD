#Gerekli kütüphanelerim import işlemi
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Yahoo Finance üzerinden ilgili hisse senedinin verilerine erişimi sağlayan fonksiyon
def dataImporter(symbol="", date='2017-01-01', inBist=True):
    if inBist:
        symbol = symbol + ".IS"
        df = yf.download(symbol,
                         start=date,
                         progress=False)

    else:
        df = yf.download(symbol,
                         start=date,
                         progress=False)
    return df


# AMAZON hisse senedinin verilerini df adında bir dataframe'de tutmak
df = dataImporter("AMZN", inBist=False)

# Hisse senedinin kapanış değerlerinin görselleştirilmesi
df['Close'].plot()

# 12 günlük EMA'nın hesaplanması
df["Short"] = df['Close'].ewm(span=12, adjust=False).mean()

# 26 günlük EMA'nın hesaplanması
df["Short"] = df['Close'].ewm(span=12, adjust=False).mean()

# MACD Hattı'nın hesaplanması
df["MACD"] = df["Short"] - df["Long"]

# MACD Hattı'nın değerlerinin görselleştirilmesi
df["MACD"].plot()

# Sinyal Hattı'nın hesaplanması
df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

# Sinyal değerleri ile MACD değerlerini görsel üzerinde incelemek.

plt.figure(figsize=(12,5))
plt.plot(df.index, df.MACD, color="red")
plt.plot(df.index, df.Signal, color="blue")
plt.show()


import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/PJME_daily.csv")
with open("PJME_daily.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("PJME_daily.csv")

df = all.df.tail(100)
df = df.set_index("Date")

df["SMA"] = df ["PJME_MW"].rolling(7).mean()

df["EMA"] = df["PJME_MW"].ewm(alpha=0.05).mean()

print(df["PJME_MW"].autocorr(lag=1))

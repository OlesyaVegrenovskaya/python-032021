import requests
import pandas
акщь staticmethod
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/AirPassengers.csv")
with open("AirPassengers.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("AirPassengers.csv")
df = df.rename({"#Passengers", "Passengers"}, axis=1)
df = df.set_index("Month")
df["SMA_12"] = df["Passengers"].rolling(12, min_peroiods = 1).mean()
df.plot()
df.show
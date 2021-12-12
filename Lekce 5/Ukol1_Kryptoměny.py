import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

crypto_prices = pandas.read_csv("crypto_prices.csv")
# print(crypto_prices)
# Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn.
# Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami.
# Ošetřit to můžeš pomocí metody groupby(), jako jsme to dělali např. u metody shift().

crypto_prices["Close_2"] = crypto_prices.groupby(["Name"])["Close"].shift(1)
crypto_prices["zmena"] = (crypto_prices["Close"]-crypto_prices["Close_2"])*100/crypto_prices["Close"]

print(crypto_prices["zmena"])
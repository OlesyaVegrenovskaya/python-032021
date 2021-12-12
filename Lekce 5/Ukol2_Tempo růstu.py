import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

crypto = pandas.read_csv("crypto_prices.csv")

# Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn.
# Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami.
# Ošetřit to můžeš pomocí metody groupby(), jako jsme to dělali např. u metody shift().

crypto["zmena"] = crypto.groupby(["Name"]).shift(1)["Close"]
print(crypto)

# Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku.

# V tabulce vyber dvojici kryptoměn s vysokou hodnotou koeficientu korelace a jinou dvojici s koeficientem korelace blízko 0.
# Změny cen pro dvojice měn, které jsou hodně a naopak málo korelované, si zobraz jako bodový graf.
import requests
import pandas
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/ceny_domu.csv")
with open("ceny_domu.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("ceny_domu.csv")
print(df.head())
mod=smf.ols(formula="prodejni_cena_mil~obytna_plocha_m2", data=df)
res = mod.fit()
plt.plot(df["obytna_plocha_m2"], df["prodejni_cena_mil"], "b")
plt.plot(df["obytna_plocha_m2"],res.fittedvalues, "r")
import seaborn

seaborn.lmplot(x="obytna_plocha_m2", y="prodejna_cena_mil")

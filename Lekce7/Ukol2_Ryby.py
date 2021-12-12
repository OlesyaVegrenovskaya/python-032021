# V souboru Fish.csv najdeš informace o rybách z rybího trhu:
# délku (vertikální - Length1, diagonální - Length2 a úhlopříčnou - Length3),
# výšku,
# šířku,
# živočišný druh ryby,
# hmnotnost ryby.

import requests
import pandas
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

fish = pandas.read_csv("Fish.csv")
print(fish)

# Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
fish1 = smf.ols(formula="Weight ~ Length2", data=fish)
res = fish1.fit()
print(res.summary())

# Zkus přidat do modelu výšku ryby (sloupec Height) a porovnej, jak se zvýšila kvalita modelu.

fish2 = smf.ols(formula="Weight ~ Length2 + Height", data=fish)
res = fish2.fit()
print(res.summary())

# Hodnota R-squared prvi modeli je 0.844. Po pridani sloupca Height přestnost modelu zvysuje do 0.875

# Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryby.

fish3 = fish.groupby('Species')['Weight'].mean()
fish["Druhy_prum"] = fish["Species"].map(fish3)
predictors = ["Length2", "Height", "Druhy_prum"]
mod = smf.ols(formula="Weight ~ Length2 + Height + Druhy_prum", data=fish)
res = mod.fit()
print(res.summary())
# R-squared se zvysila na 0.9



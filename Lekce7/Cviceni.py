import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/insurance.csv")
with open("insurance.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("insurance.csv")
print(df.head())

# # seaborn.heatmap(df.corr(), aanot=True, fmt=".2f")
# mod = smf.ols(formula="charges~age+sex", data=df)
#
#
# mod = smf.ols(formula="charges~age+sex+smoker", data=df)
# res = mod.fit()
# print(res.summary())

mean_charges_region = df.groupby("region")["charges"].mean()
df["mean_charges_region"] = df["region"].map(mean_charges_region)
mod = smf.ols(formula="charges~age+sex+smoker+mean_charges_region", data=df)
res = mod.fit()
print(res.summary())


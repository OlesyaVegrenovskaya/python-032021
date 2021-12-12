# V souboru Concrete_Data_Yeh.csv najdeš informace o kvalitě cementu.
# Sloupce 1-7 udávají množství jednotlivých složek v kg, které byly přimíchány do krychlového metru betonu
# (např. cement, voda, kamenivo, písek atd.).
# Ve sloupci 8 je stáří betonu a ve sloupci 9 kompresní síla betonu v megapascalech.

import requests
import pandas
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

cement = pandas.read_csv("Concrete_Data_Yeh.csv")
print(cement.isna().sum())

# Vytvoř regresní model, který bude predikovat kompresní sílu betonu na základě všech množství jednotlivých složek a jeho stáří.

mod=smf.ols(formula="csMPa ~ cement + slag + flyash + water + coarseaggregate + fineaggregate + age", data=cement)
res=mod.fit()
print(res.summary())

# Zhodnoť kvalitu modelu.

# R-squared:0.612 neni tak vysoká přestnost.

# Tipni si, která ze složek betonu ovlivňuje sílu betonu negativní (tj. má záporný regresní koeficient). Napiš, o kterou složku jde, do komentáře svého programu.

mod=smf.ols(formula="csMPa ~ cement + slag + flyash + coarseaggregate + fineaggregate + age", data=cement)
res=mod.fit()
print(res.summary())

# Voda má záporny regresní koeficent. To známena že čim vice vody bude v betonu tim niže bude jeho kvalita.
# Kdýž odstránim vodu hodnota R-squared : 0.597. To znamena že voda nemá negativny vliv na model.
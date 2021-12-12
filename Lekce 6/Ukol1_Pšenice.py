# V souboru jsou data o délce zrn pšenice v milimetrech pro dvě odrůdy - Rosa a Canadian.
# Proveď statistický test hypotézy o tom, zda se délka těchto dvou zrn liší.
# K testu použij Mann–Whitney U test, který jsme používali na lekci.

import requests
import pandas
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

# V komentáři u programu formuluj hypotézy, které budeš ověřovat. Je potřeba formulovat dvě hypotézy - nulovou a alternativní.
# Provádíme oboustranný test, takže alternativní hypotézy by měla být, že průměry délky zrna jsou různé (nejsou si rovné).

# H0: Délka zrn je stejná
# H1: Délka zrn se liší


# Pomocí modulu scipy urči p-hodnotu testu a porovnej ji s hladinou významnosti 5 %.
# V komentáři uveď závěr, jestli nulovou hypotézu na základě p-hodnoty zamítáme.

psenice = pandas.read_csv("psenice.csv")
print(psenice)
x = psenice["Rosa"]
y = psenice["Canadian"]
print(mannwhitneyu(x, y))

# pvalue=3.522437521029982e-24 a to je < 5% proto H0 zámítáme
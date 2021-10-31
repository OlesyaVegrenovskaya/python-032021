
# V souboru air_polution_ukol.csv najdeš data o množství jemných částic změřených v ovzduší v jedné plzeňské
# meteorologické stanici.

# Načti dataset a převeď sloupec date (datum měření) na typ datetime.

import pandas
import requests
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")

air_polution["date_convert"] = pandas.to_datetime(air_polution["date"])


# Přidej sloupce s rokem a číslem měsíce, které získáš z data měření.

air_polution["year"] = air_polution["date_convert"].dt.year
air_polution["month"] = air_polution["date_convert"].dt.month


# Vytvoř pivot tabulku s průměrným počtem množství jemných částic (sloupec pm25) v jednotlivých měsících
# a jednotlivých letech. Jako funkci pro agregaci můžeš použít numpy.mean.

air_polution_pivot = pandas.pivot_table(air_polution, index ="month", columns="year", values="pm25", aggfunc=numpy.mean)
print(air_polution_pivot)
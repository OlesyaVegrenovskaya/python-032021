import requests
import pandas

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

# Načti dataset a převeď sloupec date (datum měření) na typ datetime.


castice = pandas.read_csv("air_polution_ukol.csv")
# print(castice)

castice["date"]=pandas.to_datetime(castice["date"])
castice["year"] = castice["date"].dt.year
castice["month"] = castice["date"].dt.month
# print(castice)

# Z dat vyber data za leden roku 2019 a 2020.

castice_leden2019 = castice[(castice["year"] == 2019) & (castice["month"] == 1)]
castice_leden2020 = castice[(castice["year"] == 2020) & (castice["month"] == 1)]

x = castice_leden2019["pm25"]
y = castice_leden2020["pm25"]

# Porovnej průměrné množství jemných částic ve vzduchu v těchto dvou měsících pomocí Mann–Whitney U testu.

from scipy.stats import mannwhitneyu

print(mannwhitneyu(x, y))
# Formuluj hypotézy pro oboustranný test (nulovou i alternativní) a napiš je do komentářů v programu.

# H0:Množství jemných částic ve vzduchu pro leden 2019 a leden 2020  je stejné.
# H1:Množství jemných částic ve vzduchu pro leden 2019 a leden 2020  se liší.

# P-value je  1,1% proto nulová hypoteza je zamitnuta. Množství jemných částic ve vzduchu pro leden 2019 a leden 2020  se liší.

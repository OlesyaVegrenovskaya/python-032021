import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/baroko_half_marathon.csv")
open("baroko_half_marathon.csv", 'wb').write(r.content)

# V souboru baroko_half_marathon.csv najdeš výsledky Baroko půlmaratonu, který se běží každý rok na začátku září.
# Tvým úkolem je vzít výsledky za dva po sobě jdoucí roky a porovnat výkony běžců, kteří se zúčastnili obou závodů.
# Závěrem analýzy bude zjištění, kolik běžců se meziročně zlepšilo a kolik zhoršilo.

baroko_half_marathon = pandas.read_csv("baroko_half_marathon.csv")

# Data musíš nejprve seřadit. Seřaď data dle jména závodníka, ročík a roku závodu.

baroko_half_marathon = baroko_half_marathon.sort_values(["Jméno závodníka", "Ročník", "Rok závodu", "FINISH"])
#
# Nyní pracuj se sloupcem FINISH, který obsahuje čas závodníka.
# Převeď tento sloupec na typ datetime. Nemusíš používat žádný formátovací řetězec.

baroko_half_marathon["FINISH"] = pandas.to_datetime(baroko_half_marathon["FINISH"])

# Použij metodu shift, abys získal(a) na stejném řádku časy závodníka v obou letech.
# Aby se ti ale nepomíchaly časy rozdílných závodníků, aplikuj metodu groupby(),
# jako jsme to udělali u dat indexu ekonomické svobody.

baroko_half_marathon["FINISH PREVIOUS YEAR"] = baroko_half_marathon.groupby(["Jméno závodníka", "Ročník"])["FINISH"].shift()

# Z tabulky odstraň data závodníků, kteří se zúčastnili pouze jednoho za závodů, a řádky s daty z roku 2019.
# Můžeš použít třeba metodu dropna() a jedním příkazem se zbavit všech zbytečných řádků.

baroko_half_marathon = baroko_half_marathon.dropna(subset=["FINISH PREVIOUS YEAR"])

print(baroko_half_marathon.head())

# Vypočti rozdíl mezi časy závodníků v letech 2019 a 2020.

baroko_half_marathon["diff"] = baroko_half_marathon["FINISH PREVIOUS YEAR"]-baroko_half_marathon["FINISH"]

# Vypočítej, kolik závodníků si svůj čas zlepšilo a kolik zhoršilo.
# Při dotazu na porovnávání můžeš sloupec s časovým rozdílem porovnat s hodnotou pandas.
# Timedelta("P0D"), což je nulová změna.
# Pomocí tohoto porovnání jasně odlišíš, kteří závodníci se zlepšili a kteří zhoršili.
baroko_half_marathon["diff_text"]= numpy.where(baroko_half_marathon["diff"]>pandas.Timedelta("P0D"), "zhoršení", "zlepšení")

print(baroko_half_marathon.groupby(["diff_text"]).size())
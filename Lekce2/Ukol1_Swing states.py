import requests
import pandas
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
 open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

president_elections = pandas.read_csv("1976-2020-president.csv")


#Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()).
# Nezapomeň, že data je před použitím metody nutné seřadit

president_elections = president_elections.sort_values(["year", "state", "candidatevotes"])

# a spolu s metodou rank() je nutné použít metodu groupby().

president_elections["RANK"] = president_elections.groupby(["state", "year"])["candidatevotes"].rank(method="min", ascending=False)


# Pro další analýzu jsou důležití pouze vítězové.
# Ponech si v tabulce pouze řádky, které obsahují vítěze voleb v jednotlivých letech v jednotlivých státech.
president_winner = president_elections[president_elections["RANK"]==1]


# Pomocí metody shift() přidej nový sloupec, abys v jednotlivých řádcích měl(a) po sobě vítězné strany ve
# dvou po sobě jdoucích letech.

president_winner = president_winner.sort_values(["state", "year"])
president_winner["previous_elections"] = president_winner.groupby(["state"])["party_simplified"].shift(1)


# Porovnej, jestli se ve dvou po sobě jdoucích letech změnila vítězná strana.
# Můžeš k tomu použít např. funkce numpy.where a vložit hodnotu 0 nebo 1 podle toho, jestli došlo ke změně vítězné strany.

president_winner=president_winner.dropna(subset=["previous_elections"])
president_winner["party_change"]=numpy.where(president_winner["party_simplified"]==president_winner["previous_elections"],0,1)


# Proveď agregaci podle názvu státu a seřaď státy podle počtu změn vítězných stran.

number_of_changes = president_winner.groupby(["state"])["party_change"].sum()
number_of_changes = number_of_changes.sort_values()
print(number_of_changes)

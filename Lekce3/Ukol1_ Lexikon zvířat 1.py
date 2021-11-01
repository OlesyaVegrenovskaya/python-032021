import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

# Načtení dat
# Načti si soubor pomocí metody read_csv. Pozor, tento dataset využívá jako oddělovač středník, nikoliv čárku.
# Při načítání dat proto nastav parametr sep na znak středníku (";").

lexicon_of_beasts = pandas.read_csv("lexikon-zvirat.csv", sep=";")
#
# Poslední sloupec a poslední řádek obsahují nulové hodnoty. Zbav se tohoto sloupce a řádku.
# Nastav sloupec id jako index pomocí metody set_index.
lexicon_of_beasts = lexicon_of_beasts.dropna(how="all", axis=0)
lexicon_of_beasts = lexicon_of_beasts.dropna(how="all", axis=1)
lexicon_of_beasts = lexicon_of_beasts.set_index("id")
#Napiš funkci check_url, která bude mít jeden parametr radek.
# Funkce zkontroluje, jestli je odkaz v pořádku podle několika pravidel.
def check_url(radek):
    if isinstance(radek.image_src, str) and (radek.image_src.startswith("https://zoopraha.cz/images/")) and (radek.image_src.endswith("jpg")):
        return True
error_list=[]
for radek in lexicon_of_beasts.itertuples():
    if check_url(radek) is True:
        error_list.append(radek.title)
print(error_list)






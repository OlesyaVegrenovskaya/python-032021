# Chceme ke každému zvířeti vytvořit popisek na tabulku do zoo.
# Popisek bude využívat sloupců title (název zvířete), food (typ stravy), food_note (vysvětlující doplněk ke stravě)
# a description (jak zvíře poznáme). Napiš funkci popisek, která bude mít jeden parametr radek.
# Funkce spojí informace dohromady. Následně použijte metodu apply, abyste vytvořili nový sloupec s tímto popiskem.


import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

animals = pandas.read_csv("lexikon-zvirat.csv", sep=";")

def popisek (radek):
    title = str(radek.title)
    food = str(radek.food)
    food_note = str(radek.food_note)
    description = str(radek.description)
    return f"{title} preferuje následující typ stravy: {food}. Konkrétně ocení když mu do misky přistanou {food_note}. \nJak toto zvíře poznáme: {description}."

animals["popisek"]=animals.apply(popisek,axis=1)

print(animals["popisek"])
print(animals["popisek"][320])
print(animals["popisek"][300])
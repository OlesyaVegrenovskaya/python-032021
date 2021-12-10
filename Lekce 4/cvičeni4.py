import pandas
from sqlalchemy import create_engine

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "olesya.vegrenovskaya"
USERNAME = f"olesya.vegrenovskaya@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "VtSJp2X8zG6UKnBD"


# V naší databázi se nachází dvě tabulky:
#
# pocet_obyvatel, která udává ke každé obci počet obyvatel (na základě sčítání v roce 2011)
# pocet_bytu, která udává, kolik se v roce 2011 postavilo v každé obci bytů.

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)
pocet_obyvatel = pandas.read_sql("pocet_obyvatel", con=engine)
# print(pocet_obyvatel.head())
pocet_bytu = pandas.read_sql("pocet_bytu", con=engine)
# print(pocet_bytu.head())

# Tabulky mají jen pár tisíc řádků, proto si je můžeš celé načíst do pandasu pomocí metody read_sql.
# Kterých 5 obcí s počtem obyvatel vyšším, než 1000 mělo nejlepší poměr (nejvíc nových bytů na 100 obyvatel)?
# Nápověda: tabulky spoj pomocí metody merge na názvu obce.

# pocet_obyvatel_bytu = pocet_obyvatel.merge(pocet_bytu, on="obec")
pocet_obyvatel_bytu = pandas.read_sql("SELECT * FROM pocet_obyvatel INNER JOIN pocet_bytu ON pocet_obyvatel.obec = pocet_bytu.obec", con=engine)
pocet_obyvatel_bytu["pocet bytu na 100 obyvatel"] = (pocet_obyvatel_bytu["pocet_bytu"]/pocet_obyvatel_bytu["pocet_obyvatel"])*100
print(pocet_obyvatel_bytu[pocet_obyvatel_bytu["pocet_obyvatel"]>1000].sort_values("pocet bytu na 100 obyvatel",  ascending=False).head())
# Dobrovolný doplněk:
# Zkus zjistit, jestli spojení tabulek můžeme udělat na úrovni SQL dotazu a získat je už spojené, místo toho,
# abychom obě načetly a pak je spojovali.
pocet_obyvatel_bytu = pandas.read_sql("SELECT * FROM pocet_obyvatel INNER JOIN pocet_bytu ON pocet_obyvatel.obec=pocet_bytu.obec", con=engine)
print(pocet_obyvatel_bytu)
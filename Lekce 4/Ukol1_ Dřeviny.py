import pandas
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import numpy

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "olesya.vegrenovskaya"
USERNAME = f"olesya.vegrenovskaya@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "VtSJp2X8zG6UKnBD"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)
inspector = inspect(engine)
dreviny=pandas.read_sql("dreviny", con=engine)
# print(dreviny.head())
# print(dreviny.head())
# Pomocí SQL dotazu do databáze si připrav dvě pandas tabulky:
# tabulka smrk bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska"

smrk=pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt= 'Smrk, jedle, douglaska'", con=engine)
print(smrk.head())

# tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"
nahodila_tezba=pandas.read_sql("SELECT * FROM dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
print(nahodila_tezba.head())

#Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.

smrk_aggregated = smrk.groupby(["rok"])["hodnota"].sum()
smrk_aggregated.plot()
plt.show()

#Vytvoř graf (nebo několik grafů), který ukáže vývoj objemu těžby v čase pro všechny typy nahodilé těžby.

pivot = nahodila_tezba.pivot_table(values="hodnota", aggfunc=numpy.sum, columns="prictez_txt", index="rok")
pivot.plot()
plt.show()

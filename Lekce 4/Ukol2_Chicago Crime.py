# Chicago Crime
# Tabulka crime v naší databázi obsahuje informace o kriminalitě v Chicagu. Data si můžete i interaktivně prohlédnout na mapě zde.
# Dataset je poměrně velký, a tak si určitě vytáhneme vždy jen nějaký výběr, se kterým budeme dále pracovat.


import pandas
from sqlalchemy import create_engine, inspect


HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "olesya.vegrenovskaya"
USERNAME = f"olesya.vegrenovskaya@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "VtSJp2X8zG6UKnBD"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)
inspector = inspect(engine)


# Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").

kradeze_mot_voz = pandas.read_sql("SELECT * FROM crime where \"PRIMARY_DESCRIPTION\"= 'MOTOR VEHICLE THEFT'", con=engine)
print(kradeze_mot_voz.head())

# Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
kradeze_aut = kradeze_mot_voz[kradeze_mot_voz["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"]

# Ve kterém měsíci dochází nejčastěji ke krádeži auta?

kradeze_aut["DATE_OF_OCCURRENCE"] = pandas.to_datetime(kradeze_aut["DATE_OF_OCCURRENCE"])
kradeze_aut["MONTH"] = kradeze_aut["DATE_OF_OCCURRENCE"].dt.month
kradeze_mesice = kradeze_aut.groupby("MONTH").size()

print(kradeze_mesice)
import os
import pandas
import sqlalchemy

import psycopg2

from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "olesya.vegrenovskaya"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "VtSJp2X8zG6UKnBD"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

inspector = inspect(engine)
print(inspector.get_table_names())

df = pandas.read_sql(f"uzivatele-{USER}", con=engine)
print(df)
#
# print(df[df["produkt"] == "sušička ovoce"]["address_street", "country"])

# df = pandas.read_sql("SELECT country from \"uzivatele-olesya.vegrenovskaya\" WHERE produkt = 'sušička ovoce'", con=engine)
# print(df)

nova_data= pandas.DataFrame({'name': ['Hana', 'Andrea'], 'country':['Czech Republic', 'Czech Republic'],
                            'address_street': ['Korunní', 'Vinohradská'], 'age': [35, 45], 'produkt': ['kávovar', 'vysavac']})

nova_data.to_sql(f"uzivatele-{USER}", con=engine, index=False, if_exists="append")
df = pandas.read_sql(f"uzivatele-{USER}", con=engine)
print(df)
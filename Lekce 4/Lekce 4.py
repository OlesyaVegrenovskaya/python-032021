import os
import pandas
import psycopg2
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "olesya.vegrenovskaya"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "VtSJp2X8zG6UKnBD"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

# engine = create_engine("sqlite:///:memory:")
# engine = create_engine("sqllite:///databaze.db")

# inspector = inspect(engine)
# print(inspector.get_columns("uzivatele-olesya.vegrenovskaya"))

df = pandas.read_sql(f"uzivatele-{USER}", con=engine)
print(df.columns)
# df.to_sql(f"uzivatele-{USER}", con=engine, index=False, if_exists="replace")
nova_data = pandas.DataFrame({'name': ['Hana', 'Andrea'], 'country': ['Czech Republic', 'Czech Republic'],
                              'address_street': ['Korunní', 'Vysočany'], 'age': [35,45], 'produkt': ['kávovar', 'vysavač']})
print(nova_data)

nova_data.to_sql(f"uzivatele-{USER}", con=engine, index=False, if_exists="append")
print(df)
# V naší databázi se nachází dvě tabulky:
#
# pocet_obyvatel, která udává ke každé obci počet obyvatel (na základě sčítání v roce 2011)
# pocet_bytu, která udává, kolik se v roce 2011 postavilo v každé obci bytů.
# Tabulky mají jen pár tisíc řádků, proto si je můžeš celé načíst do pandasu pomocí metody read_sql.
# Kterých 5 obcí s počtem obyvatel vyšším, než 1000 mělo nejlepší poměr (nejvíc nových bytů na 100 obyvatel)?
# Nápověda: tabulky spoj pomocí metody merge na názvu obce.
#
# Dobrovolný doplněk: Zkus zjistit, jestli spojení tabulek můžeme udělat na úrovni SQL dotazu a získat je už spojené,
# místo toho, abychom obě načetly a pak je spojovali.

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


df_pocet_obyvatel = pandas.read_sql(f'pocet_obyvatel', con=engine)
print(df_pocet_obyvatel)
df_pocet_bytu = pandas.read_sql(f'pocet_bytu', con=engine)
print(df_pocet_bytu)
merged_df = pandas.merge(df_pocet_bytu, df_pocet_obyvatel, on='obec')
print(merged_df)
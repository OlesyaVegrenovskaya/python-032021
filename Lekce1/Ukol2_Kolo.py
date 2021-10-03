import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

df_London_bicycle_rental = pandas.read_csv("london_merged.csv")
print(df_London_bicycle_rental.columns)
print(df_London_bicycle_rental)
df_London_bicycle_rental["timestamp"] = pandas.to_datetime(df_London_bicycle_rental["timestamp"])
df_London_bicycle_rental["year"] = df_London_bicycle_rental["timestamp"].dt.year
df_London_bicycle_rental_pivot = pandas.pivot_table(df_London_bicycle_rental, index="year", columns="weather_code", values="cnt", aggfunc=numpy.sum, margins=True)

print(df_London_bicycle_rental_pivot)

df_London_bicycle_rental_pivot2 = df_London_bicycle_rental_pivot.div(df_London_bicycle_rental_pivot.iloc[:,-1], axis=0)
print(df_London_bicycle_rental_pivot2)
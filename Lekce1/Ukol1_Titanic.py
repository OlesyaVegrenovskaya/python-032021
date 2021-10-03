import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

df_titanic = pandas.read_csv("titanic.csv")
total = df_titanic.Survived.sum()
print(total)
# print(df_titanic)

df_titanic_pivot = pandas.pivot_table(df_titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=numpy.sum)
print(df_titanic_pivot)

df_titanic_pivot1 = pandas.pivot_table(df_titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=numpy.mean)
print(df_titanic_pivot1)

# df_titanic_pivot2 = pandas.pivot_table(df_titanic, index="Sex", columns="Pclass", values="Survived", aggfunc=len(Survived))
# print(df_titanic_pivot2)
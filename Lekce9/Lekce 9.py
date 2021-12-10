import sklearn
import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)
data = pandas.read_csv("water-potability.csv")
print(data.isna().sum)




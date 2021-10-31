# #
# # import statistics
# # import matplotlib.pyplot as plt
# #
# # first_seven_days = [
# #   5.1,
# #   5,
# #   4.8,
# #   4.7,
# #   63.7,
# #   4.3,
# #   7.1,
# #   0.8,
# # ]
# #
# # x = range(1, len(first_seven_days) + 1)
# # # plt.bar(x, first_seven_days)
# # # plt.show()
# # print(statistics.mean(first_seven_days))
# # second_seven_days = [
# #   8.3,
# #   16.5,
# #   10.8,
# #   7.5,
# #   6.2,
# #   6.4,
# #   1.6,
# #   1.7,
# #   1.9,
# #   1.9,
# #   4,
# #   1.8,
# #   2.4,
# #   2,
# #   15.1,
# #   11.2,
# #   11.8,
# #   21.9,
# #   3.9
# # ]
# # print(statistics.pvariance(first_seven_days))
# # print(statistics.pvariance(second_seven_days))
#
#
# import yfinance as yf
# import pandas
#
#
# msft = yf.Ticker("MSFT")
# msft_df = msft.history(period="1y")
# aapl = yf.Ticker("AAPL")
# aapl_df = aapl.history()
import requests
import statistics
import pandas

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/UberDrives.csv")
open("UberDrives.csv", "wb").write(r.content)

df = pandas.read_csv("UberDrives.csv")
# print(df.head())
#
# print(df.groupby(['CATEGORY'])['MILES'].median())
# print(df.groupby(['CATEGORY'])['MILES'].mean())
# print(df.groupby(['CATEGORY'])['MILES'].std())
# print(df.groupby(['CATEGORY'])['MILES'].min())
# print(df.groupby(['CATEGORY'])['MILES'].max())
# g = df.groupby(['CATEGORY'])['MILES'].median().to_frame()
# g.columns = ['median']
# g['prumer'] = df.groupby(['CATEGORY'])['MILES'].mean()
# g['min'] = df.groupby(['CATEGORY'])['MILES'].min()
# g['max'] = df.groupby(['CATEGORY'])['MILES'].max()
# g['variacni_rozpeti'] = g['max'] - g['min']
# print(g)


import itertools

ranks = (1,2,3,4,5,6)
abcd = ('A', 'B', 'C', 'D', 'E', 'F')

list_of_place = list(itertools.product(ranks, abcd))

for item in list_of_place:
  print(f"{item[0]} {item[1]}")


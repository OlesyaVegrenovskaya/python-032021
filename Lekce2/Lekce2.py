# employee_list = [
#     {"first_name": "Jan", "last_name": "Novák", "position": "senior projektový manažer", "hourly_rate": 1550},
#     {"first_name": "Jan", "last_name": "Novák", "position": "junior software developer", "hourly_rate": 980},
#     {"first_name": "Josef", "last_name": "Opatrný", "position": "sales manager", "hourly_rate": 1500}
# ]
#
# project_hours_list = [
#     {"year": 2021, "month": 8, "first_name": "Jan", "last_name": "Novák", "hours": 20},
#     {"year": 2021, "month": 8, "first_name": "Jan", "last_name": "Novák", "hours": 160},
#     {"year": 2021, "month": 8, "first_name": "Josef", "last_name": "Opatrný", "hours": 24},
# ]
#
# import pandas
#
# employees_df=pandas.DataFrame(employee_list)
# print(employees_df)
# project_hours_df=pandas.DataFrame(project_hours_list)
# print(project_hours_df)
# merged_dataframe = pandas.merge(project_hours_df,employees_df)
# print(merged_dataframe)
#
# employee_list = [
#     {"id": 1, "first_name": "Jan", "last_name": "Novák", "position": "senior projektový manažer", "hourly_rate": 1550},
#     {"id": 2, "first_name": "Jan", "last_name": "Novák", "position": "junior software developer", "hourly_rate": 980},
#     {"id": 3, "first_name": "Josef", "last_name": "Opatrný", "position": "sales manager", "hourly_rate": 1500}
# ]
#
# project_hours_list = [
#     {"year": 2021, "month": 8, "employee_id": 1, "hours": 20},
#     {"year": 2021, "month": 8, "employee_id": 2, "hours": 160},
#     {"year": 2021, "month": 8, "employee_id": 3, "hours": 24},
# ]
#
# employees_df = pandas.DataFrame(employee_list)
import requests
import pandas
import numpy
import datetime


# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/data_with_ids.json")
# open("data_with_ids.json", 'wb').write(r.content)
#
# data_with_ids = pandas.read_json("data_with_ids.json")
# print(data_with_ids.shape[0])
# # print(data_with_ids.head())
# print(data_with_ids["bank_id"].nunique())
# data_with_ids_unique = data_with_ids.drop_duplicates(ignore_index=True)
# # print(data_with_ids_unique.head())
# print((data_with_ids_unique.shape))

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/covid_data.csv")
# open("covid_data.csv", 'wb').write(r.content)
# covid_data = pandas.read_csv("covid_data.csv")
# covid_data =covid_data.drop_duplicates(subset=["date"], keep="last")
# print(covid_data.head())

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices.csv")
# open("invoices.csv", 'wb').write(r.content)
# invoices = pandas.read_csv("invoices.csv")
# invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"])
# invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("60 days")
# today_date = datetime.datetime.now()
# invoices["status"] = numpy.where(invoices["due_date"] < today_date, "po splatnosti", "před splatnosti")
# print(invoices.groupby("status")["amount"].sum())

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices_2.csv")
# open("invoices_2.csv", 'wb').write(r.content)
#
# invoices_2 = pandas.read_csv("invoices_2.csv")
# invoices_2["invoice_date"] = pandas.to_datetime(invoices_2["invoice_date"], format="%d. %m. %Y")
# invoices_2["payment_date"] = pandas.to_datetime(invoices_2["payment_date"], format="%d. %m. %Y")
# invoices_2_paid = invoices_2.dropna().reset_index(drop=True)
# invoices_2_paid["paid_in"] = invoices_2["payment_date"]-invoices_2["invoice_date"]
# average_payment_data = invoices_2_paid.groupby(["customer"])["paid_in"].mean()
# average_payment_data = pandas.DataFrame(average_payment_data)
# invoices_2_not_paid = invoices_2[invoices_2["payment_date"].isna()]
# invoices_2_not_paid = pandas.merge(invoices_2_not_paid, average_payment_data, on=["customer"], how="outer")
# invoices_2_not_paid["expected_payment_date"] = invoices_2_not_paid["invoice_date"]+invoices_2_not_paid["paid_in"]
# invoices_2_not_paid["expected_payment_date"] = invoices_2_not_paid["expected_payment_date"].dt.date
# print(invoices_2_not_paid)

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/signal_monitoring.csv")
# open("signal_monitoring.csv", 'wb').write(r.content)
# signal_monitoring = pandas.read_csv("signal_monitoring.csv")
# signal_monitoring["event_date_time"] = pandas.to_datetime(signal_monitoring["event_date_time"])
# signal_monitoring["event_date_time2"] = signal_monitoring["event_date_time"].shift(-1)
# signal_monitoring["even_lenth"] = signal_monitoring["event_date_time2"] - signal_monitoring["event_date_time"]
# print(signal_monitoring.head())

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/ioef.csv")
open("ioef.csv", 'wb').write(r.content)

ioef = pandas.read_csv("ioef.csv")
ioef["Rank"] = ioef.groupby(["Index Year"])["Overall Score"].rank(ascending=False)
# ioef = ioef.sort_values(["Name", "Index Year"])
# ioef["Rank Prevision Year"] = ioef.groupby(["Name"])["Rank"].shift()
# ioef["Difference"] = ioef["Rank"] - ioef["Rank Prevision Year"]
print(ioef)
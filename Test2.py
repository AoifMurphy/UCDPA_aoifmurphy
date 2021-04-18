import pandas as pd
import numpy as np

telco_data=pd.read_csv("Telco-Customer-Churn.csv")
print(telco_data)

print(telco_data.info())

print (telco_data.head())

missing_value=telco_data.isnull().sum
print(missing_value)

print(telco_data.describe())

customer_list=telco_data[telco_data["customerID"], telco_data["Churn"]]
print(customer_list)


def import_csv(filename):
    data=pd.read_csv(filename)
    print(data.head())
    print(data)


import_csv("Telco-Customer-Churn.csv")

x=telco_data["TotalCharges"].cummax()
print(x)





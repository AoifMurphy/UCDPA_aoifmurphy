import pandas as pd
import numpy as np

telco_data=pd.read_csv("Telco-Customer-Churn.csv")
print(telco_data)

print(telco_data.info())

print (telco_data.head())

missing_value=telco_data.isnull().sum
print(missing_value)

print(telco_data.describe())

def import_csv(filename):
    data=pd.read_csv(filename)
    print(data.head())

import_csv("portfolio.csv")

def cleaned_data(filename):
    data=

customer_list=telco_data["customerID"]
print(customer_list)
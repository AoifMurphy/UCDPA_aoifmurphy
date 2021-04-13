# import packages
import pandas as pd

import numpy as np

telco_data=pd.read_csv("Telco-Customer-Churn.csv")
print(telco_data)

print(telco_data.info())

print (telco_data.head())

missing_value=telco_data.isnull().sum
print(missing_value)

print(telco_data.describe())

def importdata(filename):
    data=pd.read_csv(filename)
    print(data.head())
    print(data.index)
    print(data.info)

importdata("Telco-Customer-Churn.csv")
importdata("portfolio.csv")
importdata("profile.csv")
importdata("transcript.csv")
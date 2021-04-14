import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Customer_Churn=pd.read_csv("Telco-Customer-Churn.csv")
print(Customer_Churn)
print(Customer_Churn.describe)
print(Customer_Churn.info)
print(Customer_Churn.head())

droprows=Customer_Churn.dropna()
print(Customer_Churn.shape, droprows.shape)

TotalSpend=Customer_Churn["TotalCharges"].sum()
print(TotalSpend)


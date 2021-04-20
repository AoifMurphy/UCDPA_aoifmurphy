import pandas as pd
import numpy as np
customer_profile = pd.read_csv(r'profile.csv')
print(customer_profile.head())

customer_portfolio = pd.read_csv(r'portfolio.csv')
print(customer_portfolio)

Customer_Churn = pd.read_csv(r'Telco-Customer-Churn.csv')
print(Customer_Churn.head())
print(Customer_Churn.columns)
print(Customer_Churn.describe())


def import_csv(Filename):
    data=pd.read_csv(Filename)
    print(data.head())
    missing_value = data.isnull ().sum
    print (missing_value)

import_csv("profile.csv")

Starbucks_Cust_Prof = pd.read_csv("profile.csv")
print(Starbucks_Cust_Prof.head())
print(Starbucks_Cust_Prof.shape)

clean_data = Starbucks_Cust_Prof["income"].fillna(Starbucks_Cust_Prof["income"].mean()), inplace=True)
print(clean_data)





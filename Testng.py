import pandas as pd
import numpy as np
customer_profile = pd.read_csv(r'profile.csv')
print(customer_profile.head())

customer_portfolio = pd.read_csv(r'portfolio.csv')
print(customer_portfolio)

Customer_Churn = pd.read_csv(r'Telco-Customer-Churn.csv')
print(Customer_Churn.head())
print(Customer_Churn.columns())
print(Customer_Churn.describe())




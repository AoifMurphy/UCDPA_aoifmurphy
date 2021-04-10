import pandas as pd
import numpy as np
customer_profile = pd.read_csv(r'profile.csv')
print(customer_profile.head())

customer_portfolio = pd.read_csv(r'portfolio.csv')
print(customer_portfolio)

# Lists

x = [2, 5, 4, 0, 7, 1]

print(x[0])

np_2d = np.array([[2,3],[4,5]])
print(np_2d[-2,1])

p = 3
q = "Hello! "
print(q * p)

Customer_Churn = pd.read_csv(r'C:\Users\aoife\Desktop\UCDPA_AoifePMurphy\Telco-Customer-Churn.csv')
print(Customer_Churn.head())
print(Customer_Churn.columns)


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

df=Customer_Churn[["gender", "Churn"]]
print(df.head())

df = pd.read_csv('Telco-Customer-Churn.csv', index_col = 0)
print(df)

Gender_Churn=df[["gender", "Churn"]]
print(Gender_Churn.head(25))

Churn=df["Churn"]
print(Churn.head(20))

print(df)

Totals=df.sum(axis=0, skipna=True)
print(Totals)

Infl=df.columns
print(Infl)

My_Dict={'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges', 'Churn'}

print(My_Dict)
print(type(My_Dict))


List_of_influences=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges', 'Churn']
print(type(List_of_influences))







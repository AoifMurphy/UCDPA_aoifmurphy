import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

df=pd.read_csv('Telco-Customer-Churn.csv')
print(df.head())
print(df.info())
df.TotalCharges = pd.to_numeric(df.TotalCharges, errors='coerce')
df.isnull().sum()

df1 = df.iloc[:,1:]

#transform to binary code
df1['Churn'].replace(to_replace='Yes', value=1, inplace=True)
df1['Churn'].replace(to_replace='No',  value=0, inplace=True)

df_dummies = pd.get_dummies(df1)
df_dummies.head()
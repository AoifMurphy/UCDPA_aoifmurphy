import pandas as pd
import numpy as np

#import csv file
Profile_Cust_Stbks = pd.read_csv("profile.csv")
print(Profile_Cust_Stbks.head())

#Check for missing values
missing_values_count = Profile_Cust_Stbks.isnull().sum()
print(missing_values_count)

#Drop rows where data is missing
droprows=Profile_Cust_Stbks.dropna()
print(Profile_Cust_Stbks.shape, droprows.shape)

#Replace Missing Values instead
clean_data = Profile_Cust_Stbks.fillna(0)
print(Profile_Cust_Stbks.shape, clean_data.shape)

#import data
St_Cust_Portfolio = pd.read_csv("portfolio.csv")
print(St_Cust_Portfolio.head())

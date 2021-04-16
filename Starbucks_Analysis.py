import pandas as pd
import numpy as np

def import_csv(filename):
    data = pd.read_csv(filename)
    print(data)
    print(data.describe())
    print(data.columns)

CustProf=import_csv("profile.csv")

Cust_Port=import_csv("portfolio.csv")

Cust_Trpt=import_csv("transcript.csv")

StarbucksCSAT=import_csv("Starbucks satisfactory survey.csv")











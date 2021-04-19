import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def import_data(Filename) :
    data=pd.read_csv(Filename)
    print(data.head(20))
    print(data.columns)
    print(data.info)

Telco_Cust_Churn=pd.read_csv(r"Telco-Customer-Churn.csv")
print(Telco_Cust_Churn)

Slice=Telco_Cust_Churn.iloc[: , 18:21]
Slice.to_csv("SliceA.csv")
print(Slice)

Slice2=Telco_Cust_Churn.iloc[: , :2]
Slice2.to_csv("SliceB.csv")
print(Slice2)

Merged_data=pd.concat((Slice2, Slice), axis=1, join='inner')
print(Merged_data.head())

SliceA=pd.read_csv("SliceA.csv")
print(SliceA.head())
print(SliceA.columns)
SliceB=pd.read_csv("SliceB.csv")
print(SliceB.head())
print(SliceB.columns)

Concat=pd.concat([SliceB, SliceA], axis=1, join='inner')
print(Concat.head())


Slice3=Telco_Cust_Churn.iloc[: , :2]
Slice3.to_csv("Slice3.csv", index=False)
print(Slice3)
Slice4=Telco_Cust_Churn.iloc[: , 18:21]
Slice.to_csv("Slice4.csv", index=False)
print(Slice4)
New_df=pd.concat([Slice3, Slice4], ignore_index=True)
print(New_df.head(5))
print(New_df)

a= Telco_Cust_Churn[Telco_Cust_Churn["gender"].isin(["Female"])]
print(a)

#Female Customers Total is 3488

b=Telco_Cust_Churn[Telco_Cust_Churn["gender"].isin(["Male"])]
print(b)

#Male Customers Total is 3555

x=[3555, 3488]
labels=["Male", "Female"]
fig, ax= plt.subplots()
ax.pie(x, labels=labels, autopct='%.0f%%')
ax.set_title("Telco Customers")
plt.show()
plt.clf()


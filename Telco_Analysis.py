import pandas as pd
# Import the Telco data and insights
Telco_data2=pd.read_csv("Telco-Customer-Churn.csv", index_col = 0)
print(Telco_data2.describe)
print(Telco_data2.info)
print(Telco_data2.head())
# Drop rows with na
drop_rows=Telco_data2.dropna()
print(Telco_data2.shape, drop_rows.shape)
# Get Total Spend
TotalSpend=Telco_data2["TotalCharges"].sum()
print(TotalSpend)
# Get the breakdown of Gender and Churn
df=Telco_data2[["gender", "Churn"]]
print(df.head())
# Sort by Monthly Charges
sorted_df=Telco_data2.groupby(["MonthlyCharges"])
print(sorted_df.head(15))
# Show Churn
Churn=Telco_data2["Churn"]
print(Churn.head(15))

import pandas as pd
import matplotlib.pyplot as plt
# import Telco data as Pandas dataframe
Telco_data = pd.read_csv(r"Telco-Customer-Churn.csv")
print(Telco_data.head())
# Gather the data and form two independent dataframes
Df1 = Telco_data.iloc[:, 18:21]
Df1.to_csv("Sliced_Df1.csv")
print(Df1.head())
print(type(Df1))
Df2 = Telco_data.iloc[:, :2]
Df2.to_csv("Sliced_df2.csv")
print(Df2.head())
# Concatenate both dataframes into a new one called Merged_data
Merged_data = pd.concat((Df2, Df1), axis=1, join='inner')
print(Merged_data.head())
print(type(Merged_data))
# Find total Female customers
a = Telco_data[Telco_data["gender"].isin(["Female"])]
print(a)  # Result = Female Customers Total is 3488
# Find Total Male customers
b = Telco_data[Telco_data["gender"].isin(["Male"])]
print(b)  # Male Customers Total is 3555
# Visualise this data on a pie chart
x = [3555, 3488]
labels = ["Male", "Female"]
fig, ax = plt.subplots()
ax.pie(x, labels=labels, autopct='%.0f%%')
ax.set_title("Telco Customers")
plt.show()
plt.clf()
plt.close()

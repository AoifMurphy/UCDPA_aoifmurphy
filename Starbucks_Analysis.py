import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def import_csv(filename):
    data = pd.read_csv(filename)
    print(data)
    print(data.describe())
    print(data.columns)
    print(data.info)

CustProf=import_csv("profile.csv")

Cust_Port=import_csv("portfolio.csv")

Cust_Trpt=import_csv("transcript.csv")

StarbucksCSAT=import_csv("Starbucks satisfactory survey.csv")


print(type(StarbucksCSAT))

print(Cust_Port)

Service = {"One": [1], "Two": [4], "Three": [43], "Four": [51], "Five": [23]}

Satisf_Score_df = pd.DataFrame(data = Service)
print(Satisf_Score_df)

bargraph = sns.barplot(data = Satisf_Score_df)
bargraph.set(title = "How do you rate Service at Starbucks?", xlabel = "Score", ylabel ="No of Customers")
plt.savefig("bar2.png")
plt.show()
plt.clf()

data=[60, 62]
labels=["Yes", "No"]
fig, ax= plt.subplots()
ax.pie(data, labels=labels, autopct='%.0f%%')
ax.set_title("Starbucks Membership")
plt.show()
plt.clf()










import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#DEFINE FUNCTION.
def import_csv(filename):
    data=pd.read_csv(filename)
    print(data)
    print(data.columns)
    print(data.info)
StarbucksCSAT=import_csv("Starbucks satisfactory survey.csv")
# Create Dictionary from Q17 in CSAT and visualise
Service = {"One": [1], "Two": [4], "Three": [43], "Four": [51], "Five": [23]}
Satisf_Score_df=pd.DataFrame(data=Service)
print(Satisf_Score_df)
bargraph=sns.barplot(data=Satisf_Score_df)
bargraph.set(title="How do you rate Service at Starbucks?", xlabel="Score", ylabel="No of Customers")
plt.savefig("bar2.png")
plt.show()
plt.clf()
# Visualise Sample of Starbucks Membership and create pie chart
data=[60, 62]
labels=["Yes", "No"]
fig, ax= plt.subplots()
ax.pie(data, labels=labels, autopct='%.0f%%')
ax.set_title("Starbucks Membership")
plt.show()
plt.clf()
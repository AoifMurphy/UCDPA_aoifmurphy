import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# iterrows and use for loop
telco_data3 = pd.read_csv("Telco-Customer-Churn.csv")
for lab, row in telco_data3.iterrows():
    print(lab)
    print(row)
for lab, row in telco_data3.iterrows():
    print(row["PaymentMethod"])
# Group by method to call Payment methods
Payment_methods = telco_data3.groupby("PaymentMethod").size()
print(Payment_methods)

Payment_Types = {"Bank transfer": [1544], "Credit Card": [1522], "Electronic check": [2365], "Mailed check": [1612]}
print(Payment_Types)
# Create a bar plot to show payment methods
type = {"Bank transfer": [1544], "Credit Card": [1522], "Electronic check": [2365], "Mailed check": [1612]}
df6 = pd.DataFrame(data=type)
print(df6)

bargraph = sns.barplot(data=df6)
bargraph.set(title="Favored Payment Types",
xlabel="Payment Type", ylabel="Number of Customers")
plt.savefig("bar.png")
plt.show()
plt.clf()

# Create numpy array
a = np.array([1544, 1522, 2365, 1612])
print(a)
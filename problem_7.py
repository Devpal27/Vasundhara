								
'''Write a Python Program to Read 'Diesel', 'Petrol' of all months and display it using the Subplots'''	
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "months" : ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "petrol":[2000,2500,2200,2000,3000,2000,3200,3000,2900,3300,3400,3400],
    "diesel":[1500,1800,2000,2200,2500,2700,2600,3000,3200,3500,3600,3800]
}

df = pd.DataFrame(data)

# Create subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Petrol subplot
axes[0].plot(df["months"], df["petrol"], marker='o')
axes[0].set_title("Monthly Petrol Sales")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Petrol Sales")

# Diesel subplot
axes[1].plot(df["months"], df["diesel"], color='red', marker='o')
axes[1].set_title("Monthly Diesel Sales")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Diesel Sales")

plt.tight_layout()
plt.show()

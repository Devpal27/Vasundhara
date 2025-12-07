									
# '''Write a Python Program to Read 'Petrol' and 'CNG' FuelType sales data and show it using								
# the Heatmap. The bar chart should display the number of units sold per month for each								
# product. Add a separate bar for each product in the same chart								
# '''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (Aap CSV se bhi read kar sakte ho)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Petrol": [120, 150, 170, 160, 180, 200],
    "CNG": [80, 90, 100, 95, 110, 120]
}

df = pd.DataFrame(data)
df.set_index("Month", inplace=True)

# -------------------------
# 🔥 1) HEATMAP
# -------------------------
plt.figure(figsize=(8, 4))
sns.heatmap(df, annot=True, cmap="YlGnBu")
plt.title("Fuel Sales Heatmap")
plt.show()

# -------------------------
# 🔥 2) BAR CHART (Side-by-side Bars)
# -------------------------
plt.figure(figsize=(8, 4))

x = range(len(df))
width = 0.35

plt.bar([i - width/2 for i in x], df["Petrol"], width=width, label="Petrol")
plt.bar([i + width/2 for i in x], df["CNG"], width=width, label="CNG")

plt.xticks(x, df.index)
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Monthly Sales Comparison")
plt.legend()

plt.show()


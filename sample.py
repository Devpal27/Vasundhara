									
# '''Write a Python Program to Read 'Petrol' and 'CNG' FuelType sales data and show it using								
# the Heatmap. The bar chart should display the number of units sold per month for each								
# product. Add a separate bar for each product in the same chart								
# '''

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # ---------------------------
# # Sample Petrol & CNG Sales Data
# # ---------------------------
# data = {
#     "months": ["January", "February", "March", "April", "May", "June"],
#     "petrol": [10, 20, 15, 30, 25, 18],
#     "cng": [5, 10, 8, 14, 11, 9]
# }

# df = pd.DataFrame(data)

# # ---------------------------
# # 1️⃣ HEATMAP (Using Seaborn)
# # ---------------------------
# df_heatmap = df.set_index("months")   # months as index

# plt.figure(figsize=(8,5))
# sns.heatmap(df_heatmap, annot=True, cmap="coolwarm")
# plt.title("Monthly Petrol & CNG Sales Heatmap")
# plt.show()

# # ---------------------------
# # 2️⃣ BAR CHART (Side-by-side Bars)
# # ---------------------------

# x = range(len(df["months"]))
# width = 0.35  # bar width

# plt.figure(figsize=(10,5))

# plt.bar([i - width/2 for i in x], df["petrol"], width=width, label="Petrol")
# plt.bar([i + width/2 for i in x], df["cng"], width=width, label="CNG")

# plt.xticks(x, df["months"], rotation=45)
# plt.xlabel("Months")
# plt.ylabel("Units Sold")
# plt.title("Monthly Petrol & CNG Sales (Bar Chart)")
# plt.legend()
# plt.grid(axis='y')

# plt.show()

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


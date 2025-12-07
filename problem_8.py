"''Write a Python Program to Read all FuelType data and show it using the stack plot.''"		
import pandas as pd
import matplotlib.pyplot as plt

# Sample FuelType data
data = {
    'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 135, 150, 160, 170, 180],
    'Diesel': [100, 110, 120, 130, 140, 150],
    'CNG': [80, 90, 95, 100, 110, 120],
    'Electric': [10, 12, 15, 18, 20, 25]
}

# Create DataFrame
df = pd.DataFrame(data)

# Stack Plot
plt.figure(figsize=(8, 5))
plt.stackplot(df['months'],
              df['Petrol'],
              df['Diesel'],
              df['CNG'],
              df['Electric'],
              labels=['Petrol', 'Diesel', 'CNG', 'Electric'])

plt.title("FuelType Sales Stack Plot")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.legend(loc='upper left')
plt.show()
print("not by dev")
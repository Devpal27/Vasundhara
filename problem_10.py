									
'''Write a Python program to display a summary of the basic information about a specified								
DataFrame which is created by Toyota.csv and its data like index, columns, non null values of								
each column, memory usage etc								
'''

import pandas as pd

# Sample Toyota data (CSV ke bina)
data = {
    "Model": ["Corolla", "Camry", "Innova", "Fortuner"],
    "Year": [2018, 2019, 2020, 2017],
    "Price": [800000, 1200000, 1500000, 2800000],
    "FuelType": ["Petrol", "Diesel", "Diesel", "Petrol"],
    "Mileage": [18.0, 16.0, 12.5, 10.0]
}
df = pd.DataFrame(data)
df.to_csv("Toyota.csv", index=False)

print(df)
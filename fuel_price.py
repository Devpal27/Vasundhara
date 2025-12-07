import pandas as pd
import matplotlib.pyplot as plt

data = {
    "fuel_type" : ["petrol", "petrol", "petrol_premium", "diesel", "cng", "ethanol"],
    "price_per_liter" : [100, 100, 120, 80, 60, 50]
}
price = pd.DataFrame(data)
print(price)
total = price.groupby("fuel_type")["price_per_liter"].sum()

plt.plot(total.index, total.values,marker='o',color='red',linestyle ='--', linewidth =2, markersize =10,label='Fuel Price')
plt.title("Fuel Price per Liter")
plt.xlabel("fuel type")
plt.ylabel("price")
plt.legend(loc = 'upper right')
plt.grid(color = 'black')
plt.show()
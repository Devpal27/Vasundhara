'''Write a Python Program to Calculate total Price data for last year for each FuelType and								
show it using a Pie chart.								
'''
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "months" : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "petrol":[20000,30000,6000,500,900,1000,7000,16000,9000,31000,1000,27000],
    "petrol_premium" : [5000, 6000, 5500, 7000, 3000, 4000, 4500, 8000, 7500, 6500, 9000, 10000],
    "diesel":[9000,10000,1100,21000,6000,40000,30000,80000,20000,33000,4000,50000],
    "cng":[10000,30000,50000,70000,90000,12300,3333,500,1000,4000,70000,50000]

 
} 
price = pd.DataFrame(data)
print(price)
explode = (0.1, 0, 0, 0)
total =  [price["petrol"].sum(),
        price["petrol_premium"].sum(),
        price["diesel"].sum(),
        price["cng"].sum()]
plt.pie(total,labels=["petrol","petrol_premium","diesel","cng"],autopct='%1.1f%%', explode=explode ,wedgeprops={'edgecolor':'black'})
plt.title("quaterly fuel sales",size=20)
plt.show()
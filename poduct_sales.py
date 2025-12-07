import pandas as pd
import matplotlib.pyplot as plt
data = {
    "months" : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "petrol_sales":[20000,30000,6000,500,900,1000,7000,16000,9000,31000,1000,27000],
    "petrol_premium_sales" : [5000, 6000, 5500, 7000, 3000, 4000, 4500, 8000, 7500, 6500, 9000, 10000],
    "diesel":[9000,10000,1100,21000,6000,40000,30000,80000,20000,33000,4000,50000],
    "cng":[10000,30000,50000,70000,90000,12300,3333,500,1000,4000,70000,50000]

 
} 
price = pd.DataFrame(data)
print(price)

plt.plot( price["months"] , price["petrol_sales"],label= 'petrol sales', marker='o')
plt.plot(price["months"], price["petrol_premium_sales"],label = 'petrol premium sales', marker='o',linestyle= "--")
plt.plot(price["months"], price["diesel"],label = 'diesel sales', marker='o', linestyle= "--")
plt.plot(price["months"], price["cng"],label = 'cng sales', marker='o',linestyle= "--")


plt.legend(loc = "upper right")
plt.xticks(rotation = 45)
plt.grid(color = 'gray')
plt.title("Monthly fuel sales data", size=20)
plt.ylabel("total rupees sales",size=15)
plt.show()
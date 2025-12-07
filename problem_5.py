'''Write a Python Program to Read the total Price of each month and show it using 
histogram to see most common Price ranges'''
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "months":["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"],
    "total_price":[2900,2200,2200,2000,3000,2000,3000,3000,2900,3300,3400,2400]
}
price = pd.DataFrame(data)
print(price)
plt.hist(price["total_price"],bins = 6,edgecolor='black')
plt.xlabel("total price range")
plt.ylabel("number of months")
plt.show()
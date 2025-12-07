'''Write a Python Program to Read 'Petrol' sales data of each month and show it using a								
scatter plot Firstly, Insert a column Months in a DataFrame. Also, add a grid in the plot. gridline								
style should “–“						'''
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "months" : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "petrol_sales":[ 10,20,60,5,9,10,7,16,9,31,10,27]
}
price = pd.DataFrame(data)
print(price)
plt.scatter(price["months"],price["petrol_sales"],color = 'red',marker='o',label='petrol sales per litre')
plt.title("annual pertrol sales")
plt.legend(loc = "upper right")
plt.grid()
plt.xticks(rotation = 45)
plt.xlabel("months")
plt.ylabel("petrol sales in litre")
plt.show()
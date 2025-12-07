"''Write a Python Program to Read all FuelType data and show it using the stack plot.''"		
import pandas as pd
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [5, 6, 4, 5, 7]
y2 = [1, 6, 4, 5, 6]
y3 = [1, 1, 2, 3, 2]

# Creating the stack plot
plt.stackplot(x, y1, y2, y3)
plt.show()

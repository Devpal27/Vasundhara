'''Write a python program to for linear and multilinear regression'''			

import numpy as np
from sklearn.linear_model import LinearRegression

# Linear Regression (Single Feature)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(X, y)

print("=== Linear Regression ===")
print("Coefficient (Slope):", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for x = 6 :", model.predict([[6]]))

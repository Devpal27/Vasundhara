import numpy as np
from sklearn.linear_model import LinearRegression

# Multilinear Regression (Two Features)
X = np.array([
    [5, 20],
    [6, 25],
    [7, 30],
    [8, 35],
    [9, 40]
])
y = np.array([50, 60, 65, 70, 80])

model = LinearRegression()
model.fit(X, y)

print("=== Multilinear Regression ===")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for [10, 45] :", model.predict([[10, 45]]))

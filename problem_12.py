'''Write a Python program to select the rows where the 'FuelType' is missing, i.e. is NaN.								
Hint: print(df[df['FuelType'].isnull()])								
'''
import pandas as pd
import numpy as np
data ={ 
    "fuel_type" : ["petrol", np.nan, "petrol_premium", np.nan, "cng", "ethanol"],
    "price_per_liter" : [100, 100, 120, 80, 60, 50]
}
df = pd.DataFrame(data)
print(df[df['fuel_type'].isnull()])
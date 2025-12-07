'''Write a Python program to get the first 3 rows of a given DataFrame where data frame								
create by using dictionary. {'name': ['Dinesh', 'Suresh', 'Rahul', 'Ravi', 'Manoj', 'Hari', 'Yatharth',								
Saurabh', 'Kapil', 'Salini'], 'runs': [125, 129, 165, np.nan, 109, 120, 145, np.nan, 118, 119],								
attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']								
'''
import pandas as pd
import numpy as np
data = {'name': ['Dinesh', 'Suresh', 'Rahul', 'Ravi', 'Manoj', 'Hari', 'Yatharth',								
        'Saurabh', 'Kapil', 'Salini'],
        'runs': [125, 129, 165, np.nan, 109, 120, 145, np.nan, 118, 119],								
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']	
df = pd.DataFrame(data, index =  labels)
print(df.head(3))
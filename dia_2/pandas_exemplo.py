'''
https://pandas.pydata.org/pandas-docs/stable/10min.html
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/data/insurance.csv')

data.head()

data.tail(3)

data.index

data.columns

data.values

data.describe()

data.sort_values(by='age')

data['age']
data.age

data[10:14]

data.loc[10:14,['sex','age','smoker']]
data.at[10,'sex']

data.iloc[10:14,[1,0,4]]
data.iat[10,1]

data[(data.age < 21) & (data.children > 1) & (data.bmi < data.bmi.mean())]

data.children.value_counts()

data.groupby(['sex','smoker']).mean()

plt.figure(figsize=(12,12))
plt.scatter(data.age,data.charges,
            s=30*data.bmi,
            c=pd.factorize(data.sex)[0],
            alpha=0.5)




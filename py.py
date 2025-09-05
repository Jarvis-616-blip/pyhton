import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Series1 = pd.Series([2,3,4,5])
Series2 = pd.Series([2,8,5,6,])
print(Series1[0])
print(Series1[:3])

temp = Series1<8
print(temp)

a = len(Series1)
print(a)

Series1=Series2
print(Series2)
Series1.index =['A','B','C','D']
print(Series1)
print(Series2)
Series1 = Series2.copy()
print(Series2)
Series1.index =['A','B','C','D']
print(Series1)

def AddSeries(x,y):
    for i in range(x):
        print(x[i] + y[i])
    AddSeries(Series1,Series2)
    

plt.plot(Series2)  
plt.ylabel('index')
plt.show
    
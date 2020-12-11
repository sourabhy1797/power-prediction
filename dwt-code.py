import pandas as pd

import pywt

import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\yadavs\Documents\wavelet transform\series6.csv')

data1 = data['Average Energy Delivered']

cA, cD = pywt.dwt(data1, 'db2')

np.savetxt("GFG.csv",  
           cD, 
           delimiter =", ",  
           fmt ='% s')

plt.plot(cD, color= 'blue')
plt.title("Series-6")
plt.show()
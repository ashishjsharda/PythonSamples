'''
Created on Apr 9, 2017

@author: asharda
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("ign.csv")
print (data.head(5))
print(data.shape)
t=np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


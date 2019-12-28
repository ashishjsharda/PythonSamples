'''
Created on Dec 28, 2019
Array Iteration
@author: ashish
'''
import numpy as np
a=np.arange(0,60,5)
for x in np.nditer(a):
    print(x)

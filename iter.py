'''
Created on Aug 24, 2019
Using Iterator function in Numpy
@author: asharda
'''
import numpy as np
list=range(5)
it=iter(list)
x=np.fromiter(it,dtype=int)
print(x)

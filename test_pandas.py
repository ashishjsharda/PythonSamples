'''
Created on Apr 10, 2017

@author: asharda
'''
import numpy as np
import matplotlib as p
import pdb
from pandas import *
data=read_csv('train.csv')
#print(data)
print(data['Name'])
data.pclass.hist()
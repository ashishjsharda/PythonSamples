'''
Created on Sep 7, 2019

Matrix Multiplication using numpy
@author: asharda
'''
import numpy as np

def matrix_mul(a,b):
    mul=np.matmul(a,b)
    return mul


a=[[1,2],[3,4]]
b=[[4,5],[6,7]]
print(matrix_mul(a, b))

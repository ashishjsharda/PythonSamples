'''
Created on Jan 20, 2020
Using Callable Functions in Python
@author: ashish
'''
x=10
print(callable(x))

def testfunction():
    print("Test")

y=testfunction
print(callable(y))

'''
Created on Dec 22, 2019
Using Try/Except
@author: ashish
'''
try:
    x=int(input("Pls enter a number"))
    print(x)
    y=input("Please enter another number")
    print(y)
except Exception:
    print("Exception seen")

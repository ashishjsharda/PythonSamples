'''
Created on Jul 28, 2019
Using Classes
@author: asharda
'''

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("Name seen is ",self.name)
        print("Roll seen is",self.roll)

s=Student("Ashish",4)
s.display()    

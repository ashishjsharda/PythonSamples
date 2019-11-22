'''
Created on Nov 22, 2019
Using Classes
@author: asharda
'''
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print("Name of the student is ",self.name ," Roll No is ",self.rno)
        

s=Student("Ashish",4)
s.display()        

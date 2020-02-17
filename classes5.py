'''
Using Classes in Python
'''
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(" Student Name is " ,self.name ," Student Roll No is  ",self.rollno)

s=Student("Ram",20)
s.display()
n=Student("Jack",21)
n.display()

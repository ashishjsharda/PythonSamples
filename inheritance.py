'''
Inheritance in Python
@author: asharda
'''

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def display(self):
        print(self.fname)
        
        
        
class Male(Person):
    
    def __init__(self,gender,fname,lname):
        self.gender=gender
        self.fname=fname
        self.lname=lname
        super()
        
    def display(self):
        Person.display(self)
        print(self.gender)
p=Male('male','AJ','Alwar')
p.display()        
    

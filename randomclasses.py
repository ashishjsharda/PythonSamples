'''
Created on Nov 7, 2019
Using Classes 
@author: asharda
'''
class EmployeeCount:
    empcount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print("Name seen is ",self.name)
        print("Salary seen is ",self.salary)
        
e=EmployeeCount("Sai",40000)
e.display()

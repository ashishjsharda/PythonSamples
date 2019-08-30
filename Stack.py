'''
Created on Aug 30, 2019
Stack in Python
@author: asharda
'''

class Stack:
    
    #Initialize Stack
    def __init__(self):
        self.items=[]
        
    #Push items in Stack
    def push(self,data):
        self.items.insert(0, data)
        
    #Pop element from List
    def pop(self):
        return self.items.pop(0)
    
    #Check if stack is Empty
    def isEmpty(self):
        return self.items==[]
    
    #Display Stack Contents
    def display(self):
        for i in reversed(self.items):
            print(i)
       
        
        
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.display()

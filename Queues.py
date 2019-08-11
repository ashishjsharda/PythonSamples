'''
Created on Aug 11, 2019
Queues in Python
@author: asharda
'''
class Queue:
    def __init__(self):
        self.items=[]
    'Enqueue in Queue'
    def enqueue(self,item):
        self.items.insert(0, item)
    'Dequeue Operation'
    def dequeue(self):
        self.items.pop()
    'Get the Length of Queue'
    def getlength(self):
        return len(self.items)
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
print(q.getlength())
q.dequeue()
print(q.getlength())

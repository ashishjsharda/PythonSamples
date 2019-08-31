'''
Created on Aug 31, 2019
Try/Except /Finally
@author: asharda
'''

lists=[1,2,3,4,5]
try:
    print(lists)
    lists.clear()
    print(lists[0])
except Exception as e:
    print(e)
finally:
    print("In finally")

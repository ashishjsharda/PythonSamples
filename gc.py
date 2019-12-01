'''
Garbage Collection
@author: asharda
'''

import gc
print("Threshold seen is ",gc.get_threshold())
#Invoke GC
print(gc.collect())

'''
Created on Jul 31, 2019
Using Yield
@author: asharda
'''


def gen_nums():
    n=0
    while n<4:
        yield n
        n+=1

for num in gen_nums():
    print(num)

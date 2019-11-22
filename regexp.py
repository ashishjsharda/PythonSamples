'''
Created on Nov 22, 2019
Using Regular Expressions
@author: asharda
'''
import re

line="Cats are smarter than dogs"
matchObj=re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")

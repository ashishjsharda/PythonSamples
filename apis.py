'''
Created on Jul 28, 2019
Using API
@author: asharda
'''

import requests
response=requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
data=response.json()
print(data)
print(data['number'])

'''
Created on Sep 7, 2019

@author: asharda
'''
import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Go connection from addr",addr)
    c.send("Thank you for connecting")
    c.close()

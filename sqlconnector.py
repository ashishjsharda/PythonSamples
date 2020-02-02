"""
Using MySQL Connector
"""
import mysql.connector
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="username",
    password="password",
    auth_plugin='mysql_native_password'
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE employee")
mycursor.close()
#print(mydb)

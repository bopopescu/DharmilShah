# import pymsql.cursors

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")

if mydb:
    print('connection made successfully')


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="tabledata")

if mydb:
    print('connection made')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS tabledata")

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS student")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="student")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

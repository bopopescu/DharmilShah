import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS userinput")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="userinput")
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS userinputdata(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255  ))")

sql = "INSERT INTO userinputdata (name, address) VALUES(%s, %s)"

dataentry = int(input('how many times u want to nter the data :'))
for i in range(dataentry):
    n = input('enter the name : ')
    ad = input('enter the address : ')
    val = (n, ad)
    mycursor.execute(sql, val)
    mydb.commit()

print(dataentry, "record Inserted")

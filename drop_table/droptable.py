import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS userinput")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="userinput",buffered=True)
mycursor = mydb.cursor()

# mycursor.execute(
# "CREATE TABLE IF NOT EXISTS sample(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255  ))")
#
# sql = "INSERT INTO sample (name, address) VALUES(%s, %s)"
#
# dataentry = int(input('how many times u want to nter the data :'))
# for i in range(dataentry):
#     n = input('enter the name : ')
#     ad = input('enter the address : ')
#     val = (n, ad)
#     mycursor.execute(sql, val)
#     mydb.commit()
#
# print(dataentry, "record Inserted")
#
# mycursor.execute("SELECT * FROM sample")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

print('--------------------------------------------------')
print('Dropping Table Sample')
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS sample"
mycursor.execute(sql)
print('Table Dropped ')







import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS userinput")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="userinput",buffered=True)
mycursor = mydb.cursor()

# mycursor.execute(
# "CREATE TABLE IF NOT EXISTS updatedata(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255  ))")
#
# sql = "INSERT INTO updatedata (name, address) VALUES(%s, %s)"
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

mycursor.execute("SELECT * FROM updatedata")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = "UPDATE updatedata SET name = 'DHARMIL' WHERE name = 'dh3rmil' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, 'data updated')
print('---------------')
mycursor.execute("SELECT * FROM updatedata")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('-------------------------------------------------------------')
print('displaying only some row data using LIMIT function ')
mycursor.execute("SELECT * FROM updatedata LIMIT 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('-------------------------------------------------------------')
print('displaying only some row data starting from particular function using LIMIT function ')
mycursor.execute("SELECT * FROM updatedata LIMIT 3 OFFSET 1 ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)












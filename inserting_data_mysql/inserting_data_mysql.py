import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS insertdata")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="insertdata")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS insertt(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255  ))")

sql = "INSERT INTO insertt (name, address) VALUES(%s, %s)"
val = ("dharmil", "q3wer")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record Inserted")

sql ="INSERT INTO insertt(name, address) VALUES(%s, %s)"
val = [
    ("rj","pokn "),
    ("rtyhj", "wqsdfbg"),
    ("wqscv", "qsdf")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted")
import sqlite3
conn = sqlite3.connect("insert.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS insertdata(id INTEGER PRIMARY KEY NOT NULL, name TEXT, number REAl)")
data = int(input('how many data u want to add'))
for i in range(data):
    n = input('enter the name ')
    no = int(input('emter the number'))
    c.execute("INSERT INTO insertdata(name, number) VALUES(?, ? )", (n, no))
    print('data entered')
    conn.commit()
#c.execute("INSERT INTO insertdata(name, number) VALUES(?, ? )", (n, no))

c.close()
conn.close()



import sqlite3
conn = sqlite3.connect("readdata.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS readdata(id INTEGER PRIMARY KEY NOT NULL, name TEXT, number REAl)")
# data = int(input('how many data u want to add'))
#
# for i in range(data):
#     n = input('enter the name ')
#     no = int(input('emter the number'))
#     c.execute("INSERT INTO readdata(name, number) VALUES(?, ? )", (n, no))
#     print('data entered')
#     conn.commit()

print('')
print('fetching all data :')
c.execute('SELECT * FROM readdata ')
for row in c.fetchall():
    print(row)

print('')
print('fetching single column :')
c.execute('SELECT * FROM readdata ')
for row in c.fetchall():
    print(row[1])


c.close()
conn.close()



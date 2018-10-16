import sqlite3

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect("graphdata.db")
c = conn.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS graphdata(id INTEGER PRIMARY KEY NOT NULL, name TEXT, number REAl)")
# data = int(input('how many data u want to add'))
#
# for i in range(data):
#     n = input('enter the name ')
#     no = int(input('emter the number'))
#     c.execute("INSERT INTO graphdata(name, number) VALUES(?, ? )", (n, no))
#     print('data entered')
#     conn.commit()

# print('')
# print('fetching all data :')
# c.execute('SELECT * FROM graphdata ')
# for row in c.fetchall():
#     print(row)



# graph procedure

c.execute('SELECT * from graphdata')
name = []
id = []
number = []
for row in c.fetchall():
    name.append(row[1])
    id.append(row[0])
plt.plot(name, id, '-')
plt.show()

c.close()
conn.close()



import sqlite3

conn = sqlite3.connect("crud.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS crud(id INTEGER PRIMARY KEY NOT NULL, name TEXT, number REAl)")
data = int(input('how many data u want to add'))

for i in range(data):
    n = input('enter the name ')
    no = int(input('emter the number'))
    c.execute("INSERT INTO crud(name, number) VALUES(?, ? )", (n, no))
    print('data entered successfully ')
    conn.commit()

print('--------------------------------------------------------------------------------------------')
print('fetching all data :')
c.execute('SELECT * FROM crud ')
for row in c.fetchall():
    print(row)

print('--------------------------------------------------------------------------------------------')

n1 = input('enter the name for update')
num1 = int(input('enter the number you want to update'))
id_up = int(input('emter the id from above data you want to update'))

print('')

print('Data Updated syccessfully')
c.execute("UPDATE crud SET name = ?, number = ? where id = ? ", (n1, num1, id_up))
print('--------------------------------------------------------------------------------------------')

c.execute('SELECT * FROM crud')
for row in c.fetchall():
    print(row)

dele = input('enter the id you want to delete')
c.execute("DELETE FROM crud where id = ? ", (dele))
print('Data deleted successfully ')
print('--------------------------------------------------------------------------------------------')

c.execute('SELECT * FROM crud')
for row in c.fetchall():
    print(row)

conn.commit()




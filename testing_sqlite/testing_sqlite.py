import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

if c:
    print('database created')

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS demo(name TEXT, mno REAL, email TEXT)')

def data_entry():
    c.execute("INSERT INTO demo VALUES('xyz', 12345,'SADF')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()

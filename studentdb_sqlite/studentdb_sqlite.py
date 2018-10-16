import sqlite3

conn = sqlite3.connect('student.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY NOT NULL, name TEXT, rollno REAL, standard TEXT)')
c.execute("INSERT INTO student(name, rollno, standard) VALUES('dharmil',12,'9')")
c.execute("INSERT INTO student(name, rollno, standard) VALUES('raj',12,'9')")
c.execute("INSERT INTO student(name, rollno, standard) VALUES('rj',12,'9')")
conn.commit()
c.close()
conn.close()
import sqlite3

conn = sqlite3.connect('students.db')

conn.execute('CREATE TABLE users (name TEXT,mobile TEXT)')
print("Table created successfully")
conn.close()

import sqlite3

conn = sqlite3.connect('stddatabase.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE students (name TEXT NOT NULL, addr TEXT, city TEXT, zip TEXT)')
print("Created table successfully!")

conn.close()


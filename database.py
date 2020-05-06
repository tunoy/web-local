import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    username varchar(20) Primary key,
    password varchar(20),
    role varchar(20),
    donecodes varchar(100),
    doingcodes varchar(100),
    programming_languages varchar(100),
    email varchar(20)
)""")
cursor.close()

conn.commit()

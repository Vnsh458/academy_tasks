import sqlite3

# creating new database
connection = sqlite3.connect('my_db.db')
cursor = connection.cursor()

# creating new table in database
# cursor.execute(
#     '''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# '''
# )

'''#create index for column "email"
cursor.execute('CREATE INDEX idx_email ON Users (email)')'''

#Create new user

cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

connection.commit()
connection.close()


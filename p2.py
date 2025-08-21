import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINNCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

#cursor.execute('''
#    INSERT INTO users (username, password) VALUES (?, ?)
#''', ('Alice', 'password'))

conn.commit()

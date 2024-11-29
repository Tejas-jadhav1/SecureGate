import sqlite3

# Connect to SQLite database (will create SecureGate.db if it doesn't exist)
conn = sqlite3.connect('SecureGate.db')

# Create a cursor object
cur = conn.cursor()

# Create the SignUp table with username, mail, and password fields
cur.execute('''
    CREATE TABLE IF NOT EXISTS SignUp (
        username TEXT NOT NULL,
        mail TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        type TEXT NOT NULL DEFAULT 'Guard'
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS owner(
            flat_num primary key,
            mob_num TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            members TEXT
            )
            ''')


# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database 'SecureGate' and table 'SignUp' created successfully!")

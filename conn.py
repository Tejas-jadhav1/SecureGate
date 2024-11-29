import sqlite3


# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('SecureGate.db')
    return conn

# Function to initialize the database and create tables if they do not exist
def initialize_database():
    conn = create_connection()
    cur = conn.cursor()

    # Create the 'SignUp' table if it doesn't already exist
    cur.execute('''
    CREATE TABLE IF NOT EXISTS SignUp (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        mail TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        type TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def owner_database():
    conn = create_connection()
    cur = conn.cursor()
    print("call")
    cur.execute('''
        CREATE TABLE IF NOT EXISTS flat_owner(
        flat_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        mobile TEXT NOT NULL,
        member TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

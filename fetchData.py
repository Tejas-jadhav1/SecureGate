import sqlite3

# Connect to the existing SecureGate.db database
conn = sqlite3.connect('SecureGate.db')
cur = conn.cursor()

# Fixing the syntax error in your SELECT query to list tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()  # Get the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])  # Print each table name

# Example: Retrieve and print all users from the SignUp table
cur.execute("SELECT * FROM SignUp")  # Assuming SignUp is a valid table
rows = cur.fetchall()
print("\nSignUp Table Data:")
for row in rows:
    print(row)

# Close the connection
conn.close()

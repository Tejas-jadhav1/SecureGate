import sqlite3
import random
import string
from datetime import datetime, timedelta

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('SecureGate.db')
    return conn

# Function to generate random data for the visitor table
def generate_random_string(length=8):
    """Generates a random string of letters and digits of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_date(start_date, end_date):
    """Generates a random date between two given dates."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

def generate_random_time():
    """Generates a random time in 24-hour format (HH:MM)."""
    hour = random.randint(0, 23)  # Random hour between 0 and 23
    minute = random.randint(0, 59)  # Random minute between 0 and 59
    return f"{hour:02}:{minute:02}"  # Format as HH:MM

def generate_random_remark():
    """Randomly selects a remark from a predefined list."""
    remarks = ["friends", "relatives", "E-services"]
    return random.choice(remarks)

def insert_random_visitor_data():
    conn = create_connection()
    cur = conn.cursor()

    # Define the start and end date for random date generation
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)

    for _ in range(100):  # Insert 100 random rows
        name = generate_random_string(10)  # Random name
        tot_person = random.randint(1, 5)  # Total persons between 1 and 5
        date = generate_random_date(start_date, end_date)  # Random date
        mob_num = f"+91{random.randint(7000000000, 9999999999)}"  # Random mobile number
        time = generate_random_time()  # Random time in 24-hour format
        remark = generate_random_remark()  # Random remark (friends, relatives, E-services)
        flat_id = random.randint(1, 5)  # Flat ID between 1 and 5

        # Insert random visitor data into the database
        cur.execute('''
            INSERT INTO visitor (name, tot_person, date, mob_num, time, remark, flat_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, tot_person, date, mob_num, time, remark, flat_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_random_visitor_data()
    print("100 random entries have been inserted into the visitor table.")

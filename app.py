import sqlite3

# Connect to SQLite database or create it if it doesn't exist
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Clear previous queries from the Table
cursor.execute('DELETE FROM users')

# Insert a record
records = [
    ('Alice', 30), 
    ('Daniel', 27), 
    ('Kenny', 57), 
    ('Brock', 19), 
    ('Steve', 45), 
    ('Abby', 13),
    ('Jennifer', 72),
    ('Bob', 16),
    ('Robby', 38), 
    ('Anthony', 64),
    ('Dorris', 7),
]

cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", records)

# Commit the changes
conn.commit()

# Query the database
cursor.execute("SELECT count(*) FROM users where age > 21")

num_over_21 = cursor.fetchone()[0]
print(f"Number of users over 21: {num_over_21}")

cursor.execute("SELECT name, age FROM users where age > 21 and name not like '%y' order by age desc")

rows = cursor.fetchall()
print("Users over 21 with names that do not end in 'y':")
for name, age in rows:
    print(f"{name}, {age}")

# Close the connection
conn.close()
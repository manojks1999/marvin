import sqlite3
con = sqlite3.connect('application.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS history
               (id integer primary key,
                user_id integer not null,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                data text)''')

# Insert a few rows of data
cur.execute("INSERT INTO history(user_id, data) VALUES (900, 'Sample data')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

#Better to you sql scripts in another file
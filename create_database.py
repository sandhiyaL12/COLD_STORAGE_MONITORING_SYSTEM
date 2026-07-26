import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature_readings (
    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chamber_id TEXT NOT NULL,
    temperature_c REAL,
    door_state TEXT NOT NULL,
    alarm_flag TEXT NOT NULL,
    recorded_at TEXT NOT NULL
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("✅ Database and table created successfully!")

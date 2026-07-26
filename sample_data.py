import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Remove old data
cursor.execute("DELETE FROM temperature_readings")

# Reset auto-increment IDs
cursor.execute("DELETE FROM sqlite_sequence WHERE name='temperature_readings'")

conn.commit()

chambers = ["C001", "C002", "C003", "C004", "C005"]

start_time = datetime.now() - timedelta(minutes=39)

for i in range(40):

    chamber = random.choice(chambers)

    # Generate realistic temperature
    temperature = round(random.uniform(2.0, 8.0), 1)

    # Occasionally create high temperature (alarm)
    if random.random() < 0.15:
        temperature = round(random.uniform(9.0, 15.0), 1)

    # One missing sensor reading
    if i == 30:
        temperature = None

    door = random.choice(["Open", "Closed"])

    if temperature is None:
        alarm = "No"
    elif temperature > 8:
        alarm = "Yes"
    else:
        alarm = "No"

    recorded_at = (
        start_time + timedelta(minutes=i)
    ).strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO temperature_readings
    (
        chamber_id,
        temperature_c,
        door_state,
        alarm_flag,
        recorded_at
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        chamber,
        temperature,
        door,
        alarm,
        recorded_at
    ))

conn.commit()
conn.close()

print("✅ 40 sample records inserted successfully!")

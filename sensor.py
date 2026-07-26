import sqlite3
import random
import time
from datetime import datetime

DATABASE = "database.db"

SAFE_MIN = 2
SAFE_MAX = 8

previous_temperature = 5.0


def save_reading(chamber_id, temperature, door_state, alarm):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

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
        chamber_id,
        temperature,
        door_state,
        alarm,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


print("Cold Storage Sensor Started...")
print("------------------------------------")

while True:

    # Generate random temperature
    temperature = round(random.uniform(-5, 15), 1)

    # Random door status
    door_state = random.choice(["Open", "Closed"])

    # Reject impossible values
    if temperature < -20 or temperature > 60:
        print("Invalid Reading Rejected")
        continue

    # Smooth sudden spikes
    temperature = round((previous_temperature + temperature) / 2, 1)
    previous_temperature = temperature

    # Alarm Logic
    if temperature > SAFE_MAX:
        alarm = "Yes"
    else:
        alarm = "No"

    # Save to database
    save_reading("C001", temperature, door_state, alarm)

    print("------------------------------------")
    print("Time :", datetime.now().strftime("%H:%M:%S"))
    print("Temperature :", temperature, "°C")
    print("Door :", door_state)
    print("Alarm :", alarm)

    if alarm == "Yes":
        print("WARNING! Temperature Above Safe Limit")

    print("------------------------------------")

    # Wait 5 seconds
    time.sleep(5)

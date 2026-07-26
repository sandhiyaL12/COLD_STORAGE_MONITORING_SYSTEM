from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "database.db"


# ---------------------------------
# Database Connection
# ---------------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------
# Home Page
# ---------------------------------
@app.route("/")
def index():

    search = request.args.get("search", "")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Search
    if search:

        cursor.execute("""
        SELECT *
        FROM temperature_readings
        WHERE chamber_id LIKE ?
        ORDER BY reading_id ASC
        """, ('%' + search + '%',))

    else:

        cursor.execute("""
        SELECT *
        FROM temperature_readings
        ORDER BY reading_id ASC
        """)

    readings = cursor.fetchall()

    # Dashboard Cards

    cursor.execute("""
    SELECT COUNT(*)
    FROM temperature_readings
    """)
    total = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM temperature_readings
    WHERE alarm_flag='Yes'
    """)
    alarms = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM temperature_readings
    WHERE alarm_flag='No'
    """)
    safe = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        readings=readings,
        total=total,
        alarms=alarms,
        safe=safe,
        search=search
    )


# ---------------------------------
# Add Reading
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        chamber_id = request.form["chamber_id"]

        temp = request.form["temperature"]

        door_state = request.form["door_state"]

        # Alarm Logic
        if temp == "":
            temperature = None
            alarm = "No"
        else:
            temperature = float(temp)

            if temperature > 8:
                alarm = "Yes"
            else:
                alarm = "No"

        recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = get_db_connection()
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
            recorded_at
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


# ---------------------------------
# Delete Reading
# ---------------------------------
@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM temperature_readings
    WHERE reading_id=?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect("/")


# ---------------------------------
# Run Flask
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)

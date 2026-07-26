# 🧊 Cold Storage Monitoring System

## 📌 Project Overview

The Cold Storage Monitoring System is a web-based application developed using Python Flask and SQLite to monitor temperature conditions inside cold storage chambers.

The system records temperature readings, chamber information, door status, and alarm conditions. It provides a simple dashboard for monitoring storage conditions in real time. This project can also be integrated with IoT hardware such as ESP32 and DS18B20 temperature sensors.

---

## 🚀 Features

- Temperature Monitoring
- Multiple Chamber Support
- Door Status Monitoring
- Temperature Alarm Detection
- Add New Temperature Reading
- Delete Reading
- SQLite Database Storage
- Responsive Dashboard
- IoT Ready (ESP32 Integration)

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite3
- HTML5
- CSS3
- Jinja2

---

## 📂 Project Structure

```
Cold_Storage_Monitoring_System/
│
├── app.py
├── database.db
├── create_database.py
├── sample_data.py
├── sensor.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── add.html
│
└── static/
    └── style.css
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/COLD_STORAGE_MONITORING_SYSTEM.git
```

Go to project folder

```bash
cd COLD_STORAGE_MONITORING_SYSTEM
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Create Database

```bash
python create_database.py
```

Insert Sample Data

```bash
python sample_data.py
```

Run Application

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

## 📊 Dashboard Features

- Total Readings
- Safe Readings
- Alarm Readings
- Chamber ID
- Temperature
- Door Status
- Alarm Status
- Timestamp

---

## 🔔 Alarm Logic

| Temperature | Alarm |
|-------------|-------|
| 2°C – 8°C | Safe |
| Above 8°C | Alarm |

---

## 🔌 Future Improvements

- ESP32 Integration
- DS18B20 Temperature Sensor
- Buzzer Alert
- Email Notification
- SMS Notification
- Live Temperature Graph
- Cloud Database

---

## 👩‍💻 Developed By

**Sandhiya L**

Electronics and Communication Engineering

Prince Shri Venkateshwara Padmavathy Engineering College

---

## 📄 License

This project is developed for educational purposes.

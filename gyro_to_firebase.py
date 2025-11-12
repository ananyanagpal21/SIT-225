import serial
import json
import time
import firebase_admin
from firebase_admin import credentials, db

# Firebase Setup
cred = credentials.Certificate(r"data-capture-473bd-firebase-adminsdk-fbsvc-6db523a2ec.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-capture-473bd-default-rtdb.firebaseio.com'
})

# Serial Communication Setup (update if different)
ser = serial.Serial('/dev/tty.usbmodem11101', 115200, timeout=1)
print(f"Connected to: {ser.port}")
print("Streaming data to Firebase... (Press Ctrl+C to stop)")

# Firebase Upload Loop
try:
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) != 4:
            continue

        try:
            timestamp = int(parts[0])
            x, y, z = map(float, parts[1:])
        except ValueError:
            continue 

        data = {
            "timestamp": timestamp,
            "x": x,
            "y": y,
            "z": z
        }

        ref = db.reference("/gyroscope_data")
        ref.push(data)
        print(f"Uploaded: {data}")

except KeyboardInterrupt:
    print("Data collection stopped.")
    ser.close()

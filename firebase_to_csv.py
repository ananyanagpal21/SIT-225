import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

# Firebase Setup
cred = credentials.Certificate(r"data-capture-473bd-firebase-adminsdk-fbsvc-6db523a2ec.json")  
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-capture-473bd-default-rtdb.firebaseio.com/' 
})

# Fetch Data from Firebase
ref = db.reference("/gyroscope_data")
data = ref.get()

if data:
    records = [{"timestamp": v["timestamp"], "x": v["x"], "y": v["y"], "z": v["z"]} for v in data.values()]
    df = pd.DataFrame(records)
    df.to_csv("gyroscope_data.csv", index=False)
    print("Data saved to gyroscope_data.csv")
else:
    print("No data found in Firebase.")
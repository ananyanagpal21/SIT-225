import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("week3_data.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert data columns to numbers
df['temperature'] = pd.to_numeric(df['temperature'])
df['humidity'] = pd.to_numeric(df['humidity'])

# Temperature plot
plt.figure(figsize=(10,4))
plt.plot(df['timestamp'], df['temperature'])
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Humidity plot
plt.figure(figsize=(10,4))
plt.plot(df['timestamp'], df['humidity'])
plt.title("Humidity Over Time")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.show()

# Combined plot
plt.figure(figsize=(10,4))
plt.plot(df['timestamp'], df['temperature'], label="Temperature")
plt.plot(df['timestamp'], df['humidity'], label="Humidity")
plt.title("Temperature & Humidity Over Time")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()

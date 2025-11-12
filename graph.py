import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("gyroscope_data.csv")

# Convert timestamps to seconds
df["timestamp"] = (df["timestamp"] - df["timestamp"].min()) / 1000  

# Plot individual x, y, z graphs
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(df["timestamp"], df["x"], label="X-axis", color='r')
plt.xlabel("Time (s)")
plt.ylabel("X (°/s)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df["timestamp"], df["y"], label="Y-axis", color='g')
plt.xlabel("Time (s)")
plt.ylabel("Y (°/s)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df["timestamp"], df["z"], label="Z-axis", color='b')
plt.xlabel("Time (s)")
plt.ylabel("Z (°/s)")
plt.legend()

plt.tight_layout()
plt.show()

# Combined plot
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["x"], label="X-axis", color='r')
plt.plot(df["timestamp"], df["y"], label="Y-axis", color='g')
plt.plot(df["timestamp"], df["z"], label="Z-axis", color='b')
plt.xlabel("Time (s)")
plt.ylabel("Gyroscope Readings (°/s)")
plt.legend()
plt.title("Gyroscope Data (X, Y, Z)")
plt.show()

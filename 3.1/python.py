import serial
from datetime import datetime
import time

port = '/dev/cu.usbmodem11201'   
baud = 9600
filename = "week3_data.csv"

ser = serial.Serial(port, baud)
time.sleep(2)  # wait for Arduino to reset

# Open file and write header
file = open(filename, "w")
file.write("timestamp,temperature,humidity\n")

print("Collecting data for 10 minutes...")

start_time = time.time()
while time.time() - start_time < 10 * 60:  # 10 minutes
    data = ser.readline().decode().strip()
    if data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp},{data}\n")
        print(timestamp, data)

file.close()
ser.close()
print("Done! File saved as", filename)


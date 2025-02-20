import serial
import datetime

now = datetime.datetime.now()
ser = serial.Serial('COM4', 115200)

while True:
    temp = ser.readline().decode().strip()
    print(f"Received signal {temp}")
    print(now.year, now.month, now.day, now.hour)
    #if (int(temp) > 0):
    #    print("got a signal")

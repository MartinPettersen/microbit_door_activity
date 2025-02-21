import serial
import datetime
import json

now = datetime.datetime.now()
ser = serial.Serial('COM4', 115200)

with open("activity_data.json", "r") as file:
    data = json.load(file)
    if not isinstance(data, list):
        data = []

def add_activity (date):
    print(date)
    data.append(date)
    with open("activity_data.json", "w") as file:
        json.dump(data, file, indent=4)


while True:
    temp = ser.readline().decode().strip()
    print(f"Received signal {temp}")
    #print(now.year, now.month, now.day, now.hour)
    add_activity(
        {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour
        }
    )
    #if (int(temp) > 0):
    #    print("got a signal")

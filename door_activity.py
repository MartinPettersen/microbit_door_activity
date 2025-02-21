import serial
import datetime
import json
import tkinter as tk
import threading
import time

ser = serial.Serial('COM4', 115200, timeout=1)

with open("activity_data.json", "r") as file:
    data = json.load(file)
    if not isinstance(data, list):
        data = []

def add_activity (date):
    print(date)
    data.append(date)
    with open("activity_data.json", "w") as file:
        json.dump(data, file, indent=4)

def read_serial():
    while True:
        temp = ser.readline().decode().strip()
        if temp: 
            now = datetime.datetime.now()
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
            window.event_generate("new data", when="tail")
        
        time.sleep(0.1)
        #window.after(100, read_serial)
    #if (int(temp) > 0):
    #    print("got a signal")

def on_new_data(event):
    if data:
        last_activity = data[-1]
        label.config(text=f"new signal : {last_activity.get('signal')}")

window = tk.Tk()

window.title("Dør aktivitet")

label = tk.Label(window, text="Aktivitet i døra")
label.pack()

#window.after(100, read_serial)

window.bind("new data", on_new_data)

thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

window.mainloop()



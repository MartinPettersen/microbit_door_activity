import serial
import datetime
import json
import tkinter as tk
import threading
import time

ser = serial.Serial('COM4', 115200, timeout=1)
now = datetime.datetime.now()

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

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
win_width = 700
win_height = 200

x = width_screen - win_width - 10
y = height_screen - win_height - 10

window.geometry(f"{win_width}x{win_height}+{x}+{y}")

window.title("Dør aktivitet")


label = tk.Label(window, text=f"Aktivitet i døra {now.day}.{now.month}.{now.year}")
#label.pack()
label.grid(row=0, column=1, padx=5, pady=5)

button_left = tk.Button(
    text="<",
    width=1,
    height=1,
    bg="skyblue",
    fg="white"
)
#button_left.pack()
button_left.grid(row=1, column=0, padx=5, pady=5)


activity_container = tk.Frame(window, bg="aliceblue")
activity_container.grid(row=1, column=1, padx=4, pady=4)


for hour in range(24):
    blueSquare = tk.Frame(activity_container, bg="skyblue",width=6,height=15, relief="solid")
    blueSquare.grid(row=0, column=hour, padx=5, pady=5)
    blueSquare.grid_propagate(False)

    hourLabel = tk.Label(activity_container, text=f"{hour}")
    hourLabel.grid(row=1, column=hour, padx=5, pady=5)

button_right = tk.Button(
    text=">",
    width=1,
    height=1,
    bg="skyblue",
    fg="white"
)

#button_right.pack()
button_right.grid(row=1, column=2, padx=5, pady=5)

#window.after(100, read_serial)

window.bind("new data", on_new_data)

thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

window.mainloop()



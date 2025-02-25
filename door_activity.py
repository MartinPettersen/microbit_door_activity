import serial
import datetime
import json
import tkinter as tk
import threading
import time

ser = serial.Serial('COM4', 115200, timeout=1)
now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day

daily_activity_data = []

with open("activity_data.json", "r") as file:
    data = json.load(file)
    if not isinstance(data, list):
        data = []

def add_activity (date):
    data.append(date)
    with open("activity_data.json", "w") as file:
        json.dump(data, file, indent=4)

def read_serial():
    while True:
        temp = ser.readline().decode().strip()
        if temp: 
            add_activity(
                {
                    "year": now.year,
                    "month": now.month,
                    "day": now.day,
                    "hour": now.hour
                }
            )
            window.event_generate("<<NewData>>", when="tail")
        
        time.sleep(0.1)


def on_new_data(event):
    update_display()
    if data:
        last_activity = data[-1]

def get_activity_day():
    result = list(filter(lambda x: (x["day"] == now.day and x["month"] == now.month and x["year"] == now.year), data))
    return len(result)


def get_activity_hour(hour):
    result = list(filter(lambda x: (x["hour"] == hour and x["day"] == now.day and x["month"] == now.month and x["year"] == now.year), data))
    return len(result)


window = tk.Tk()

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
win_width = 700
win_height = 240

x = width_screen - win_width - 10
y = height_screen - win_height - 10

window.geometry(f"{win_width}x{win_height}+{x}+{y}")

window.title("Dør aktivitet")
label = tk.Label(window, text=f"Aktivitet i døra {now.day}.{now.month}.{now.year}")

def init_display():
    label.grid(row=0, column=1, padx=5, pady=5)

    button_left = tk.Button(
        text="<",
        width=1,
        height=1,
        bg="skyblue",
        fg="white",
        command=yesterday
    )
    button_left.grid(row=1, column=0, padx=5, pady=5, 
        )


    activity_container = tk.Frame(window, bg="aliceblue")
    activity_container.grid(row=1, column=1, padx=4, pady=4)


    allActivityDay = get_activity_day()

    for hour in range(24):
        activity_in_hour = get_activity_hour(hour)
        if (allActivityDay != 0):   
            blueSquare = tk.Frame(activity_container, bg="skyblue",width=6,height=(activity_in_hour *( 100 / allActivityDay)), relief="solid")
        else:
            blueSquare = tk.Frame(activity_container, bg="skyblue",width=6,height=0, relief="solid")
        
        daily_activity_data.append(blueSquare)
        blueSquare.grid(row=0, column=hour, padx=5, pady=5, sticky="s")
        blueSquare.grid_propagate(False)

        hourLabel = tk.Label(activity_container, text=f"{hour}")
        hourLabel.grid(row=1, column=hour, padx=5, pady=5)

    button_right = tk.Button(
        text=">",
        width=1,
        height=1,
        bg="skyblue",
        fg="white",
        command=next_day
    )

    button_right.grid(row=1, column=2, padx=5, pady=5)

window.bind("<<NewData>>", on_new_data)

def update_display():
    allActivityDay = get_activity_day()
        
    for i, square in enumerate(daily_activity_data):
        
        activity_in_hour = get_activity_hour(i)
        if (allActivityDay != 0):   
            square.config( bg="skyblue",width=6,height=(activity_in_hour *( 100 / allActivityDay)), relief="solid")
        else:
            square.config( bg="skyblue",width=6,height=0, relief="solid")
        
        

def yesterday():
    global now 
    now = now - datetime.timedelta(days=1)
    label.config(text=f"Aktivitet i døra {now.day}.{now.month}.{now.year}")
    update_display()

def next_day():
    global now 
    now = now + datetime.timedelta(days=1)
    label.config(text=f"Aktivitet i døra {now.day}.{now.month}.{now.year}")
    update_display()


init_display()
        

thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

window.mainloop()



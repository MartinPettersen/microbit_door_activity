# Micro:bit Door Activity Project

This project utilizes **micro:bits** to monitor door activity. It requires at least **two micro:bits**, with the option to add relay micro:bits if the distance between the sender and receiver is too great.

## Requirements
### Hardware:
- **1x Micro:bit (Sender)** – Attached to the door, detecting movement using its accelerometer.
- **1x Micro:bit (Receiver)** – Connected to a computer via USB.
- **1x Computer** – Runs the `door_activity.py` script.
- **(Optional) Relay Micro:bits** – Extend signal range if needed.

### Software:
- Micro:bit firmware (`.hex` files) for sender, receiver, and optional relay.
- Python script (`door_activity.py`) to process received data.

## Setup Instructions
1. **Flash the Sender Micro:bit**
   - Flash a micro:bit with the **Sender Code** (`Wireless door activity sender.hex` file in `microbit_code/` folder).
   - Attach it to the door.
   - Place it so that movement triggers the accelerometer.
   - Default movement sensitivity is **60**, but this can be adjusted in the code.

2. **Flash the Receiver Micro:bit**
   - Connect a second micro:bit to your computer via USB.
   - Flash it with the **Receiver Code** (`Wireless door activity receiver.hex` file in `microbit_code/` folder).

3. **Run the Python Script**
   - Ensure the receiver micro:bit is connected.
   - Run `door_activity.py` on your computer to receive and process signals.

4. **(Optional) Add Relay Micro:bits**
   - If the sender and receiver are too far apart, flash additional micro:bits with **Relay Code** to extend the signal range (`Wireless door monitor relay.hex` file in `microbit_code/` folder).

## Files in `microbit_code/`
- `.hex` files for **Sender, Receiver, and Relay** micro:bits.
- A text document with the source code for each `.hex` file.

---
This setup allows for real-time monitoring of door activity using micro:bits.

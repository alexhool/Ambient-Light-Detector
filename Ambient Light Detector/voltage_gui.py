# Non-standard imports found in requirements.txt
import os
import time
import tkinter as tk
import serial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Function to turn the LED on
def led_on():
    onLED.configure(state="disabled", bg="#D3D3D3")
    ser.write(bytes("H", "UTF-8"))
    ser.flush()
    offLED.configure(state="normal", bg="#f0f6f7")


# Function to turn the LED off
def led_off():
    offLED.configure(state="disabled", bg="#D3D3D3")
    ser.write(bytes("L", "UTF-8"))
    ser.flush()
    onLED.configure(state="normal", bg="#f0f6f7")


# Function to turn serial connection on
def serial_on():
    onSer.configure(state="disabled", bg="#D3D3D3")
    rect[0].set_visible(True)
    ser.open()
    time.sleep(1.27)
    onLED.configure(state="normal", bg="#f0f6f7")
    offSer.configure(state="normal", bg="#f0f6f7")


# Function to turn serial connection off
def serial_off():
    offSer.configure(state="disabled", bg="#D3D3D3")
    led_off()
    onLED.configure(state="disabled", bg="#D3D3D3")
    ser.close()
    rect[0].set_visible(False)
    text.set_text("Serial Connection Off")
    text.set_y(2.8)
    canvas.draw()
    onSer.configure(state="normal", bg="#f0f6f7")


# Function to update the bar graph
def update(height):
    ax.margins(0.5, 0)
    ax.set_ylim(0, 5.4)
    ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    ax.set_title("Ambient Light", size=16, pad=25, weight="bold")
    ax.set_ylabel("Voltage (V)", size=14, labelpad=10)
    rect[0].set_height(height)
    text.set_text(f"{height:.3f} V")
    text.set_y(height + 0.08)
    canvas.draw()


# Function to quit the program
def exit_gui():
    if not ser.is_open:
        ser.open()
    led_off()
    os._exit(0)


# Initialize serial connection
ser = serial.Serial(port="COM3", baudrate=9600, timeout=0)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Ambient Light Graph")
icon = tk.PhotoImage(file="light-bulb.png")
root.iconphoto(True, icon)
root.geometry("543x625")
root.resizable(False, False)
root.config(bg="#fdefc3")

# Set up the plot
fig = Figure(figsize=(4, 6), facecolor="#fdefc3")
fig.subplots_adjust(
    top=0.865, bottom=0.115, left=0.215, right=0.85, hspace=0.2, wspace=0.2
)
ax = fig.add_subplot(1, 1, 1)
ax.set_facecolor("#fefdf9")
ax.tick_params(axis="x", bottom=False, labelsize=14, pad=10)
ax.tick_params(axis="y", left=True, labelsize=12, pad=2)
rect = ax.bar(
    x="Brightness",
    height=0,
    color="#fcd768",
    edgecolor="#000000",
    linewidth=0.5,
    width=2,
    align="center",
)
text = ax.text(0, 0, "", ha="center", va="bottom")

# Add the plot to the Tkinter widget
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().config(bg="#000000")
canvas.get_tk_widget().grid(
    column=0, row=0, rowspan=15, sticky=tk.NSEW, padx=10, pady=10, ipadx=5, ipady=2
)

# Add Serial Connection label
labelSer = tk.Label(
    root,
    text="Serial Connection",
    font=("DejaVu Sans", 15),
    bg="#fdefc3",
    wraplength=110,
    justify="center",
)
labelSer.grid(column=1, row=2, padx=0, pady=0, sticky=tk.SW)

# Add the Serial On button
onSer = tk.Button(
    root,
    text="On",
    width=10,
    height=1,
    font=("DejaVu Sans", 9),
    bg="#D3D3D3",
    state="disabled",
    command=serial_on,
)
onSer.grid(column=1, row=3, padx=12, pady=10, sticky=tk.NW)

# Add the Serial Off button
offSer = tk.Button(
    root,
    text="Off",
    width=10,
    height=1,
    font=("DejaVu Sans", 9),
    bg="#fefdf9",
    state="normal",
    command=serial_off,
)
offSer.grid(column=1, row=3, padx=12, pady=38, sticky=tk.NW)

# Add LED Visualizer label
labelLED = tk.Label(
    root,
    text="LED Visualizer",
    font=("DejaVu Sans", 15),
    bg="#fdefc3",
    wraplength=100,
    justify="center",
)
labelLED.grid(column=1, row=4, padx=8, pady=0, sticky=tk.SW)

# Add the LED On button
onLED = tk.Button(
    root,
    text="On",
    width=10,
    height=1,
    font=("DejaVu Sans", 9),
    bg="#fefdf9",
    state="normal",
    command=led_on,
)
onLED.grid(column=1, row=5, padx=12, pady=10, sticky=tk.NW)

# Add the LED Off button
offLED = tk.Button(
    root,
    text="Off",
    width=10,
    height=1,
    font=("DejaVu Sans", 9),
    bg="#D3D3D3",
    state="disabled",
    command=led_off,
)
offLED.grid(column=1, row=5, padx=12, pady=38, sticky=tk.NW)

# Add the quit button
quitB = tk.Button(
    root,
    text="QUIT",
    width=10,
    height=2,
    font=("DejaVu Sans", 9),
    bg="#fefdf9",
    activebackground="#de282c",
    activeforeground="#fefdf9",
    command=exit_gui,
)
quitB.grid(column=1, row=14, padx=12, pady=8, sticky=tk.W)
root.protocol("WM_DELETE_WINDOW", exit_gui)

# Read serial data and update the bar graph
lst = []
while True:
    while "|" not in lst and ser.is_open:
        try:
            data = ser.read().decode().strip()
            if data:
                lst.append(data)
        except ValueError:
            pass
    if lst:
        lst.pop()
    try:
        VOLTAGE = int("".join(lst)) * (4.963 / 1023.0)
        update(VOLTAGE)
    except ValueError:
        pass
    lst.clear()
    root.update_idletasks()
    root.update()

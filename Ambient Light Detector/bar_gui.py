import os
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import serial
import time

# Function to turn the LED on
def ledOn():
    onLED.configure(state="disabled", bg='#D3D3D3')
    ser.write(bytes('H', 'UTF-8'))
    ser.flush()
    offLED.configure(state="normal", bg='#f0f6f7')

# Function to turn the LED off
def ledOff():
    offLED.configure(state="disabled", bg='#D3D3D3')
    ser.write(bytes('L', 'UTF-8'))
    ser.flush()
    onLED.configure(state="normal", bg='#f0f6f7')

# Function to turn data collection on
def dataOn():
    onData.configure(state="disabled", bg='#D3D3D3')
    ser.open()
    offData.configure(state="normal", bg='#f0f6f7')

# Function to turn data collection off
def dataOff():
    offData.configure(state="disabled", bg='#D3D3D3')
    ser.close()
    bar[0].set_height(0)
    text.set_text("Data Collection Off")
    text.set_y(2.8)
    canvas.draw()
    onData.configure(state="normal", bg='#f0f6f7')
    
# Function to update the bar graph
def update(voltage):
    ax.margins(0.5, 0) 
    ax.set_ylim(0, 5.4)
    ax.set_yticks(np.arange(0, 5.5, 0.5))
    ax.set_title("Ambient Light", size=16, pad=25, weight='bold')
    ax.set_ylabel("Voltage (V)", size=14, labelpad=10)
    bar[0].set_height(voltage)
    text.set_text('{:.3f} V'.format(voltage))
    text.set_y(voltage + 0.08)
    canvas.draw()

# Function to quit the program
def exit():
    if not ser.is_open:
        ser.open()
    ledOff()
    os._exit(0)

# Initialize serial connection
ser = serial.Serial(port='COM3', baudrate=115200, timeout=0)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Ambient Light Graph")
root.geometry('540x625')
root.resizable(False, False)
root.config(bg='#e4f2f5')

# Set up the plot
fig = Figure(figsize=(4, 6), facecolor='#e4f2f5')
fig.subplots_adjust(top=0.865, bottom=0.115, left=0.215, right=0.85, hspace=0.2, wspace=0.2)
ax = fig.add_subplot(1,1,1)
ax.set_facecolor('#f0f6f7')
ax.tick_params(axis='x', bottom=False, labelsize=14, pad=10)
ax.tick_params(axis='y', left=True, labelsize=12, pad=2)
bar = ax.bar("Brightness", 0, color='#a1c9f4', linewidth=0, width=2, align="center")
text = ax.text(0, 0, '', ha='center', va='bottom')

# Add the plot to the Tkinter widget
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().config(bg='black')
canvas.get_tk_widget().grid(column=0, row=0, rowspan=15, sticky=tk.NSEW, padx=10, pady=10, ipadx=5, ipady=2)

# Add Data Collection label
labelData = tk.Label(root, text="Data Collection:", font=("DejaVu Sans", 15), bg='#e4f2f5', wraplength=100, justify="center")
labelData.grid(column=1, row=2, padx=4, pady=0, sticky=tk.SW)

# Add the Data On button
onData = tk.Button(root, text="On", width=10, height=1, font=("DejaVu Sans", 9), bg='#D3D3D3', state="disabled", command=dataOn)
onData.grid(column=1, row=3, padx=10, pady=10, sticky=tk.NW)

# Add the Data Off button
offData = tk.Button(root, text="Off", width=10, height=1, font=("DejaVu Sans", 9), bg='#f0f6f7', state="normal", command=dataOff)
offData.grid(column=1, row=3, padx=10, pady=38, sticky=tk.NW)

# Add LED Visualizer label
labelLED = tk.Label(root, text="LED Visualizer:", font=("DejaVu Sans", 15), bg='#e4f2f5', wraplength=100, justify="center")
labelLED.grid(column=1, row=4, padx=4, pady=0, sticky=tk.SW)

# Add the LED On button
onLED = tk.Button(root, text="On", width=10, height=1, font=("DejaVu Sans", 9), bg='#f0f6f7', state="normal", command=ledOn)
onLED.grid(column=1, row=5, padx=10, pady=10, sticky=tk.NW)

# Add the LED Off button
offLED = tk.Button(root, text="Off", width=10, height=1, font=("DejaVu Sans", 9), bg='#D3D3D3', state="disabled", command=ledOff)
offLED.grid(column=1, row=5, padx=10, pady=38, sticky=tk.NW)

# Add the quit button
quitB = tk.Button(root, text="QUIT", width=10, height=2, font=("DejaVu Sans", 9), bg='#f0f6f7',
                activebackground='#de282c', activeforeground='#f0f6f7', command=exit)
quitB.grid(column=1, row=14, padx=10, pady=5, sticky=tk.W)
root.protocol("WM_DELETE_WINDOW", exit)

# Read serial data and update the bar graph
list = []
time.sleep(1.25)
while True:
    while ('|' not in list and ser.is_open):
        try:
            data = ser.read().decode().strip()
            if data:
                list.append(data)
        except ValueError:
            pass
    if list:
        list.pop()
    try:
        voltage = int("".join(list)) * (5.0 / 1023.0)
        update(voltage)
    except ValueError:
        pass
    list.clear()
    root.update_idletasks()
    root.update()
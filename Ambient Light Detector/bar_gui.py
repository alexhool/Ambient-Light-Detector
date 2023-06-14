import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import serial
import time

# Function to turn the LED on
def ledOn():
    on.configure(state="disabled", bg='#D3D3D3')
    ser.write(bytes('H', 'UTF-8'))
    ser.flush()
    off.configure(state="normal", bg='#f0f6f7')

# Function to turn the LED off
def ledOff():
    off.configure(state="disabled", bg='#D3D3D3')
    ser.write(bytes('L', 'UTF-8'))
    ser.flush()
    on.configure(state="normal", bg='#f0f6f7')
    
# Function to update the bar graph
def update(voltage):
    ax.margins(0.5, 0) 
    ax.set_ylim(0, 5.4)
    ax.set_yticks(np.arange(0, 5.5, 0.5))
    ax.set_title("Ambient Light", size=16, pad=25, weight='bold')
    ax.set_ylabel("Voltage (V)", size=14, labelpad=10)
    bar[0].set_height(voltage)
    text.set_text('{:.3f} V'.format(voltage)) # update voltage label
    text.set_y(voltage + 0.08) # move label with bar
    canvas.draw()

# Function to quit the program
def exit():
    ledOff()
    root.destroy()

# Initialize serial connection
ser = serial.Serial(port='COM3', baudrate=9600, timeout=0)

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

# Add LED Visualizer label
label = tk.Label(root, text="LED Visualizer:", font=("DejaVu Sans", 15), bg='#e4f2f5', wraplength=100, justify="center")
label.grid(column=1, row=2, padx=6, pady=0, sticky=tk.SW)

# Add the on button
on = tk.Button(root, text="On", width=10, height=1, font=("DejaVu Sans", 9), bg='#f0f6f7', state="normal", command=ledOn)
on.grid(column=1, row=3, padx=12, pady=10, sticky=tk.NW)

# Add the off button
off = tk.Button(root, text="Off", width=10, height=1, font=("DejaVu Sans", 9), bg='#D3D3D3', state="disabled", command=ledOff)
off.grid(column=1, row=3, padx=12, pady=38, sticky=tk.NW)

# Add the quit button
quit = tk.Button(root, text="QUIT", width=10, height=2, font=("DejaVu Sans", 9), bg='#f0f6f7',
                activebackground='#de282c', activeforeground='#f0f6f7',
                command=exit)
quit.grid(column=1, row=14, padx=12, pady=5, sticky=tk.W)
root.protocol("WM_DELETE_WINDOW", exit)

# Read serial data and update the bar graph
time.sleep(1.25)
while True:
    try:
        data = ser.readline().decode().strip()
        ser.reset_input_buffer()
        if data:
            voltage = int(data) * (5.0 / 1023.0)
            if (voltage > 0.5 or voltage == 0):
                print(voltage)
                update(voltage)
    except ValueError:
        pass
    root.update_idletasks()
    root.update()
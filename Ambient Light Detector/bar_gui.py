import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import serial

# Initialize serial connection
ser = serial.Serial(port='COM3', baudrate=9600, timeout=0)

# Set up the plot
fig = Figure(figsize=(4, 6), facecolor='#e4f2f5')
fig.subplots_adjust(top=0.865, bottom=0.115, left=0.215, right=0.85, hspace=0.2, wspace=0.2)
ax = fig.add_subplot(1,1,1)
ax.set_facecolor('#f0f6f7')
ax.tick_params(axis='x', bottom=False, labelsize=14, pad=10)
ax.tick_params(axis='y', left=True, labelsize=12, pad=2)
voltage_bar = ax.bar("Brightness", 0, color='#a1c9f4', linewidth=0, width=2, align='center')

# Set up the Tkinter GUI
root = tkinter.Tk()
root.title("Ambient Light Graph")
root.resizable(False, False)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

# Function to update the bar graph
def update(voltage):
    for rect, y in zip(voltage_bar, range(1)):
        rect.set_height(voltage)
    ax.margins(0.5, 0) 
    ax.set_ylim(0, 5.25)
    ax.set_yticks(np.arange(0, 5.5, 0.5))
    ax.set_title("Ambient Light", size=16, pad=20, weight='bold')
    ax.set_ylabel("Voltage (V)", size=14, labelpad=8)
    Figure.pause(0.01)

# Read serial data and update the bar graph
while True:
    try:
        data = ser.readline().strip().decode()
        if data:
            voltage = int(data) * (5.0 / 1023.0)
            update(voltage)
    except KeyboardInterrupt:
        break
    except Exception as e:
        pass
    canvas.draw()
    root.update_idletasks()
    root.update()

# Close the serial connection
ser.close()
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import serial

ser = serial.Serial(
        port='COM3', 
        baudrate=9600, 
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0)

fig = plt.figure(figsize=(4,6))
fig.set_facecolor('#e4f2f5')
ax = fig.add_subplot(1,1,1)
ax.set_facecolor('#f0f6f7')
plt.subplots_adjust(top=0.865, bottom=0.115, left=0.215, right=0.88, hspace=0.2, wspace=0.2)
plt.tick_params(axis='x', bottom=False, labelsize=14, pad=10)
plt.tick_params(axis='y', left=True, labelsize=12, pad=2)

def animate(i):
    while True:
        try:
            voltage = float(ser.readline().decode('utf-8')) * (5.0 / 1023.0)
            if (voltage > 0.5 or voltage == 0.0):
                break
        except:
            pass
    ax.clear()
    ax.margins(0.5, 0)
    ax.set_ylim(0, 5.25)
    plt.title("Ambient Light", size=16, pad=20, weight='bold')
    plt.ylabel("Volts", size=14, labelpad=8)
    plt.yticks(np.arange(0, 5.5, step=0.5))
    plt.bar("Brightness", voltage, color='#a1c9f4', linewidth=0, width=2, align='center')

ani = FuncAnimation(fig, animate, frames=1000, interval=0, repeat=True)
plt.show()
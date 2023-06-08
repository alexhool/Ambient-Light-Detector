import matplotlib
matplotlib.use('qtagg')
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize=(4,6))
axes = fig.add_subplot(1,1,1)
plt.subplots_adjust(top=0.87, bottom=0.11, left=0.15, right=0.9, hspace=0.2, wspace=0.2)
plt.tick_params(axis='x', bottom=False, labelsize=12, pad=10)
axes.set_ylim(0, 310)

lst=[i for i in range(300)]

def animate(i):
    x=["", "Brightness", "\n"]
    y=lst[i]
    plt.bar(x, [0,y,0], color='#a1c9f4', linewidth=0, width=2, align='center')

plt.title("Ambient Light", size=16, pad=20, weight='bold')
ani = FuncAnimation(fig, animate, frames=300, interval=10, repeat=True)

plt.show()
import matplotlib
matplotlib.use('qtagg')
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

lst=[i for i in (np.sin(np.linspace(-np.pi, np.pi, 200))+10)]

fig = plt.figure(figsize=(4,6))
axes = fig.add_subplot(1,1,1)
plt.subplots_adjust(top=0.87, bottom=0.11, left=0.15, right=0.9, hspace=0.2, wspace=0.2)
plt.tick_params(axis='x', bottom=False, labelsize=12, pad=10)


def animate(i):
    axes.clear()
    axes.margins(0.5, 0)
    axes.set_ylim(min(lst), max(lst)+1)
    plt.yticks(np.arange(min(lst), max(lst)+1, step=0.5))
    plt.title("Ambient Light", size=16, pad=20, weight='bold')
    plt.bar("Brightness", lst[i], color='#a1c9f4', linewidth=0, width=2, align='center')

ani = FuncAnimation(fig, animate, frames=200, interval=1, repeat=True)
print(len(lst))
plt.show()
# Standard imports
import os
import time
import tkinter as tk
from contextlib import suppress
# Non-standard imports as found in requirements.txt
import psutil
import serial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class LightGui:
    def __init__(self, ser):
        # Initialize the serial connection
        self.ser = ser

        # Initialize the Tkinter GUI
        self.root = tk.Tk()

        # Initialize the plot
        self.fig = Figure(figsize=(4, 6), facecolor="#fdefc3")
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.rect = self.ax.bar(
            x="Brightness",
            height=0,
            color="#fcd768",
            edgecolor="#000000",
            linewidth=0.7,
            width=2,
            align="center",
        )
        self.textVolt = self.ax.text(0, 0, "", ha="center", va="bottom", size=11)

        # Initialize the plot to the Tkinter widget
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)

        # Initialize Serial Connection label
        self.labelSer = tk.Label(
            self.root,
            text="Serial Connection",
            font=("DejaVu Sans", 15),
            bg="#fdefc3",
            wraplength=110,
            justify="center",
        )

        # Initialize the Serial On button
        self.onSer = tk.Button(
            self.root,
            text="On",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#D3D3D3",
            state="disabled",
            command=self.serial_on,
        )

        # Initialize the Serial Off button
        self.offSer = tk.Button(
            self.root,
            text="Off",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#fefdf9",
            state="normal",
            command=self.serial_off,
        )

        # Initialize LED Visualizer label
        self.labelLED = tk.Label(
            self.root,
            text="LED Visualizer",
            font=("DejaVu Sans", 15),
            bg="#fdefc3",
            wraplength=100,
            justify="center",
        )

        # Initialize the LED On button
        self.onLED = tk.Button(
            self.root,
            text="On",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#fefdf9",
            state="normal",
            command=self.led_on,
        )

        # Initialize the LED Off button
        self.offLED = tk.Button(
            self.root,
            text="Off",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#D3D3D3",
            state="disabled",
            command=self.led_off,
        )

        # Initialize the Night LED label
        self.labelNightLED = tk.Label(
            self.root,
            text="LED\nNight Light",
            font=("DejaVu Sans", 15),
            bg="#fdefc3",
            wraplength=100,
            justify="center",
        )

        # Initialize the Night LED On button
        self.onNightLED = tk.Button(
            self.root,
            text="On",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#fefdf9",
            state="normal",
            command=self.night_on,
        )

        # Initialize the Night LED Off button
        self.offNightLED = tk.Button(
            self.root,
            text="Off",
            width=10,
            height=1,
            font=("DejaVu Sans", 9),
            bg="#D3D3D3",
            state="disabled",
            command=self.night_off,
        )

        # Initialize the Lux label
        self.labelLux = tk.Label(
            self.root,
            text="Incident Light Value",
            font=("DejaVu Sans", 15),
            bg="#fdefc3",
            wraplength=100,
            justify="center",
        )

        # Initialize the Lux value label
        self.textLux = tk.Label(
            self.root,
            width=11,
            height=1,
            font=("DejaVu Sans", 13),
            bg="#fefdf9",
            borderwidth=1,
            relief="solid",
            anchor=tk.CENTER,
        )

        # Initialize the quit button
        self.quitB = tk.Button(
            self.root,
            text="QUIT",
            width=10,
            height=2,
            font=("DejaVu Sans", 9),
            bg="#fefdf9",
            activebackground="#de282c",
            activeforeground="#fefdf9",
            command=self.exit_gui,
        )

    def create_gui(self):
        # Set up the Tkinter GUI
        self.root.title("Ambient Light Graph")
        icon = tk.PhotoImage(file="light-bulb.png")
        self.root.iconphoto(True, icon)
        self.root.geometry("545x621")
        self.root.resizable(False, False)
        self.root.config(bg="#fdefc3")

        # Set up the plot
        self.fig.subplots_adjust(top=0.865, bottom=0.1, left=0.215, right=0.85, hspace=0.2, wspace=0.2)
        self.ax.set_facecolor("#fefdf9")
        self.ax.tick_params(axis="x", bottom=False, labelsize=14, pad=10)
        self.ax.tick_params(axis="y", left=True, labelsize=12, pad=2)

        # Add the plot to the Tkinter widget
        self.canvas.get_tk_widget().config(bg="#000000")
        self.canvas.get_tk_widget().grid(column=0, row=0, rowspan=2, sticky=tk.N, padx=10, pady=8, ipadx=5, ipady=2)

        # Add Serial Connection label
        self.labelSer.grid(column=1, row=0, rowspan=2, padx=0, pady=26, sticky=tk.N)

        # Add the Serial On button
        self.onSer.grid(column=1, row=0, rowspan=2, padx=14, pady=84, sticky=tk.N)

        # Add the Serial Off button
        self.offSer.grid(column=1, row=0, rowspan=2, padx=14, pady=111, sticky=tk.N)

        # Add LED Visualizer label
        self.labelLED.grid(column=1, row=1, rowspan=4, padx=0, pady=156, sticky=tk.N)

        # Add the LED On button
        self.onLED.grid(column=1, row=1, rowspan=1, padx=14, pady=214, sticky=tk.N)

        # Add the LED Off button
        self.offLED.grid(column=1, row=1, rowspan=1, padx=14, pady=241, sticky=tk.N)

        # Add the Night LED label
        self.labelNightLED.grid(column=1, row=1, rowspan=1, padx=0, pady=286, sticky=tk.N)

        # Add the Night LED On button
        self.onNightLED.grid(column=1, row=1, rowspan=1, padx=14, pady=344, sticky=tk.N)

        # Add the Night LED Off button
        self.offNightLED.grid(column=1, row=1, rowspan=1, padx=14, pady=371, sticky=tk.N)

        # Add the Lux label
        self.labelLux.grid(column=1, row=1, padx=0, pady=416, sticky=tk.N)

        # Add the Lux value label
        self.textLux.grid(column=1, row=1, padx=1, pady=474, ipady=16, sticky=tk.N)

        # Add the quit button
        self.quitB.grid(column=1, row=1, padx=13, pady=564, sticky=tk.N)
        self.root.protocol("WM_DELETE_WINDOW", self.exit_gui)

    # Function to draw the GUI
    def draw(self):
        self.root.update_idletasks()
        self.root.update()

    # Function to turn the LED on
    def led_on(self):
        self.onLED.configure(state="disabled", bg="#D3D3D3")
        self.onNightLED.configure(state="disabled", bg="#D3D3D3")
        self.ser.write(bytes("H", "UTF-8"))
        self.ser.flush()
        self.offLED.configure(state="normal", bg="#f0f6f7")

    # Function to turn the LED off
    def led_off(self):
        with suppress(serial.SerialException):
            self.ser.write(bytes("L", "UTF-8"))
            self.ser.flush()
        self.offLED.configure(state="disabled", bg="#D3D3D3")
        self.onLED.configure(state="normal", bg="#f0f6f7")
        self.onNightLED.configure(state="normal", bg="#f0f6f7")

    # Function to turn the night LED on
    def night_on(self):
        self.onNightLED.configure(state="disabled", bg="#D3D3D3")
        self.onLED.configure(state="disabled", bg="#D3D3D3")
        self.ser.write(bytes("N", "UTF-8"))
        self.ser.flush()
        self.offNightLED.configure(state="normal", bg="#f0f6f7")

    # Function to turn the night LED off
    def night_off(self):
        with suppress(serial.SerialException):
            self.ser.write(bytes("D", "UTF-8"))
            self.ser.flush()
        self.offNightLED.configure(state="disabled", bg="#D3D3D3")
        self.onNightLED.configure(state="normal", bg="#f0f6f7")
        self.onLED.configure(state="normal", bg="#f0f6f7")

    # Function to turn serial connection on
    def serial_on(self):
        with suppress(serial.SerialException):
            self.onSer.configure(state="disabled", bg="#D3D3D3")
            self.rect[0].set_visible(True)
            self.ser.open()
            time.sleep(1.27)
            self.onLED.configure(state="normal", bg="#f0f6f7")
            self.onNightLED.configure(state="normal", bg="#f0f6f7")
            self.offSer.configure(state="normal", bg="#f0f6f7")

    # Function to turn serial connection off
    def serial_off(self):
        self.offSer.configure(state="disabled", bg="#D3D3D3")
        self.led_off()
        self.night_off()
        self.onLED.configure(state="disabled", bg="#D3D3D3")
        self.onNightLED.configure(state="disabled", bg="#D3D3D3")
        self.ser.close()
        self.rect[0].set_visible(False)
        self.textVolt.set_text("Lost Connection")
        self.textVolt.set_y(2.7)
        self.textLux.config(text="")
        self.canvas.draw()
        self.onSer.configure(state="normal", bg="#f0f6f7")

    # Function to update the bar graph
    def update(self, analog):
        lux = int(round(pow(analog, 2) * -0.00035 + analog * 1.85, -1))
        height = analog * (4.963 / 1023.0)
        self.ax.margins(0.5, 0)
        self.ax.set_ylim(0, 5.4)
        self.ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
        self.ax.set_title("Ambient Light", size=16, pad=25, weight="bold")
        self.ax.set_ylabel("Voltage (V)", size=14, labelpad=10)
        self.rect[0].set_height(height)
        self.textVolt.set_text(f"{height:.3f} V")
        self.textVolt.set_y(height + 0.08)
        self.textLux.config(text=f"{lux} Lux")
        self.canvas.draw()

    # Function to quit the program
    def exit_gui(self):
        with suppress(serial.SerialException):
            if not self.ser.is_open:
                self.ser.open()
            self.led_off()
            self.night_off()
        os._exit(0)


def main():
    # Set the process priority to high
    win = psutil.Process()
    win.nice(psutil.HIGH_PRIORITY_CLASS)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Start serial connection
    ser = serial.Serial(baudrate=9600, timeout=0)
    ser.port = "COM3"

    # Create the GUI
    gui = LightGui(ser)
    gui.create_gui()

    # Read serial data and update the bar graph
    lst = []
    gui.update(0)
    with suppress(serial.SerialException):
        gui.serial_on()
    while True:
        try:
            while "|" not in lst:
                if data := ser.read().decode().strip():
                    lst.append(data)
            if lst:
                lst.pop()
            analog = int("".join(lst))
            gui.update(analog)
        except ValueError:
            pass
        except serial.SerialException:
            gui.serial_off()
        lst.clear()
        gui.draw()


# Run the program
if __name__ == "__main__":
    main()

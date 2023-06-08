from tkinter import *
from tkinter import ttk
import serial
import time
import sys

def ledOn():
    ser.write(bytes('H', 'UTF-8'))
    style.configure("state.TLabel", background="grey", foreground="green", font=("Arial", 14, "normal"))

def ledOff():
    ser.write(bytes('L', 'UTF-8'))
    style.configure("state.TLabel", background="grey", foreground="red", font=("Arial", 14, "normal"))

# root window
root = Tk()
root.title("Serial LED Control")
root.config(bg='grey', padx=30, pady=30)
root.geometry('350x235')
root.resizable(False, False)
state = StringVar()

# style
style = ttk.Style()
style.configure("title.TLabel", background="grey", font=("Arial", 20, "bold"))
style.configure("text.TLabel", background="grey", font=("Arial", 14, "normal"))
style.configure("TButton", background="grey", font=("Arial", 14, "normal"))

# serial setup
ser = serial.Serial(
        port='COM3', 
        baudrate=9600, 
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0)
ledOff()

# label - title
label = ttk.Label(root, text="LED Control", style="title.TLabel")
label.grid(column=0, row=0, sticky=N, columnspan=2, padx=20, pady=10)

# label - state text
label = ttk.Label(root, text="State: ", style="text.TLabel")
label.grid(column=0, row=1, sticky=E, padx=0, pady=5)

# label - led state
label = ttk.Label(root, textvariable=state, style="state.TLabel")
label.grid(column=1, row=1, sticky=W, padx=0, pady=5)

# button - LED on
onButton = ttk.Button(root, text="On", width=10, command=ledOn)
onButton.grid(column=0, row=2, sticky=S, padx=10, pady=10, ipadx=5, ipady=2)

# button - LED off
offButton = ttk.Button(root, text="Off", width=10, command=ledOff)
offButton.grid(column=1, row=2, sticky=S, padx=10, pady=10, ipadx=5, ipady=2)

# main loop
time.sleep(1.25)
while True:
    if (ser.read() == b'1'):
        state.set("On")
    if (ser.read() == b'0'):
        state.set("Off")
    root.update_idletasks()
    root.update()
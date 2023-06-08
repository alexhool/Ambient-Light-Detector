from tkinter import *
from tkinter import ttk
import serial

# serial setup
ser = serial.Serial('com3', 9600)
ser.write(bytes('L', 'UTF-8'))

def ledOn():
    ser.write(bytes('H', 'UTF-8'))

def ledOff():
    ser.write(bytes('L', 'UTF-8'))

# root window
root = Tk()
root.title("Serial LED Control")
root.config(bg='grey', padx=50, pady=30)
root.geometry('400x250')
root.resizable(False, False)

# style
style = ttk.Style()
style.configure("TLabel", background="grey", font=("Arial", 20, "bold"))
style.configure("TButton", background="grey", foreground="black", font=("Arial", 14, "normal"))

# label - title
label = ttk.Label(root, text="LED Control", style="TLabel")
label.grid(column=0, row=0, sticky=N, columnspan=2, padx=20, pady=30)

# button - LED on
onButton = ttk.Button(root, text="On", width=10, command=ledOn)
onButton.grid(column=0, row=1, sticky=S, padx=10, pady=10, ipadx=5, ipady=2)
# button - LED off
onButton = ttk.Button(root, text="Off", width=10, command=ledOff)
onButton.grid(column=1, row=1, sticky=S, padx=10, pady=10, ipadx=5, ipady=2)

root.mainloop()
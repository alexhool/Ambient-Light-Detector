from tkinter import *
from tkinter import ttk
import serial

def ledOn():
    ser.write(bytes('H', 'UTF-8'))
    status.set("LED ON")

def ledOff():
    ser.write(bytes('L', 'UTF-8'))
    status.set("LED OFF")

# root window
root = Tk()
root.title("Serial LED Control")
root.config(bg='grey', padx=30, pady=30)
root.geometry('350x235')
root.resizable(False, False)
status = StringVar()

# serial setup
ser = serial.Serial('com3', 9600)
ledOff()

# style
style = ttk.Style()
style.configure("title.TLabel", background="grey", font=("Arial", 20, "bold"))
style.configure("text.TLabel", background="grey", font=("Arial", 14, "normal"))
style.configure("TButton", background="grey", font=("Arial", 14, "normal"))

# label - title
label = ttk.Label(root, text="LED Control", style="title.TLabel")
label.grid(column=0, row=0, sticky=N, columnspan=2, padx=20, pady=10)

# label - led status
label = ttk.Label(root, text=status, style="text.TLabel")
label.grid(column=0, row=1, sticky=N, columnspan=2, padx=5, pady=5)

# button - LED on
onButton = ttk.Button(root, text="On", width=10, command=ledOn)
onButton.grid(column=0, row=2, sticky=S, padx=10, pady=20, ipadx=5, ipady=2)
# button - LED off
offButton = ttk.Button(root, text="Off", width=10, command=ledOff)
offButton.grid(column=1, row=2, sticky=S, padx=10, pady=20, ipadx=5, ipady=2)

root.mainloop()
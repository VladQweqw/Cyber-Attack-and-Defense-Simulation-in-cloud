import core.utils.attacks as attacks
import core.utils.tools as tools

import psutil
import ipaddress

import tkinter
from tkinter import ttk
import sv_ttk

root = tkinter.Tk()
sv_ttk.set_theme('dark')
root.geometry('600x500+10+20')
root.title("Casper - Peneration testing tool")

# grid layout

# 3 columns, 1fr 1fr 1fr
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# 3 rows
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

header_frame = ttk.Frame(root, padding=10)

header_frame.grid(row=0, column=0, sticky='nsew', columnspan=3)

appTitle = ttk.Label(header_frame, text="Casper")
appTitle.place(relx=0.5, rely=0.1, anchor="center")

# last line
root.mainloop()

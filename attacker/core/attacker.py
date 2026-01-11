import core.utils.attacks as attacks
import core.utils.tools as tools

from core.utils.helpers import menu_options

import psutil
import ipaddress

import tkinter as tk
from tkinter import ttk
import sv_ttk

root = tk.Tk()
sv_ttk.set_theme('dark')
root.geometry('600x700')
root.minsize(600, 700)
root.maxsize(600, 700)
root.title("Casper - Peneration testing tool")
root.iconbitmap("public/images/logo.ico")
# grid layout

# 3 columns, 1fr 1fr 1fr
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# 3 rows
root.rowconfigure(0, weight=0, minsize=75)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

header_frame = ttk.Frame(root, padding=10)
attackComboFrame = ttk.Frame(root, padding=10)
interfaceComboFrame = ttk.Frame(root, padding=10)

header_frame.grid(row=0, column=0, sticky='nsew', columnspan=2)
attackComboFrame.grid(row=1, column=0, sticky='nsew')
interfaceComboFrame.grid(row=1, column=1, sticky='nsew')

# app title
image = tk.PhotoImage(file='public/images/hero_logo.png')
appTitle = ttk.Label(header_frame, image=image)
appTitle.place(relx=0.5, rely=.5, anchor="center")

# Attack dropdown
attacksLabel = tk.Label(
    attackComboFrame,
    text="Choose attack type")
attacksLabel.pack(side='top')

attacksText = tk.StringVar(value=menu_options[0])
attackCombo = ttk.Combobox(
    attackComboFrame, 
    textvariable=attacksText,
    values=menu_options,
    state='readonly',
    width=30
)
attackCombo.place(anchor='center', relx=0.5, rely=0.2)

# Interface dropdown
interfacesLabel = tk.Label(
    interfaceComboFrame,
    text="Choose interface")
interfacesLabel.pack(side='top')

# get interfaces

interfaces, brief_interfaces = tools.get_interfaces()

interfacesText = tk.StringVar(value=menu_options[0])
interfacesCombo = ttk.Combobox(
    interfaceComboFrame, 
    textvariable=interfacesText,
    values=brief_interfaces,
    state='readonly',
    width=30
)
interfacesCombo.place(anchor='center', relx=0.5, rely=0.2)


# last line
root.mainloop()

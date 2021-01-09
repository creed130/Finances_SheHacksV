import tkinter as tk
from tkinter import *

def window():
    newWindow = Toplevel()

    newWindow.geometry('600x400')
    Label(newWindow,
         text="Choose your apartment!\n",
         fg="black"
    ).pack()
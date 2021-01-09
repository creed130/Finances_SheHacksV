import tkinter as tk
from tkinter import *

class gameMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            text="Congratulations, you're an adult.\nTime to move out!\n",
            fg="black",
        )

        def window():
            Toplevel()

        self.button = tk.Button(
            text="Click here to begin!",
            command=window,
            width=25,
            height=3,
            bg="white",
            fg="red"
        )

        self.bquit = tk.Button(text="QUIT", fg="red", bg="white",
                              command=self.master.destroy)

        self.label.pack()
        self.button.pack()
        self.bquit.pack()
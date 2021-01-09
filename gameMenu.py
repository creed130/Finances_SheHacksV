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
            text="\n\n\nCongratulations, you're an adult.\n\nTime to move out!\n",
            fg="black",
            font=("Arial", 16)
        )

        def window():
            Toplevel()

        self.button = tk.Button(
            text="Click here to begin your life!",
            command=window,
            fg="red",
            padx=10
        )

        self.bquit = tk.Button(text="QUIT", fg="red", bg="white",
                              command=self.master.destroy)

        self.label.pack()
        self.button.pack()
        self.bquit.pack(anchor="w", side="bottom")
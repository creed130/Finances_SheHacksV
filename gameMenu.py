import tkinter as tk
import gamePlay

class gameMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            text="\n\n\nCongratulations, you're an adult.\n\nYour parents have given you $10 000 in savings. Time to move out!\n",
            fg="black",
            font=16
        )

        self.button = tk.Button(
            text="Click here to begin your life!",
            command=gamePlay.window1,
            width=25,
            height=3,
            bg="white",
            fg="red"
        )

        self.bquit = tk.Button(text="QUIT",
                               fg="red",
                               bg="white",
                               command=self.master.destroy)

        self.label.pack()
        self.button.pack()
        self.bquit.pack(anchor="w", side="bottom")

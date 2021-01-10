import tkinter as tk
import gamePlay


class gameMenu(tk.Frame):
    def __init__(self, HOUSE='cheap', master=None):


class GameMenu(tk.Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            text="\n\n\nCongratulations, you're an adult.\n\nTime to move out!\n\n"
            "You just got your first credit card,\nand now you need to build your credit score.\n"
            "\n\nA credit score is a number the bank keeps track of\nto represent how trustworthy you are to receive a loan.\n"
            "It will rise slowly as you pay your credit card bills on time,\n"
            "But watch out! One mistake can drop it drastically.\n\n"
            "\nThroughout the game, you will make financial decisions\nwhich will help or detriment your financial situation.\n"
            "Good luck!\n\n",
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

"""
Authors: Charlotte Reed, Jen Kovinich, Al Wong
c2021 for the SheHacks V Hackathon
"""

import tkinter as tk
import gamePlay

class gameMenu(tk.Frame):
    '''
    A class to represent the physical game menu.
    Inherits from the tkinter Frame class.

    ...

    Attributes
    ----------
    master : tk.root
        The root menu widget.

    Methods
    -------
    create_widgets(self):
        Initializes the widgets on the root menu.
    '''

    def __init__(self, HOUSE='cheap', master=None):
        '''
        Constructs all the necessary attributes for the gameMenu.

        Parameters
        ----------
            HOUSE : str
                type of house the person starts with.
            master : tk.root
                the root menu widget.
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        '''
        Creates the widgets for the root menu.

        Returns
        -------
        None
        '''
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

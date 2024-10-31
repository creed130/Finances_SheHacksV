"""
Authors: Charlotte Reed, Jen Kovinich, Al Wong
c2021 for the SheHacks V Hackathon
"""

import tkinter as tk

from gameMenu import gameMenu

HOUSE = 'cheap'

SAVINGS = 10000

if __name__ == '__main__':
    '''
    Main loop to open the app
    '''
    root = tk.Tk()
    root.title('Common Cents')
    root.geometry('600x500')

    app = gameMenu(HOUSE, master=root)
    app.mainloop()


class CommonCents(tk.Tk):
    '''
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes the tkinter class Common Cents.
        Inherits parameters.
        '''
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, GetStarted):  # Month1, Month2):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        '''
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        '''

        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):
    '''
    The Main Menu, which is the first frame that a user sees when they start the app.
    '''

    def __init__(self, parent, controller):
        '''
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        '''
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Congratulations, you just turned 18! " +
                                     "Your parents have given you $10 000 in savings.\n",
                                fg="black").pack()
        label2 = tk.Label(self, text="Now that you're on your own, you need to manage your finances yourself." +
                                     "\nTo start, choose an apartment." +
                                     "\nThe newer apartment looks nicer, but costs more upfront. " +
                                     "The older apartment might be better for your bank account upfront, " +
                                     "but don't forget about any fixes you might have to do later. Choose wisely!").pack()
        buttonExp = tk.Button(self, text="New Apartment",
                              command=lambda: controller.show_frame(GetStarted))
        buttonExp.pack()

        buttonCheap = tk.Button(self, text="Old Apartment",
                                command=lambda: controller.show_frame(GetStarted))
        buttonCheap.pack()


class GetStarted(tk.Frame):
    '''
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    '''

    def __init__(self, parent, controller):
        '''
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        '''

        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Your rent is $").pack()

        button = tk.Button(self, text="Main Menu?",
                           command=lambda: controller.show_frame(MainMenu))
        button.pack()

app = CommonCents()
app.mainloop()


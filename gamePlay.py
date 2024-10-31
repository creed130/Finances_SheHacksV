"""
Authors: Charlotte Reed, Jen Kovinich, Al Wong
c2021 for the SheHacks V Hackathon
"""

from tkinter import *

def window1():
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

    newWindow1 = Toplevel()

    newWindow1.geometry('600x400')
    Label(newWindow1,
         text="Choose your apartment wisely!\n\nThe nice apartment is more expensive"
              "\nwhile the cheap apartment is more risky.\n",
         fg="black"
    ).pack()

    nice = Button(
        newWindow1,
        text="Nice Apartment",
        command=window2,
        fg="black"
    )

    cheap = Button(
        newWindow1,
        text="Cheap Apartment",
        command=window3,
        fg="black"
    )

    nice.pack()
    cheap.pack()

#nice apt
def window2():
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

    HOUSE='nice'
    newWindow2 = Toplevel()
    newWindow2.geometry('400x200')
    Label(newWindow2,
          text="Welcome to your new apartment!\n\nYour monthly rent is $900",
          fg="black"
        ).pack()

#cheap apt
def window3():
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

    HOUSE='cheap'
    newWindow3 = Toplevel()
    newWindow3.geometry('400x200')
    Label(newWindow3,
          text="Welcome to your new apartment!\n\nYour monthly rent is $700",
          fg="black").pack()

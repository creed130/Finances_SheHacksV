from tkinter import *

def window1():
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

def window2():
    HOUSE='nice'
    newWindow2 = Toplevel()
    newWindow2.geometry('400x200')

def window3():
    HOUSE='cheap'
    newWindow3 = Toplevel()
    newWindow3.geometry('400x200')
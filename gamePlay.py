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
    newWindow2 = Toplevel()

def window3():
    newWindow3 = Toplevel()
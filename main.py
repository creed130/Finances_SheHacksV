import tkinter as tk

from gameMenu import gameMenu

HOUSE = 'cheap'

#from gameMenu import gameMenu


SAVINGS = 10000


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Common Cents')
    root.geometry('600x500')


    app = gameMenu(HOUSE, master=root)
    app.mainloop()


    #app = gameMenu(master=root)
    #app.mainloop()


#global apartment # if 0, apartment is cheap. if 1, apartment is expensive

class CommonCents(tk.Tk):
    def __init__(self, *args, **kwargs):
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

        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
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

        # global apartment
        # if buttonCheap:
            # apartment = 0
        # elif buttonExp:
            # apartment = 1


class GetStarted(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

    # global apartment
    # print(apartment)

        label = tk.Label(self, text="Your rent is $").pack()

        button = tk.Button(self, text="Main Menu?",
                           command=lambda: controller.show_frame(MainMenu))
        button.pack()


app = CommonCents()
app.mainloop()


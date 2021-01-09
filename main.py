import tkinter as tk
from gameMenu import gameMenu

<<<<<<< HEAD
class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.titleText = tk.Label(
            text="Welcome to Common Cents! Let's walk through a year of living on your own.",
            bg="white",
            fg="black",
            width=70,
            height=3
        )
        self.titleText.pack()

        self.button = tk.Button(self,
            text="Click here to begin!",
            width=25,
            height=5,
            bg="white",
            fg="red"
            #command=self.sayHi
        )
        self.button.pack()
        #self.entry = tk.Entry()

        self.bquit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.bquit.pack()

        #self.hiLabel = tk.Label(
            #text="Hello Tkinter",
            #fg="white",
            #bg="black",
            #width=10,
            #height=4
        #)
        #self.entry.pack(side="bottom")
        #self.hiLabel.pack(side="bottom")
        #def sayHi(self):
        # print out hello and their name
        #name = self.entry.get()
        #print("Hello", name)
        #self.entry.delete(0, tk.END)  # empty the text box

root = tk.Tk()
app = Game(master=root)
app.mainloop()

#if __name__ == '__main__':
=======
if __name__ == '__main__':
    root = tk.Tk()
    app = gameMenu(master=root)
    app.mainloop()
>>>>>>> upstream/main
#
#    self.window = tk.Tk(None, None, 'adulting', 1)
#    self.greeting = tk.Label(text="Hello!")
#    self.greeting.pack()

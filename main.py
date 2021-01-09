import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.button = tk.Button(self,
            text="Click here to begin!",
            width=25,
            height=5,
            bg="white",
            fg="red",
            command=self.sayHi
        )


        self.entry = tk.Entry()

        self.bquit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)


        self.hiLabel = tk.Label(
            text="Hello Tkinter",
            fg="white",
            bg="black",
            width=10,
            height=4
        )

        self.button.pack(side="top")
        self.entry.pack(side="bottom")
        self.hiLabel.pack(side="bottom")
        self.bquit.pack(side="bottom")

    def sayHi(self):
        # print out hello and their name
        name = self.entry.get()
        print("Hello", name)
        self.entry.delete(0, tk.END)  # empty the text box

root = tk.Tk()
app = Game(master=root)
app.mainloop()

#if __name__ == '__main__':
#
#    window = tk.Tk(None, None, 'adulting', 1)
#    greeting = tk.Label(text="Hello!")
#    greeting.pack()
#
#
#
#    window.mainloop()
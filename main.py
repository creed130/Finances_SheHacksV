import tkinter as tk
from gameMenu import gameMenu

if __name__ == '__main__':
    root = tk.Tk()
    app = gameMenu(master=root)
    app.mainloop()

#
#    self.window = tk.Tk(None, None, 'adulting', 1)
#    self.greeting = tk.Label(text="Hello!")
#    self.greeting.pack()

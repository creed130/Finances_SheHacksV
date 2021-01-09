import tkinter as tk
from gameMenu import gameMenu

if __name__ == '__main__':
    root = tk.Tk()
    app = gameMenu(master=root)
    app.mainloop()

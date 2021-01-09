import tkinter as tk
from gameMenu import gameMenu

SAVINGS = 10000

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Common Cents')
    root.geometry('800x600')

    app = gameMenu(master=root)
    app.mainloop()
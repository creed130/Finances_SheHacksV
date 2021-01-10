import tkinter as tk
from gameMenu import gameMenu



if __name__ == '__main__':
    root = tk.Tk()
    root.title('Common Cents')
    root.geometry('600x500')

    app = gameMenu(master=root)
    app.mainloop()
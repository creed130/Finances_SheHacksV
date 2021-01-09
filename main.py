import tkinter as tk


if __name__ == '__main__':

    window = tk.Tk(None, None, 'adulting', 1)

    greeting = tk.Label( text="Hello")

    greeting.pack()

    window.mainloop()
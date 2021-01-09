import tkinter as tk

if __name__ == '__main__':

    window = tk.Tk(None, None, 'adulting', 1)
    greeting = tk.Label(text="Hello!")
    greeting.pack()

    button = tk.Button(
        text = "Click here to begin!",
        width = 25,
        height = 5,
        bg = "white",
        fg = "red"
    )

    button.pack()

    window.mainloop()
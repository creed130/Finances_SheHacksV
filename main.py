import tkinter as tk

def print_hi(name):
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hi', name)


if __name__ == '__main__':
    entry = input("What is your name? ")
    print_hi(entry)

    #prints "Hello name!" to the Tkinter window
    window = tk.Tk()
    greeting = tk.Label(text="Hello " + entry + "!")
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
import tkinter as tk

def print_hi(name):
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hi', name)


if __name__ == '__main__':
    entry = input("What is your name? ")
    print_hi(entry)

    window = tk.Tk()
    greeting = tk.Label(text="Hello")

    greeting.pack

    window.mainloop()
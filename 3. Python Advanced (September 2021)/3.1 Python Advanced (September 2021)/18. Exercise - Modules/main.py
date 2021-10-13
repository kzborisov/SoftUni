import tkinter as tk

from screens import render_main_screen

WINDOWS_SIZE = "600x600"

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(WINDOWS_SIZE)
    window.title("My Cool GUI Shop")
    render_main_screen(window)
    window.mainloop()

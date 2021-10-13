import os
import tkinter as tk

from PIL import ImageTk, Image

from authentication_service import register, login
from global_constants import *
from products_service import get_all_products


def clear_window(window: tk.Tk):
    """Remove all widgets from the screen.
        window: tk.Tk object
    """
    for widget in window.winfo_children():
        widget.destroy()


def render_main_screen(window: tk.Tk):
    clear_window(window)
    # Login Button
    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="white",
        command=lambda: render_login_screen(window)
    ).grid(row=0, column=0)

    # Register Button
    tk.Button(
        window,
        text="Register",
        bg="yellow",
        fg="black",
        command=lambda: render_register_screen(window)
    ).grid(row=0, column=1)


def render_register_screen(window: tk.Tk):
    clear_window(window)

    # Username entry
    tk.Label(window, text="Username:").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    # Password entry
    tk.Label(window, text="Password:").grid(row=1, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=1, column=1)

    # First name entry
    tk.Label(window, text="First Name:").grid(row=2, column=0)
    first_name = tk.Entry(window)
    first_name.grid(row=2, column=1)

    # Last name entry
    tk.Label(window, text="Last Name:").grid(row=3, column=0)
    last_name = tk.Entry(window)
    last_name.grid(row=3, column=1)

    def on_register():
        result = register(
            username.get(), password.get(), first_name.get(), last_name.get()
        )
        if result:
            login(username.get(), password.get())
            render_product_screen(window)
        else:
            tk.Label(
                window, text="Username already exists", fg="red"
            ).grid(row=0, column=2)

    # Register Button
    tk.Button(
        window,
        text="Register",
        bg="green",
        fg="black",
        command=lambda: on_register()
    ).grid(row=4, column=1)
    # Back to main screen
    tk.Button(
        window,
        text="Back",
        bg="yellow",
        fg="black",
        command=lambda: render_main_screen(window)
    ).grid(row=5, column=1)


def render_login_screen(window: tk.Tk):
    clear_window(window)
    # Username entry
    tk.Label(window, text="Username:").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    # Password entry
    tk.Label(window, text="Password:").grid(row=1, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=1, column=1)

    def on_login():
        result = login(username.get(),
                       password.get())
        if result:
            render_product_screen(window)
        else:
            tk.Label(
                window, text="Invalid username or password", fg="red"
            ).grid(row=2, column=1)

    # Login Button
    tk.Button(
        window,
        text="Enter",
        bg="green",
        fg="black",
        command=lambda: on_login()
    ).grid(row=3, column=1)

    # Back to main screen
    tk.Button(
        window,
        text="Back",
        bg="yellow",
        fg="black",
        command=lambda: render_main_screen(window)
    ).grid(row=5, column=1)


def render_product_screen(window: tk.Tk):
    clear_window(window)

    # Get all products from db/products.txt
    all_products = get_all_products()
    row_index = col_index = 0
    for index, product in enumerate(all_products):
        if index % 3 == 0 and not index == 0:
            col_index = 0
            row_index = index * 4
        tk.Label(window, text=product["name"]).grid(row=row_index, column=col_index)

        # Generate Image
        image = Image.open(
            os.path.join(DB_FOLDER_NAME,
                         PRODUCTS_IMAGES_NAME,
                         product["image"])
        ).resize(
            (100, 100)
        )
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(image=photo_image)
        image_label.grid(row=row_index, column=col_index)

        tk.Label(window, text=product["count"]).grid(row=row_index + 2, column=col_index)
        tk.Button(
            window,
            text=f"Buy ",
            bg="black",
            fg="white",
        ).grid(row=row_index + 3, column=col_index)
        col_index += 1

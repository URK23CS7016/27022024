# login_page.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from smart_aquarium_app import SmartAquariumApp

class LoginPage:
    def __init__(self, master, login_callback):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1920x1080")
        self.login_callback = login_callback

        # Load background image for login page
        image = Image.open("background_image.jpg")
        image = image.resize((1920, 1080), Image.BILINEAR)
        image = image.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_login_form()

    def create_login_form(self):

        login_frame = tk.Frame(self.master, bg="black", bd=5, highlightthickness=0, highlightbackground="black")
        login_frame.place(x=540, y=200, anchor='center')
    
        username_label = tk.Label(login_frame, text="Username:", fg="white",bg="black", font=("Arial", 14))
        username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = tk.Entry(login_frame, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        password_label = tk.Label(login_frame, text="Password:",  fg="white",bg="black", font=("Arial", 14))
        password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=self.login, bg="#4caf50", fg="white", font=("Arial", 14))
        login_button.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check username and password
        if username == "Rahgul" and password == "12345678":
            self.master.destroy()  # Close login window
            self.login_callback(username)  # Call the callback function with the username
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

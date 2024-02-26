# smart_aquarium_app.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class SmartAquariumApp:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.title("Smart Aquarium Control Panel")
        self.root.geometry("1280x768")

        # Load background image for main application
        image = Image.open("background_image.png")
        image = image.resize((1280,768), Image.BILINEAR)
        image = image.resize((1280,768))
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_main_interface(username)  # Call the method to display the main interface with username

    def show_main_interface(self, username):
        # Frame for control buttons
        control_frame = tk.LabelFrame(self.root, text=f"Welcome {username}", padx=10, pady=10, bg="white")  # White background
        control_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button_read = tk.Button(control_frame, text="Display Sensor Readings", command=self.display_sensor_readings, bg="#008CBA", fg="white", font=("Arial", 14, "bold"))  # Blue button
        button_read.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        button_feed = tk.Button(control_frame, text="Feed Fish", command=self.feed_fish, bg="#f44336", fg="white", font=("Arial", 14, "bold"))  # Red button
        button_feed.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        button_change_water = tk.Button(control_frame, text="Change Water", command=self.change_water, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))  # Green button
        button_change_water.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=10)

    def display_sensor_readings(self):
        messagebox.showinfo("Sensor Readings", "Temperature: 25°C\nTurbidity: 50 NTU")

    def feed_fish(self):
        messagebox.showinfo("Fish Feeding", "Feeding fish... Fish fed successfully!")

    def change_water(self):
        messagebox.showinfo("Water Change", "Changing water... Water changed successfully!")

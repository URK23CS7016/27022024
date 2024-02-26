# main.py
import tkinter as tk
from login_page import LoginPage
from smart_aquarium_app import SmartAquariumApp

def main():
    root = tk.Tk()
    login_page = LoginPage(root, open_smart_aquarium_app)  # Pass the login_callback function directly
    root.mainloop()

def open_smart_aquarium_app(username):
    app = SmartAquariumApp(username)

if __name__ == "__main__":
    main()

import tkinter as tk
import json
root = tk.Tk()
root.title("Dog Database Saver")
root.geometry("400x300")


def get_database():
    try:
        with open("./Dog/Stored_dogs.json", "r") as file:
            data = json.load(file)
            return data
    except:
        return {}
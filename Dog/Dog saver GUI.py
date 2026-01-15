import tkinter as tk  # Needed for GUI creation
import json  # Needed to import the database


root = tk.Tk()  # Defining root parameters
root.config(bg="gray")
root.title("Dog Database Saver")
root.geometry("400x300")

name = tk.Entry(root)

name.pack()
def get_database():
    try:
        with open("./Dog/Stored_dogs.json", "r") as file:  # works in GH codespace
            data = json.load(file)
            print("data loaded!")
            return data
    except:
        with open("Stored_dogs.json", "r") as file:  # works locally
            data = json.load(file)
            print("data loaded!")
            return data

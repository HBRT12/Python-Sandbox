import tkinter as tk  # Needed for GUI
from tkinter import messagebox  # Needed to show info and error boxes
import json  # Needed to import the database

def get_database():
    try:
        with open("./Dog/Stored_dogs.json", "r") as file:  # works in GH codespace
            data = json.load(file)
            print("data loaded!")
    except:  # works in local machine
        with open("Stored_dogs.json", "r") as file:
            data = json.load(file)
            print("data loaded!")
    return data

def search_data():
    entry_id = entry_id_input.get()
    if entry_id in data:
        if data[entry_id]['Privacy'] == False:
            result = (f"""Name: {data[entry_id]['Name']}
Age: {data[entry_id]['Age']}
Age in dog years: {data[entry_id]['Age in dog years']}
Breed: {data[entry_id]['Breed']}
Fur type: {data[entry_id]['Fur type']}""")
            messagebox.showinfo("Dog Data Found", result)
        else:
            messagebox.showwarning("Private Data", "This response cannot be displayed because it has been marked as private.")
    else:
        messagebox.showerror("Entry Not Found", "This entry ID could not be found in the database.")

data = get_database()

root = tk.Tk()
root.title("Dog Loader GUI")
root.geometry("400x200")
entry_id_label = tk.Label(root, text="Enter Dog Entry ID:")
entry_id_label.pack(pady=10)
entry_id_input = tk.Entry(root, width=50)
entry_id_input.pack(pady=5)
search_button = tk.Button(root, text="Search", command=search_data)
search_button.pack(pady=20)
root.mainloop()
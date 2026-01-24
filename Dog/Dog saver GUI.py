import tkinter as tk  # Needed for GUI creation
from tkinter import messagebox  # Needed to show info and error boxes
import json  # Needed to import the database
import uuid  # Needed to create unique IDs for each dog entry


def get_database():
    try:
        with open("./Dog/Stored_dogs.json", "r") as file:  # works in GH codespace
            data = json.load(file)
            print("data loaded1!")
            return data
    except:
        with open("Stored_dogs.json", "r") as file:  # works locally
            data = json.load(file)
            print("data loaded2!")
            return data

def confirm(user_inputs):
    root.withdraw()  # Hides root window
    confirmation_window = tk.Toplevel(root)
    confirmation_window.geometry("330x200")
    info_display = tk.Label(confirmation_window,
                            text=f"""You have entered the following data:
    Name: {user_inputs[0]}
    Age: {user_inputs[1]}
    Age in dog years: {user_inputs[2]}
    Breed: {user_inputs[3]}
    Fur type: {user_inputs[4]}
    Private data: {user_inputs[5]}
    Submit?""").grid(row=0, column=1)
    yes_button = tk.Button(confirmation_window,
                           text="Yes",
                           activebackground="green",
                           font=("Arial", 20),
                           command=lambda: confirm_yes(confirmation_window, root, user_inputs, dog_data)).grid(row=1, column=0)
    no_button = tk.Button(confirmation_window,
                          text="No",
                          activebackground="red",
                          font=("Arial", 20),
                          command= lambda: confirm_no(confirmation_window, root)).grid(row=1, column=2)

def confirm_no(confirmwindow, rootwindow):
    confirmwindow.destroy()
    rootwindow.deiconify()

def confirm_yes(confirmwindow, rootwindow, userinfo, database):
    try:
        with open("Stored_dogs.json", "w") as file:
            messagebox.showinfo("Response saved!", f"Your response was saved successfully. You may now close the program or submit another response. Response ID: {userinfo[6]}")
    except:
        messagebox.showerror("Error: Failed to save", "The program has failed to upload your data. Your response hasn't been saved!")
    
root = tk.Tk()  # Defining root parameters
root.config(bg="gray")
root.title("Dog Database Saver")
root.geometry("200x200")

dog_name = tk.StringVar(value="Name")
name = tk.Entry(root,  # Entry for dog's name
                textvariable = dog_name).pack(pady=5)

dog_age = tk.StringVar(value="Age")
age = tk.Entry(root,  # Entry for dog's name
               textvariable = dog_age).pack(pady=5)

dog_breed = tk.StringVar(value="Breed")
breed = tk.Entry(root,  # Entry for dog's breed
                 textvariable = dog_breed).pack(pady=5)

dog_fur_type = tk.StringVar(value="Fur type")
fur_type = tk.Entry(root,  # Entry for dog's fur type
                    textvariable=dog_fur_type).pack(pady=5)

dog_privacy = tk.BooleanVar(value=False)
privacy = tk.Checkbutton(root,  # Checkbox to indicate if data is to be kept private
                         text="Hide my response when loaded",
                         onvalue=True,
                         offvalue=False,
                         variable=dog_privacy).pack(pady=5)

enter = tk.Button(root,
                  text="Submit",
                  command= lambda: confirm([dog_name.get().capitalize(),
                                            int(dog_age.get()) if dog_age.get().isdigit() else "No age provided",
                                            int(dog_age.get())*7 if dog_age.get().isdigit() else "N/A",
                                            dog_breed.get().capitalize(),
                                            dog_fur_type.get().capitalize(), 
                                            dog_privacy.get(),
                                            uuid.uuid4()])).pack(pady=5)

dog_data = get_database()
root.mainloop()

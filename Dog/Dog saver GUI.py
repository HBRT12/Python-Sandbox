import tkinter as tk  # Needed for GUI creation
from tkinter import messagebox  # Needed to show info and error boxes
import json  # Needed to import the database
import uuid  # Needed to create unique IDs for each dog entry


def get_database():
    try:
        with open("./Dog/Stored_dogs.json", "r") as file:  # works in GH codespace
            data = json.load(file)
            print("data loaded!")
            return data
    except:  # works in local machine
        with open("Stored_dogs.json", "r") as file:
            data = json.load(file)
            print("data loaded!")
            return data

def confirm(user_inputs):  # Confirmation window before submitting data
    root.withdraw()  # Hides root window
    confirmation_window = tk.Toplevel(root)
    confirmation_window.geometry("330x200")
    info_display = tk.Label(confirmation_window,  # Displaying user inputs for confirmation
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

def confirm_no(confirmwindow, rootwindow):  # If user selects no on confirmation window
    confirmwindow.destroy()  # Close confirmation window and return to root
    rootwindow.deiconify()

def confirm_yes(confirmwindow, rootwindow, userinfo, database):  # If user selects yes on confirmation window
    confirmwindow.destroy()  # Close confirmation window
    try:
        with open("./Dog/Stored_dogs.json", "w") as file:
            database[str(userinfo[6])] = {  # Adding new entry to database
                "Name": userinfo[0],
                "Age": userinfo[1],
                "Age in dog years": userinfo[2],
                "Breed": userinfo[3],
                "Fur type": userinfo[4],
                "Privacy": userinfo[5]
            }
            json.dump(database, file, indent=4)  # Saving updated database
            messagebox.showinfo("Response saved!", f"Your response was saved successfully. You may now close the program or submit another response. Response ID: {userinfo[6]}")
            confirmwindow.destroy()
            rootwindow.deiconify()
    except:
        messagebox.showerror("Error: Failed to save", "The program has failed to upload your data. Your response hasn't been saved!")
    
root = tk.Tk()  # Defining root parameters
root.config(bg="gray")
root.title("Dog Database Saver")
root.geometry("300x200")

dog_name = tk.StringVar(value="")
namelabel = tk.Label(root,  # Label for dog's name
                     text="Dog's name:",
                     bg="gray").grid(row=0, column=0, pady=5)
name = tk.Entry(root,  # Entry for dog's name
                textvariable = dog_name).grid(row=0, column=1, pady=5)

dog_age = tk.StringVar(value="")
agelabel = tk.Label(root,  # Label for dog's age
                    text="Dog's age:",
                    bg="gray").grid(row=1, column=0, pady=5)
age = tk.Entry(root,  # Entry for dog's age
               textvariable = dog_age).grid(row=1, column=1, pady=5)

dog_breed = tk.StringVar(value="")
breedlabel = tk.Label(root,  # Label for dog's breed
                      text="Dog's breed:",
                      bg="gray").grid(row=2, column=0, pady=5)
breed = tk.Entry(root,  # Entry for dog's breed
                 textvariable = dog_breed).grid(row=2, column=1, pady=5)

furtypelabel = tk.Label(root,  # Label for dog's fur type
                        text="Dog's fur type:",
                        bg="gray").grid(row=3, column=0, pady=5)
dog_fur_type = tk.StringVar(value="")
fur_type = tk.Entry(root,  # Entry for dog's fur type
                    textvariable=dog_fur_type).grid(row=3, column=1, pady=5)

dog_privacy = tk.BooleanVar(value=False)
privacylabel = tk.Label(root,  # Label for privacy checkbox
                        text="Keep data private:",
                        bg="gray").grid(row=4, column=0, pady=5)
privacy = tk.Checkbutton(root,  # Checkbox to indicate if data is to be kept private,
                         onvalue=True,
                         offvalue=False,
                         variable=dog_privacy,
                         bg="gray").grid(row=4, column=1, pady=5)

enter = tk.Button(root,
                  text="Submit",
                  command= lambda: confirm([dog_name.get().capitalize(),
                                            int(dog_age.get()) if dog_age.get().isdigit() else "No age provided",  # Dog age validation
                                            int(dog_age.get())*7 if dog_age.get().isdigit() else "N/A",  # Dog age in dog years validation
                                            dog_breed.get().capitalize(),
                                            dog_fur_type.get().capitalize(), 
                                            dog_privacy.get(),
                                            uuid.uuid4()])).grid(row=5, column=1, pady=10)  # Submit button

dog_data = get_database()
root.mainloop()

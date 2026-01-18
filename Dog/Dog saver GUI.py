import tkinter as tk  # Needed for GUI creation
import json  # Needed to import the database

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

def confirm(user_inputs):
    root.withdraw()  # Hides root window
    confirmation_window = tk.Toplevel(root)
    confirmation_window.geometry("300x200")
    info_display = tk.Label(confirmation_window,
                            text=f"""You have entered the following data:
                            Name: {user_inputs[0]}
                            Age: {user_inputs[1]}
                            Breed: {user_inputs[2]}
                            Fur type: {user_inputs[3]}
                            Private data: {user_inputs[4]}
                            Submit?""").pack()
    yes_button = tk.Button(confirmation_window,
                           text="Yes",
                           activebackground="green").pack(pady=5)
    no_button = tk.Button(confirmation_window,
                          text="No",
                          activebackground="red").pack(pady=5)


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
                  command= lambda: confirm([dog_name.get().capitalize(), dog_age.get(), dog_breed.get().capitalize(), dog_fur_type.get().capitalize(), dog_privacy.get()])).pack(pady=5)

dog_data = get_database()
root.mainloop()

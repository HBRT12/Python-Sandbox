import json  # Needed for saving/loading names

def main(name):
    if name.lower() == "hubert":  # Checks if name matches my cool name
        print(f"hello, Hubert. Welcome back to your coding sandbox!")
    else:
        print(f"Hello, {name}. Welcome to this Python program")
    
    try:
        file = open("./Greeter/name_history.txt","a")
    except:
        file = open("name_history.txt","a")  # Create the file if it doesn't exist
    file.write(f"{name}\n".capitalize())  # Write the name to the file with a newline
    file.close()

name_var = input("Please enter your name")

if __name__ == "__main__":  # Ensures program is run directly
    main(name_var)

import json  # Needed for saving/loading names

def main(name):
    if name.lower() == "hubert":  # Checks if name matches my cool name
        print(f"hello, Hubert. Welcome back to your coding sandbox!")
    else:
        print(f"Hello, {name}. Welcome to this Python program")

name_var = input("Please enter your name")

if __name__ == "__main__":  # Ensures program is run directly
    main(name_var)

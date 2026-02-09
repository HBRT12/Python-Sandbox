import json

def main(name):
    if name.lower() == "hubert":
        print(f"hello, Hubert. Welcome back to your coding sandbox!")
    else:
        print(f"Hello, {name}. Welcome to this Python program")

name_var = input("Please enter your name")

if __name__ == "__main__":
    main(name_var)

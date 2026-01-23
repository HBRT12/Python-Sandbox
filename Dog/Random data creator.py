import json
import random


names = ["Alfie", "Bruno", "Clover", "Dexter",
         "Echo", "Finn", "Gus", "Hazel",
         "Indie", "Jasper", "Koda", "Luna",
         "Milo", "Nova", "Ollie", "Pepper",
         "Quincy", "Rosie", "Scout", "Teddy",
         "Uma", "Vinnie", "Willow", "Xander",
         "Yuki", "Ziggy"]  # Possible names

fur_types = ["Short", "Medium", "Long", "Curly",
             "Wiry", "Double coat", "Silky", "Rough",
             "Corded", "Hairless"]  # Possible fur types

def get_data_amount():
    try:
        with open("./Dog/Stored_dogs.json") as data:
            stored_data = json.load(data)
            return len(stored_data)
    except:  # Get the amount of entries in JSON file
        with open("Stored_dogs.json") as data:
            stored_data = json.load(data)
            return len(stored_data)

def confirmed():
    print(f"WARNING: YOU ARE ABOUT TO OVERWRITE THE {get_data_amount()} ENTRIES IN STORED_DOGS.JSON")
    print("ARE YOU SURE YOU WANT TO DO THIS")
    confirmation = input("PLEASE TYPE 'Yes, I want to do this.' TO CONFIRM>>> ")
    if confirmation == "Yes, I want to do this.":
        return True
    else:
        return False

def create_sample_data():
    for i in range(10):
        name = random.choice(names)
        print(f"Name: {name}")

        random_age = random.random()
        if random_age < 0.1:
            age = "Not Provided"
            age_dog_years = "N/A"
        elif random_age < 0.8:
            age = random.randint(1, 8)
            age_dog_years = age * 7
        else:
            age = random.randint(1,16)
            age_dog_years = age * 7
        print(f"Age: {age} ({age_dog_years} in dog years)")

        random_privacy = random.random()

        if random_privacy < 0.15:
            privacy = True
        else:
            privacy = False
        print(f"Privacy: {privacy}")
if confirmed():
    create_sample_data()

input("Press enter to exit...")

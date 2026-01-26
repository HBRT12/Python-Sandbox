import json
import random
import uuid

sample_data = {}

names = [
    "Buddy", "Bella", "Charlie", "Lucy", "Max",
    "Daisy", "Bailey", "Luna", "Cooper", "Molly",
    "Rocky", "Sadie", "Bear", "Lola", "Duke",
    "Zoey", "Toby", "Roxy", "Jack", "Maggie",
    "Oliver", "Chloe", "Leo", "Sophie", "Finn",
    "Ruby", "Oscar", "Rosie", "Jake", "Abby",
    "Milo", "Gracie", "Bentley", "Lily", "Tucker",
    "Penny", "Zeus", "Nala", "Sam", "Ellie",
    "Gus", "Stella", "Shadow", "Coco", "Murphy",
    "Loki", "Mia", "Thor", "Harley", "Willow",
    "Henry", "Honey", "Dexter", "Ginger", "Riley",
    "Bandit", "Sasha", "Marley", "Belle", "Hunter",
    "Simba", "Dakota", "Blue", "Lacey", "Bruno",
    "Jasper", "Maddie", "Ollie", "Casey", "Scout",
    "Hank", "Pepper", "Archie", "Minnie", "Rusty",
    "Winnie", "Apollo", "Cleo", "Shadow", "Lulu",
    "King", "Angel", "Sammy", "Athena", "Bear",
    "Rex", "Dixie", "Jake", "Layla", "Baxter",
    "Sandy", "Moose", "Harper", "Ace", "Nikki",
    "Brandy", "Boomer", "Gizmo", "Honey", "Tank",
    "Chewie", "Cookie", "Rusty", "Fido", "Pepper"
]


fur_types = ["Short", "Medium", "Long", "Curly",
             "Wiry", "Double coat", "Silky", "Rough",
             "Corded", "Hairless"]  # Possible fur types

breeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever",
          "Bulldog", "Beagle", "Poodle", "Rottweiler",
          "Yorkshire Terrier", "Boxer", "Dachshund",
          "Siberian Husky", "Great Dane", "Doberman Pinscher",
          "Australian Shepherd", "Cavalier King Charles Spaniel",
          "Shih Tzu", "Boston Terrier", "Pug",
          "Havanese", "Bichon Frise", "Mastiff"]  # Possible breeds

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

def store_data(dict):
    input("Press enter to overwrite stored_dogs.json with generated data...")
    try:
        with open("./Dog/Stored_dogs.json", "w") as file:
            json.dump(dict, file, indent=4)
    except:
        with open("Stored_dogs.json", "w") as file:
            json.dump(dict, file, indent=4)

def create_sample_data(entry_count, dict=sample_data):
    for i in range(entry_count):
        dog_id = str(uuid.uuid4())  # Generating unique ID
        print(f"\nDog ID: {dog_id}")
        
        name = random.choice(names)  # Randomly selecting a name
        print(f"Name: {name}")
        
        random_age = random.random()
        if random_age < 0.1:
            age = "No age provided"
            age_dog_years = "N/A"
        elif random_age < 0.8:
            age = random.randint(1, 8)  # Randomly selecting an age with weighted probabilities
            age_dog_years = age * 7
        else:
            age = random.randint(5,16)
            age_dog_years = age * 7
        print(f"Age: {age} ({age_dog_years} in dog years)")
        
        random_privacy = random.random()
        if random_privacy < 0.1:  # 10% chance of being private
            privacy = True
        else:
            privacy = False
        print(f"Privacy: {privacy}")
        
        dict[dog_id] = {
            "Name": name,
            "Age": age,
            "Age in dog years": age_dog_years,
            "Breed": random.choice(breeds),  # Randomly selecting a breed
            "Fur type": random.choice(fur_types),  # Randomly selecting a fur type
            "Privacy": privacy
        }
        print("\n" + "-" * 20)
    store_data(dict)

if confirmed():
    create_sample_data(int(input("How many entries do you want to generate>>> ")))  # Create sample data if user confirmed
    input("Press enter to exit...")

import json  # Needed for loading data
try:
    with open("./Dog/Stored_dogs.json") as dogs:  # Imports data from JSON
        stored_dog_dict = json.load(dogs)
        print("Successfully loaded stored data from JSON file")
except:
    print("Error loading stored data from JSON file")

def display_dog_info(dog_dict):
    for dog_name, dog_info in dog_dict.items():  # Loops through each dog in the dictionary
        if dog_info["Privacy"] == False:  # Checks if user wanted their data hidden
            print(f"""Name: {dog_name}
    Age: {dog_info['Age']} (or {dog_info['Age in dog years']} in human years)
    Breed: {dog_info['Breed']}
    Fur type: {dog_info['Fur type']}
    Keep data private: {dog_info['Privacy']}""")  # Displays all info if not private
            print("-"*20)  # Separator between dogs
        else:
            print(f"Name: {dog_name} - Data is private and cannot be displayed.")  # Message if data is private
            print("-"*20)  # Separator between dogs

display_dog_info(stored_dog_dict)  # Calls function to display dog info
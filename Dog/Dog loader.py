import json  # Needed for loading data

try:
    with open("./Dog/Stored_dogs.json") as dogs:  # Imports data from JSON
        stored_dog_dict = json.load(dogs)
        print("Successfully loaded stored data from JSON file")
except:
    print("Error loading stored data from JSON file")

def display_dog_info(dog_dict):
    for each in stored_dog_dict:
        if dog_dict[each]["Privacy"] is False:  # Checks if privacy is set to False
            print(f"""Dog Name: {each}
                Age: {dog_dict[each]['Age']}
                Age in dog years: {dog_dict[each]['Age in dog years']}
                Breed: {dog_dict[each]['Breed']}
                Fur type: {dog_dict[each]['Fur type']}""")  # Displays each dog's information
        else:
            print(f"Dog Name: {each[0]}{'*'*(len(dog_dict[each])-1)} - Data is set to private and cannot be displayed.")  # Message if privacy is True
        print("\n"+"-"*40+"\n")  # Formatting line between entries

display_dog_info(stored_dog_dict)  # Calls function to display dog info

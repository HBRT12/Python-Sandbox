import json  # Needed for loading data


def get_data():
    try:
        with open("./Dog/Stored_dogs.json") as dogs:  # Imports data from JSON
            stored_dog_dict = json.load(dogs)
            print("Successfully loaded stored data from JSON file")
    except:
        with open("Stored_dogs.json") as dogs:
            stored_dog_dict = json.load(dogs)
            print("Successfully loaded stored data from JSON file")
        return stored_dog_dict

def read_data():
    entry_id = input("Please type the ID for the entry that you want to view>>> ")
    if data[entry_id]['Privacy'] == False:
        print(f"""Name: {data[entry_id]['Name']}
        Age: {data[entry_id]['Age']}
        Age in dog years: {data[entry_id]['Age in dog years']}
        Breed: {data[entry_id]['Breed']}
        Fur type: {data[entry_id]['Fur type']}""")
    else:
        print("This response cannot be displayed because it is either private or cannot be found")
data = get_data()

while True:
    read_data()

import json  # Needed for saving data

with open("Stored_dogs.json","r") as dogs:  # Imports data from JSON
    stored_dog_dict = json.load(dogs)

def store_dog(dog_dict, dog_data):
    dog_dict[dog_data[0]] = {"Age": dog_data[1],
                             "Breed": dog_data[2],
                             "Fur type": dog_data[3]}

def get_user_info():
    dog_name = input("What is your dog called>>> ")
    age = int(input("How old is your dog?>>> "))  # Obtaining information from user
    breed = input("What breed is your dog?>>> ")
    fur_type = input("What fur type does your dog have?>>> ")
    return [dog_name, age, age*7, breed, fur_type]  # Age*7 for dog years

def upload_dog_data(info, dictionary):
    with open("Stored_dogs.json","w") as dogs:  # Dumps dictionary with new entry to save file
        json.dump(info, dictionary)

user_info = get_user_info()  # Runs input function to get user information

print(f"""Name: {user_info[0]}
Age:{user_info[1]} (or {user_info[2]} in human years)
Breed: {user_info[3]}
Fur type: {user_info[4]}""")  # Displays user information

store_dog(stored_dog_dict, user_info)
upload_dog_data()
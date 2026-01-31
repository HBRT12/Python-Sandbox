import json

with open('my first json file.json','r') as file:  # Imports saved dictionary
    dictionary_1 = json.load(file)
try:
    print(f'Hello, {dictionary_1["name"]}! your date of birth is {dictionary_1["day of birth"]} {dictionary_1["month of birth"][:3]} {dictionary_1["year of birth"]} and you are {dictionary_1["age"]} years old!')
    print('JSON reading successful!')  # Displays saved data from dictionary
except:
    print('ERROR: Failed to load JSON file content')

input('\n\nPress enter to exit...')  # Stops program from closing immediately

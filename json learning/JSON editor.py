import json  # Needed to save data


dictionary_1 = {}  # Creates dictionary

name = input('What is your name>>> ')
dictionary_1['name'] = name
day_of_birth = input('What day were you born on>>> ')
dictionary_1['day of birth'] = day_of_birth
month_of_birth = input('What month were you born in>>> ')  # Gets user info
dictionary_1['month of birth'] = month_of_birth
year_of_birth = input('What year were you born in>>> ')
dictionary_1['year of birth'] = year_of_birth
age = input('How old are you>>> ')
dictionary_1['age'] = age

with open('my first json file.json','w') as file:  # saves user info
    json.dump(dictionary_1, file, indent=4)
print('Saved to JSON file!')

input("Press enter to exit")  # Stops program from closing instantly

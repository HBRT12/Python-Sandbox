from math import pi  # Pi is needed to calculate the area of a circle

def calculate_circle(radius):  # Calculates circle properties
    diameter = radius * 2  # d = 2r
    circumference= pi * diameter  # c = pi*d
    area = (radius**2) * pi  # a = pi*r^2
    return [radius, diameter, circumference, area]  # Returns results

radius = float(input("Please type the radius of your circle>>> "))

results = calculate_circle(radius)  # Gets results from function

print(f"""
radius: {results[0]}
diameter: {results[1]}
circumference: {results[2]}
area: {results[3]}""")  # Displays results for user
input("\nPress enter to exit...")

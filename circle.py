import turtle

t=turtle.Turtle()  # Setting up objects for turtle
s=turtle.Screen()

s.bgcolor("white")  # Setting colours for bg and line
t.color("black")

for i in range(360):  # Draws circle
    t.forward(1)
    t.left(1)

input("Press enter to exit")  # Awaits user input before quitting

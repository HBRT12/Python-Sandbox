import turtle  # Graphics
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Scramble")

# Parameters
NUM_TURTLES = 10
STEPS = 50
COLORS = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta", "lime", "white"]
RANDOM_EVERY_STEP = True

# Create turtles
turtles = []
for i in range(NUM_TURTLES):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(random.randint(0, 0xFFFFFF))  # Random hex code for randomness
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    turtles.append(t)

# Scramble loop
while True:
    for t in turtles:
        angle = random.randint(0, 360)
        distance = random.randint(20, 100)  # Random movement
        t.setheading(angle)
        if RANDOM_EVERY_STEP:
            t.color(random.randint(0, 0xFFFFFF))  # Random colour per movement if enabled
        t.forward(distance)
        t.speed(0)

# Done
turtle.done()

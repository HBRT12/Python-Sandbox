import turtle as poopookakaland  # Graphics
import random as r


colours = ["red","orange","yellow","green","blue","cyan","teal","brown","pink","gray"]

scr = poopookakaland.Screen()
trt = poopookakaland.Turtle()  # Defining parameters for screen
trt.width(3)

trt.speed(0)
scr.bgcolor("white")  # Defining colours for starting
trt.color("black")

for i in range(360):  # The main thing
    trt.circle(180-i/2)
    trt.right(0.5)
    trt.color(r.choice(colours))

import turtle as poopookakaland
import random as r

colours = ["red","orange","yellow","green","blue","cyan","teal","brown","pink","gray"]
scr = poopookakaland.Screen()
trt = poopookakaland.Turtle()
trt.width(3)

trt.speed(0)
scr.bgcolor("white")
trt.color("black")

for i in range(360):
    trt.circle(180-i/2)
    trt.right(0.5)
    trt.color(r.choice(colours))
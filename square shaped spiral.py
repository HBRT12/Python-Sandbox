import turtle as t
import random as r

def main():
    colours = ["yellow", "red", "blue", "green", "yellow", "orange", "purple", "pink"]
    ITERATIONS = 50
    s=t.Screen()
    s.bgcolor("gray")
    trt = t.Turtle()
    trt.speed(0)
    trt.width(20)
    for i in range(ITERATIONS):
        trt.color(r.choice(colours))
        trt.forward(i * 10)
        trt.right(90)


if __name__ == "__main__":
    main()
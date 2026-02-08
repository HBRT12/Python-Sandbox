import turtle as t
import random as r

def main():
    colours = ["red","blue","green","yellow"]
    ITERATIONS = 50
    RANDOM_COLOURS = True
    s=t.Screen()
    s.bgcolor("gray")
    trt = t.Turtle()
    trt.speed(0)
    trt.width(20)
    for i in range(ITERATIONS):
        if RANDOM_COLOURS:
            trt.color(r.choice(colours))
        else:
            trt.color(colours[i % 4])
        trt.forward(i * 10)
        trt.right(90)


if __name__ == "__main__":
    main()
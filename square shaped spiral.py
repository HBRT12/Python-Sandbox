import turtle as t  # Used for graphics
import random as r  # Used for randomisation

def main():
    colours = ["red","blue","green","yellow"]  # Colours used in spiral
    ITERATIONS = 50
    RANDOM_COLOURS = True
    s=t.Screen()  # Create screen
    s.bgcolor("gray")
    trt = t.Turtle()  # Create turtle
    trt.speed(0)
    trt.width(20)
    for i in range(ITERATIONS):
        if RANDOM_COLOURS:
            trt.color(r.choice(colours))
        else:
            trt.color(colours[i % 4])  # Keeps colours the same on each side
        trt.forward(i * 10)
        trt.right(90)  # Move and rotate


if __name__ == "__main__":  # Prevents running from being imported
    main()

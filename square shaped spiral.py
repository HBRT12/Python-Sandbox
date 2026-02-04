import turtle as t


def main():
    ITERATIONS = 50
    trt = t.Turtle()
    trt.speed(0)
    for i in range(ITERATIONS):
        trt.forward(i * 10)
        trt.right(90)

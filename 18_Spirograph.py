import turtle as t
import random
from turtle import Turtle

t.colormode(255)

shelly: Turtle = t.Turtle()
shelly.shape('turtle')
shelly.color('blue')
shelly.speed('fastest')
# shelly.pensize(1)

radius = 100


def generate_rgb_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colour = (r, g, b)
    return random_colour


circle_range = 80


def draw_circles(size_of_gap):
    for circle in range(1,circle_range):
        shelly.color(generate_rgb_colour())
        shelly.circle(100)
        shelly.right(size_of_gap)


draw_circles(5)




screen = t.Screen()
screen.exitonclick()

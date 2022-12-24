import turtle as t
import random

lia = t.Turtle()
t.colormode(255)
lia.pensize(5)


def generate_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colour = (r,g,b)
    return random_colour


point_of_compass = [0, 90, 180, 270]


num_of_walks = 0
user_input = 1500


def random_walk():
    for paths in range(0, user_input):
        lia.color(generate_colour())
        lia.forward(20)
        lia.setheading(random.choice(point_of_compass))
        lia.right(45)


random_walk()

screen = t.Screen()
screen.exitonclick()

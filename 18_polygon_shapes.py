from turtle import Turtle, Screen
import random

colors = ['pink', 'orchid', 'blue', 'green', 'red', 'yellow', 'purple', 'mediumAquamarine', 'orange']

frankie = Turtle()
frankie.shape('arrow')


def draw_shape(num_of_sides):
    angle = 360 / (num_of_sides)
    for shape in range(0, num_of_sides):
        frankie.forward(100)
        frankie.right(angle)


for shape_side_n in range(3, 11):
    frankie.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()

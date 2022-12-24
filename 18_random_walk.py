from turtle import Turtle, Screen
import random

abby = Turtle()

abby.pensize(6)
abby.speed('fastest')

colors = ['pink', 'orchid', 'blue', 'green', 'red', 'yellow', 'purple', 'mediumAquamarine', 'orange']

# WITHIN THE SCREEN BOUNDARIES
point_of_compass = [0, 90, 180, 270]

# BEYOND THE SCREEN BOUNDARIES
# point_of_compass = [0, 90, 180, 270,360,-90,-180,-270,-360]

num_of_walks = 0
user_input = 1500


def random_walk():
    for paths in range(0, user_input):
        abby.color(random.choice(colors))
        abby.forward(20)
        abby.setheading(random.choice(point_of_compass))
        # abby.right(45)


random_walk()

screen = Screen()
screen.exitonclick()


# end_of_range = False
# while end_of_range == False :
#     num_of_walks += 1
#     if num_of_walks == user_input:
#         end_of_range = True

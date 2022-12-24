from turtle import Turtle,Screen
Mikey = Turtle()
Mikey.color('yellow')
Mikey.shape('turtle')

for square in range(0,4):
    Mikey.right(90)
    Mikey.forward(100)

screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())


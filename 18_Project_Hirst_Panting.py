import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('2_hirst_painting.jpg', 100)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)

donney = t.Turtle()
donney.speed('fastest')

color_list = [(235, 240, 247), (196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109),
              (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81),
              (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112), (223, 172, 184),
              (227, 175, 167), (103, 44, 60), (50, 56, 94), (168, 207, 185), (167, 158, 66), (60, 155, 174),
              (111, 122, 155), (97, 49, 44), (178, 188, 214), (152, 207, 219), (221, 219, 20), (25, 94, 68),
              (78, 71, 42), (18, 88, 101)]

donney.penup()
donney.hideturtle()
# MY CHOSEN STARTING POINT
donney.sety(150)
donney.setx(4)
donney.forward(-159)


def create_circles():
    for item in range(0, 10):
        donney.dot(20, random.choice(color_list))
        donney.penup()
        donney.forward(35)
        donney.pendown()


still_drawing = True
count = 0

while count < 10:
    count += 1
    # print(donney.xcor())
    create_circles()

    donney.penup()
    donney.setx(-155.0)
    donney.right(90)
    donney.forward(40)
    donney.right(-90)
    # donney.pendown()



#
# donney.pendown()

screen = t.Screen()
screen.exitonclick()

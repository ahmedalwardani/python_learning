import colorgram
import turtle as turtle_module
import random

# colours = colorgram.extract('hirst-severed-spots.jpeg', 30)
# rgb_colours = []

# for colour in colours:x
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.r
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(198, 12, 198), (36, 79, 36), (233, 154, 233), (233, 228, 233), (45, 218, 45), (32, 35, 32), (204, 70, 204), (211, 13, 211), (244, 39, 244), (72, 9, 72), (243, 247, 243), (15, 154, 15), (228, 18, 228), (61, 17, 61), (225, 155, 225), (224, 140, 224), (13, 212, 13), (10, 97, 10), (51, 212, 51), (17, 18, 17), (244, 46, 244), (92, 76, 92), (249, 10, 249), (238, 156, 238), (82, 74, 82), (73, 214, 73)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()


import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("green")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def generate_random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(generate_random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)



# for i in range(3, 11):
#     tim.color(random.choice(turtle_line_colours))
#     draw_shape(i)

# for _ in range(200):
#     tim.color(generate_random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

draw_spirograph(5)


screen = Screen()
screen.exitonclick()

# import heroes as h
# print(h.gen())

import turtle as t
import random


def dashed_line(m):
    for i in range(m):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def draw_figures(n):
    for i in range(n):
        tim.fd(50)
        tim.left(360/n)

def random_lines(n):
    for i in range(n):
        r = random_color()
        tim.color(r)
        tim.fd(30)
        tim.setheading(random.choice([0,90,180,270]))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def spirograph(n):
    for i in range(int(360/n)):
        # t.color(random_color())
        t.circle(80)
        t.left(n)

# colors=['cadetblue', 'rosy brown', 'indigo', 'deeppink', 'navy', 'chartreuse', 'orchid', 'cornflowerblue', 'darkorchid', 'indianred', 'deepskyblue', 'lightseagreen', 'wheat', 'slategray', 'darkorange', 'coral', 'khaki']
# # tim.pensize(5)
# tim = t.Turtle()
t.speed(0)
t.colormode(255)

spirograph(7)


screen=t.Screen()
screen.exitonclick()





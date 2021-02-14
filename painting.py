import turtle as t
import colorgram
import random

def extract_color():
    rgb_colors = []
    colors = colorgram.extract('img.jpg', 30)

    for i in colors:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        rgb_colors.append((r, g, b))


def draw_line(n):
    for i in range(n):
        r=random.choice(colors_without_white)
        t.color(r)
        t.fd(0)
        t.pu()
        t.fd(20)
        t.pd()

def goup():
    t.penup()
    y = t.position()[1]+20
    t.goto(0,y)
    t.pendown()

def painting(n, m):
    for i in range(n):
        draw_line(m)
        goup()


colors_without_white = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
t.hideturtle()
t.colormode(255)
t.pensize(10)
t.speed(0)

painting(10, 10)


screen=t.Screen()
screen.exitonclick()
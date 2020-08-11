import turtle
import math
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()
def draw():
    t.goto(75,120)
    t.pencolor("gold")
    design1()
    t.pencolor("dark red")
    t.penup()
    t.forward(150)
    t.pendown()
    design2()
    t.pencolor("grey")
    t.penup()
    t.right(30)
    t.forward(150)
    t.pendown()
    design3()
    turtle.done()
def hex():
    for i in range(6):
        t.forward(50)
        t.right(60)
def hex_set():
    hex()
    for j in range(24):
        t.right(360/24)
        hex()
def design1():
    hex_set()
    for k in range(5):
        t.penup()
        t.right(60)
        t.forward(150)
        t.pendown()
        hex_set()
def design2():
    hex_set()
    t.right(30)
    dist1=math.sqrt(3)*150
    for k in range(5):
        t.penup()
        t.right(60)
        t.forward(dist1)
        t.pendown()
        hex_set()
def design3():
    hex_set()
    for k in range(5):
        t.penup()
        t.right(60)
        t.forward(300)
        t.pendown()
        hex_set()
draw()

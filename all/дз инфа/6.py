from turtle import *
speed(1000)
k = 20
penup()
right(30)
forward(4*k)
right(330)
pendown()

forward(4*k)
right(90)
forward(7*k)
right(45)
forward(4*(2**0.5)*k)
right(135)
forward(11*k)

penup()
for y in range(-14,2):
    for x in range(3,13):
        goto(x*k,y*k)
        dot('red')

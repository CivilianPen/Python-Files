from turtle import *
tracer(0)
goto(0,400)
k = 40
for i in range(3):
    forward(5*k)
    right(90)
    forward(12*k)
    right(90)
penup()
forward(3*k)
right(90)
forward(2*k)
right(90)
pendown()
for i in range(4):
    forward(5*k)
    right(90)
    forward(12*k)

penup()
for y in range(-20,50):
    for x in range(-20,20):
        goto(x*k,y*k)
        dot(4,'red')
update()
mainloop()
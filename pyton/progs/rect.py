
from random import randint
from turtle import *
speed(10000000)
tracer(0)
pos = [0,0]
def init():
    reset()
    k = int(input('enter the size of rects (px) >>> '))
    size = int(input('enter the size of plane shape >>> '))
    rect = [[0]*size for i in range(size)]
    value = input('enter your math graph here (x,y,(,),**,*,+,-,<,>,==,/) >>> ')
    logic(k,size,rect,value)
    

def Func(x,y,value,rect):
    try:
        exec('if ' +value+': \n rect[y][x] = 1')
    except ZeroDivisionError:
        print(x,y)
    else:
        exec('if ' +value+': \n rect[y][x] = 1')
            
def R(k):
    fillcolor('aqua')
    begin_fill()
    for _ in range(4):
        forward(k)
        left(90)
    end_fill()
    
def logic(k,size,rect,value):
    for y in range(len(rect)):
        for x in range(len(rect[y])):
            #rect[i][j] = round(randint(0,1))
            Func(x,y,value,rect)

            if rect[y][x] > 1:
                rect[y][x] = 0    

    for y in range(len(rect)):
        for x in range(len(rect[y])):
            if rect[y][x] == 1:
                penup()
                goto(pos[0]+x*k,pos[1]+y*k)
                pendown()
                R(k)
                #dot('aqua')
    update()
    #for i in range(len(rect)):
        #print(rect[i])
init()
while True:
    if input() == 'new':
        init()

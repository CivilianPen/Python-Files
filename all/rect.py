
from random import randint
from turtle import *
speed(10000000)
k = int(input('enter the size of rects (px) >>> '))
size = int(input('enter the size of plane shape >>> '))
rect = [[0]*size for i in range(size)]
pos = [0,0]
value = input('enter your math graph here (x,y,(,),**,*,+,-,<,>,==,/) >>> ')

def Func(x,y):
    try:
        exec('if ' +value+': \n rect[y][x] = 1')
    except ZeroDivisionError:
        print(x,y)
    else:
        exec('if ' +value+': \n rect[y][x] = 1')
            
def R():
    fillcolor('aqua')
    begin_fill()
    for _ in range(4):
        forward(k)
        left(90)
    end_fill()
    
for y in range(len(rect)):
    for x in range(len(rect[y])):
        #rect[i][j] = round(randint(0,1))
        Func(x,y)

        if rect[y][x] > 1:
            rect[y][x] = 0    

for y in range(len(rect)):
    for x in range(len(rect[y])):
        if rect[y][x] == 1:
            penup()
            goto(pos[0]+x*k,pos[1]+y*k)
            pendown()
            R()
            #dot('aqua')

#for i in range(len(rect)):
    #print(rect[i])

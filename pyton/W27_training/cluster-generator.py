from turtle import *
from math import dist,sin,cos,tan
import random

offsets = [0]
data = []
for count in range(len(offsets)):
    for j in range(140**2):
        x = (random.uniform(-20, 20))
        y = (random.uniform(-20, 20))
        #if (x+y < 10 and -x-y<10) or (x-y<10 and x-y>-10):
            #data.append([x, y])
        #if (y>sin(x) and y<sin(x)+5) and (x<20 and x>-20):
            #data.append([x, y])
        #if (y<10/x) and (x<10/y):
            #data.append([x,y])

def draw(clust):
    tracer(0)
    k = 20
    penup()
    for i in range(len(clust)):
        color = ['blue', 'green', 'red']

        for point in clust[i]:
            goto(point[0]*k,point[1]*k)
            dot(5,color[i])

    update()
    done()
draw([data])
'''k = random.randint(0,1000)
w = open(f'data{k}.txt','w')
for i in data:
    w.write(' '.join(str(x) for x in i)+'\n')'''



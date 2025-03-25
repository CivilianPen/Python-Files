from turtle import *
from math import dist
import random
tracer(0)
k=5
penup()
offsets = [[1,0,0],[-1,20,-100],[-1,-20,-100]]
data = []
for count in range(0,3):
    for i in range(-70,70):
        for j in range(-70,70):
            x = (random.uniform(-50, 50))
            y = (random.uniform(-50, 50))
            a = offsets[count][0]
            b = offsets[count][1]
            c = offsets[count][2]
            if a>0:
                if y > a*x**2+b*x+c:
                    data.append([x,y])
            else:
                if y < a*x**2+b*x+c:
                    data.append([x,y])
def draw(clust):
    tracer(0)
    k = 5
    penup()
    for i in range(len(clust)):
        color = ['blue', 'green', 'red']

        for point in clust[i]:
            goto(point[0]*k,point[1]*k)
            dot(5,color[i])

    update()
    done()
draw([data])
update()    
done()

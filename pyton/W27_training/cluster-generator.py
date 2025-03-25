from turtle import *
from math import dist
import random

offsets = [[[1,0,7,0,25],[2,-2,8,3,49]],[[1,3,7,1,25],[2,5,8,-2,49]]]
data = []
for count in range(len(offsets)):
    for j in range(600**2):
        x = (random.uniform(-30, 30))
        y = (random.uniform(-30, 30))
        ux,dx,uy,dy,R = offsets[count][0][0],offsets[count][0][1],offsets[count][0][2],offsets[count][0][3],offsets[count][0][4]
        ux1,dx1,uy1,dy1,R1 = offsets[count][1][0], offsets[count][1][1], offsets[count][1][2], offsets[count][0][3],offsets[count][1][4]
        if ux*(x+dx)**2+uy*(y+dy)**2<R and ux1*(x+dx1)**2+uy1*(y+dy1)**2>R1:
            data.append([x,y])
        elif x<7 and x>3 and y<5 and y>1:
            data.append([x, y])
        elif x>-10 and x<-6 and y>-6 and y<-2:
            data.append([x, y])
def draw(clust):
    tracer(0)
    k = 30
    penup()
    for i in range(len(clust)):
        color = ['blue', 'green', 'red']

        for point in clust[i]:
            goto(point[0]*k,point[1]*k)
            dot(5,color[i])

    update()
    done()

k = random.randint(0,1000)
w = open(f'data{k}.txt','w')
for i in data:
    w.write(' '.join(str(x) for x in i)+'\n')



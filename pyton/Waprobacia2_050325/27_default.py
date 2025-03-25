from turtle import *
from math import dist
f = open('27_A_20911.txt').readlines()
data = []
for i in f:
    i = i.replace(',', '.')
    x = list(map(float,i.split()))
    data.append(x)
def draw(clust):
    tracer(0)
    k = 20
    penup()
    for point in clust:
        goto(point[0]*k,point[1]*k)
        dot(5,'red')
    for y in range(-10,10):
        for x in range(-10,10):
            if x == 0 or y == 0:
                goto(x * k, y * k)
                dot(5, 'black')
    update()
    done()

clusters = [[],[]]
for i in data:
    x = i[0]
    y = i[1]
    if y>0:
        clusters[0].append(i)
    else:
        clusters[1].append(i)

centers = [[],[]]
for cl in range(len(clusters)):
    #cl - index of cluster
    min_suma = 10**10
    for point1 in range(len(clusters[cl])):
        suma = 0
        for point2 in range(len(clusters[cl])):
            suma += dist(clusters[cl][point1],clusters[cl][point2])
        if suma < min_suma:
            min_suma = suma
            centers[cl]=clusters[cl][point1]

px = int(((centers[0][0]+centers[1][0])/2)*10_000)
py = int(((centers[0][1]+centers[1][1])/2)*10_000)
print(px,py)
from turtle import *
from math import dist

f2 = open('27-59b.txt').readlines()
files = [f2]
for f in files:
    data = []
    for i in f:
        i = i.replace(',', '.')
        x = list(map(float,i.split()))
        data.append(x)

    clusters = []
    while data:
        clusters.append([data.pop()])
        for point1 in clusters[-1]:
            sosed = [point for point in data if dist(point1,point)<0.4]
            clusters[-1]+=sosed
            for point2 in sosed:
                data.remove(point2)

    def draw(clust):
        tracer(0)
        k = 40
        penup()
        for i in range(len(clusters)):
            color = ['blue', 'green', 'red','purple','yellow','orange','lime','aqua']
            color += ['grey']*len(clust)
            for point in clusters[i]:
                goto(point[0]*k,point[1]*k)
                dot(5,color[i])
            ''' for y in range(-10,10):
                for x in range(-10,10):
                    if x == 0 or y == 0:
                        goto(x * k, y * k)
                        dot(5, 'black')'''
        update()
        done()

    '''centers = [[] for i in range(len(clusters))]
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

    px = int(((sum([x[0] for x in centers]))/len(centers))*10_000)
    py = int(((sum([y[1] for y in centers]))/len(centers))*10_000)
    print(px,py)'''

    draw(clusters)
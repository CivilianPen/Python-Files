
from turtle import *
from math import dist
f1 = open('27-93a-2.txt')
f2 = open('27-93b-2.txt')
files = [f2]
curr =0
for f in files:
    def draw(clust):
        tracer(0)
        k = 20
        penup()

        for i in range(len(clust)):
                color = ['blue', 'green', 'red']
                color+= ['black' for i in range(len(clust))]
                for point in range(0,len(clust[i]),10):
                    goto(clust[i][point][0]*k,clust[i][point][1]*k)
                    dot(5,color[i])
                    update()
        for y in range(-10,10):
            for x in range(-10,10):
                if x == 0 or y == 0:
                    goto(x * k, y * k)
                    dot(5, 'aqua')
                    update()
        done()

    data = []

    for i in f:
        i = i.replace(',', '.')
        x = list(map(float,i.split()))
        data.append(x)

    clusters = [[],[],[]]
    for i in data:
        x = i[0]
        y = i[1]
        if dist(i,[9,9])<8:
            if x<9 and y>(10/9)*x:
                clusters[0].append(i)
            elif x>9 and y>-(10/9)*x + 20:
                clusters[1].append(i)
            else:
                clusters[2].append(i)

    '''clusters = []
    while data:
        clusters.append([data.pop()])
        for point1 in clusters[-1]:
            sosed = [point for point in data if dist(point1,point)< 0.4]
            clusters[-1]+=sosed
            for point2 in sosed:
                data.remove(point2)'''

    clusters = [i for i in clusters if len(i) > 100]
    centers = [[] for i in range(len(clusters))]
    for cl in range(len(clusters)):
        # cl - index of cluster
        min_suma = 10 ** 10
        for point1 in range(len(clusters[cl])):
            suma = 0
            for point2 in range(len(clusters[cl])):
                suma += dist(clusters[cl][point1], clusters[cl][point2])
            if suma < min_suma:
                min_suma = suma
                centers[cl] = clusters[cl][point1]

    
    px = int(((sum([x[0] for x in centers])) / len(centers)) * 100_000)
    py = int(((sum([y[1] for y in centers])) / len(centers)) * 100_000)
    print(px, py)


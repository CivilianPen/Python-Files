#data - массив со всеми точками 
data = []
clusters = [] # -> [[кластер1],[кластер2],...,[кластерN]]
while data:
    clusters.append([data.pop()])
    for point1 in clusters[-1]:
        sosed = [point for point in data if dist(point1,point)<2]
        clusters[-1]+=sosed
        for point2 in sosed:
            data.remove(point2)

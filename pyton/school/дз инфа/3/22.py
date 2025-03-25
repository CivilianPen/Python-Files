f1 = open('1.csv')
f2 = open('2.csv')
f3 = open('3.csv')
#1: ID 2: Rashod
ans = 0
avto = []
id_avto = []
for i in f1:
    a = (list(map(str,i.split(';'))))
    try:
        if a[3] == '2' or a[3] == '3':
            a[-1] = a[-1].replace(',','.')
            avto.append([int(a[0]),float(a[-1][:-1])])
            id_avto.append(int(a[0]))
    except:
        pass
    
rashod = [0]*50
for i in range(len(avto)):
    rashod[avto[i][0]] = avto[i][1]

vodila = []
for i in f2:
    a = (list(map(str,i.split(';'))))
    if a[-1][:-1] == 'Ульяновск':
        vodila.append(int(a[0]))
        
#1: ID avto 2: dist
poezdki = []
for i in f3:
    a = (list(map(str,i.split(';'))))
    try:
        if int(a[1]) in vodila and int(a[3][3:5]) == 12:
            a[4] = a[-1].replace(',','.')
            poezdki.append([int(a[2]),float(a[4][:-1])])
    except:
        pass

for i in range(len(poezdki)):
    if poezdki[i][0] in id_avto:
        poezdki[i][0] = rashod[poezdki[i][0]]
    else:
        poezdki[i][0] = 0
    
for i in poezdki:
    ans += ((i[0]/100)*i[1])

magaz = ['М2','М14','М21','М44','М49','М54','М60','М77','М81']
tovar_id = [122,124,125,127,128,131,132,135,138,139,140,141,143,144,149,154]
tovars = {
'30':300,'122':500,'124':250,'125':500,'127':100,
'128':120,'131':1000,'132':300,'135':1000,'138':300,
'139':1000,'140':700,'141':300,'143':250,'144':500,
'145':200,'149':300,'154':500,'157' :300
}

f = open('1.csv', 'r', encoding='windows-1251').readlines()
G = []
for i in f:
    x = list(map(str,i.split(';')))
    G.append(x)

count = []
count2 = []
for i in G:
    if i[1][5:7] == '10':
        if i[2] in magaz:
            if int(i[3]) in tovar_id:
                if i[5] == 'Продажа\n':
                    count.append(tovars[i[3]]*int(i[4]))
                else:
                    count2.append(tovars[i[3]]*int(i[4]))
print(int((sum(count)-sum(count2))/1000))

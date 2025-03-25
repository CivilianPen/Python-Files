goods_movement = open('3_1.csv')
goods = open('3_2.csv')
magaz_id = ['M10','M15']
goods_id = dict()
for i in goods:
    arr = list(map(str,i.split(';')))
    if 'Зефир' in arr[2]:
        goods_id[arr[0]]=int(arr[4])
#print(goods_id)
ans = []
for i in goods_movement:
    arr = list(map(str, i.split(';')))
    if arr[-1] == 'Поступление\n':
        if arr[2] in magaz_id:
            if int(arr[1][0:2])<=10:
                if arr[3] in goods_id:
                    ans.append(int(arr[4])*goods_id[arr[3]])
print(sum(ans)/1000)

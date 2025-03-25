f = open('26_20910.txt').readlines()
W = open('test.txt','w')
arr = []
for i in f:
    #[ряд, место]
    x = list(map(int,i.split(' ')))
    arr.append(x)
arr = [[7,7,8],[1,1],[6,6],[5,5],[6,7],[4,4],[2,2],[3,3]]
N = arr[0][0] #занятые места (длина файла)
M = arr[0][1] #количество рядов
K = arr[0][2] #количество мест

arr = sorted(arr[1:],reverse=True)
print(arr)







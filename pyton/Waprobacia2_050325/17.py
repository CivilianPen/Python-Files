f = open('17_17873.txt')
arr = [int(n) for n in f]
count = 0
mx_suma = 0
mi = min(arr)

for i in range(len(arr)-1):
    para = [arr[i],arr[i+1]]
    if para[0]%16==mi or para[1]%16==mi:
        count+=1
        mx_suma=max(mx_suma,sum(para))
print(count,mx_suma)
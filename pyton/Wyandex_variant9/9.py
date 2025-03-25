f = open('9.csv').readlines()
arr = []
for i in f:
    arr.append(list(map(int,i.split(','))))
def get_count(d):
    count = 0
    for i in d:
        if d[i]>=2:
            count+=1
    return count

def get_double(arr):
    suma1 = 0
    suma2 = 0
    nums = {
        arr[0]: 0,
        arr[1]: 0,
        arr[2]: 0,
        arr[3]: 0,
        arr[4]: 0,
        arr[5]: 0,
        arr[6]: 0,
        arr[7]: 0,
    }
    for i in arr:
        nums[i]+=1

    if get_count(nums) >= 2:
        for i in nums:
            if nums[i] >= 2:
                suma1 += i
            else:
                suma2 += i
    return suma1<suma2

count = 0
for i in arr:
    if get_double(i):
        count+=1

print(count)
arr = []
for i in range(500):
    a = input()
    a=a.replace(',','.')
    arr.append(float(a))

ans = -10 ** 20
for i in range(len(arr)):
    s = arr[i]
    if s > ans:
        ans = s
    for j in range(i + 1, len(arr)):
        if abs(arr[j] - arr[j - 1]) <= 10:
            s += arr[j]
            if s > ans:
                ans = s
        else:
            break
print(int(ans))
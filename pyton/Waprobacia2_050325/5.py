for n in range(0,13):
    n_2 = bin(n)[2:]
    arr = [int(i) for i in list(n_2)]
    if sum(arr) % 2 == 0:
        arr.append(0)
        arr[0] = 1
        arr[1] = 0
    else:
        arr.append(1)
        arr[0] = 1
        arr[1] = 1
    res = ''.join([str(n) for n in arr])
    if int(res,2) > 19:
        print(n)
        break
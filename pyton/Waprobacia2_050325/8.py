from itertools import product

arr = product('012345678', repeat = 5)
count = 0
for i in arr:
    string = ''.join(i)
    nechet = ['1','3','7','5']
    if string[0]!='0' and string.count('0') == 1:
        zero_index = string.find('0')
        if zero_index<4:
            if string[zero_index-1] not in nechet and string[zero_index+1] not in nechet:
                count += 1

        else:
            if string[zero_index-1] not in nechet:
                count += 1

print(count)
from itertools import product
words = list(product('АБРТЫ', repeat=5))

for i in range(len(words)):
    W = ''
    for j in words[i]:
        W+=j
    if W.count('Ы')== 0 and W.count('АА')== 0 :
        print(W,i+1)
        break

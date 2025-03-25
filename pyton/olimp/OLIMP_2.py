import itertools
N,W = (map(int,input().split()))

book = []
for i in range(N):
    book.append(list(map(int,input().split())))
    
def Count(array,W):
    pages = []
    Ws = []
    days = 0
    for i in range(N):
        pages.append(array[i][0])
        Ws.append(array[i][1])
    for i in range(N):
        day_book = 0
        C_pages = pages[i]
        if i != 0:
            W = Ws[i-1]
        while C_pages > 0:
            if day_book == 0:
                C_pages -= 10*W
                day_book += 1
            else:
                C_pages -= 10*Ws[i]
                day_book += 1
        days += day_book
    return days

b = list(itertools.permutations(book,len(book)))
d = []
for i in b:
    d.append(Count(list(i),W))
    
print(min(d))

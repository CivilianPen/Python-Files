n = int(input())
stroka = input()
s = []
index = 0
index_del = 0
index_plus = 0
for i in range(len(stroka)):
    if stroka[i].isdigit():
        s.append(int(stroka[i]))
    else:
        s.append(stroka[i])

while s.count('*') !=0 and index < len(s):
    if s[index] == '*':
        s[index] = s[index-1] * s[index+1]
        del s[index-1]
        del s[index]
        index = 0
    index += 1

while s.count('/') !=0 and index_del < len(s):
    if s[index_del] == '/':
        s[index_del] = s[index_del-1] / s[index_del+1]
        del s[index_del-1]
        del s[index_del]
        index_del = 0
    index_del += 1


while s.count('+') !=0:
    if s[index_plus] == '+':
        s[index_plus] = s[index_plus-1] + s[index_plus+1]
        del s[index_plus-1]
        del s[index_plus]
        index_plus = 0
    index_plus += 1

print(int(round(s[0])))

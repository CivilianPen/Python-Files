from math import *
nums = list(map(float, input().split()))
a = nums[0]  #a1
b = nums[1]  #b1
d = nums[2]  #a2
c = nums[3]  #c1 

ans = ['Not','found']

if (a**2+4*d*b-4*d*c) >= 0 and d != 0:
    ans[0] = round((a-sqrt(a**2+4*d*b-4*d*c))/(2*d) , 3)
    ans[1] = round((a+sqrt(a**2+4*d*b-4*d*c))/(2*d) , 3)

if d == 0:
    if a != 0:
        ans = ['Not found']
        ans [0] = round((c/a) - (b/a) , 3)
    else:
        ans = []
        for i in range(-10000, 10000, 1):
            ans.append(i/1000)

if len(ans) > 1 and ans[0] == ans[1]:
    print(ans[0])

else:
    if type(ans[0]) == float:
        print(', '.join(map(str, ans))) # X пересечений
        #print(a*ans[0] + b , d*(ans[1]**2) + c) это Y пересечений
    else:
        print(' '.join(map(str, ans)))

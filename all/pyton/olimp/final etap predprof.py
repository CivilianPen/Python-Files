from math import *
mas = list(map(float,input().split()))

if 2*mas[2] <= mas[3]:
    H = ((mas[3]/2)*sqrt(2))

    lh = 2 * (sqrt((mas[2]**2 - H**2)))

    cs = ((-lh**2)/(2*(mas[2]**2))) + 1

    S_seg = (((acos(cs))/(2*pi)) * pi*(mas[2]**2)) - (lh*H/2)

    S =pi*(mas[2]**2) -  4*S_seg


else:
    S = (mas[3]**2)/2
    
print(round((S-((mas[4]**2)/2)),6))

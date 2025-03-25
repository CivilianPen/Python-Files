a = float(input())
T = float(input())
t = float(input())

V=a*T

if a != 0:
    S = ((a*(T**2))/2)+(V*t*60)+(((V**2))/a)
else:
    S = 0

print(V)
print(S)

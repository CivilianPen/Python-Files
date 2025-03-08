from decimal import Decimal
f = [0]*300

for n in range(300):
  if n<=1:
    f[n]=1/2
  else:
    f[n]=Decimal((n+1)*f[n-1])
    




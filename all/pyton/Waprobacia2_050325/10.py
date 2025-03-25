f = open('10.txt').read()
import re

k = re.findall(' не ', f, flags=0)
k2 = re.findall(' Не ', f, flags=0)

print(len(k2)+len(k))
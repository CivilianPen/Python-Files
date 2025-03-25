f = open('10.txt').read()
import re
start = f.find('ЧАСТЬ ТРЕТЬЯ')
end = f.find('ЧАСТЬ ЧЕТВЁРТАЯ')

k = f[start:end]

for i in range(len(k)):
    if k[i:i+3] == 'бал' or k[i:i+3] == ' бал ':
        print(k[i-10:i+10])


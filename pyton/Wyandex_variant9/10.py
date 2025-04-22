f = open('10.txt', 'r', encoding='windows-1251').read()
import re
start = f.find('ЧАСТЬ ТРЕТЬЯ')
end = f.find('ЧАСТЬ ЧЕТВЁРТАЯ')

k = f[start:end]

print(k.count('бал')-k.count(' бал '))
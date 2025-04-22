import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.binance.com/ru/price/bitcoin'
c = 'css-1bwgsh3'

f = open('Values.txt', 'a')
r = requests.get(url)
print(r)
html = BS(r.text,'html.parser')
t = html.find(class_ = c)

try:
    f.write(str(t.text)+'\n')
except:
    f.write(str(t.text)+'\n')

s = open('Values.txt').readlines()
print(len(s))
data_y = []
data_x = []
data =[]
for i in range(len(s)):
    val = str(s[i][2:11])
    val=val.replace(',','')
    data_x.append(i)
    data_y.append(int(val[:-3]))

plt.plot(data_x, data_y)
plt.axis((0, 100, min(data_y)-1000, max(data_y)+1000))
plt.show()

f.close()



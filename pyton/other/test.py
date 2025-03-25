import requests
from bs4 import BeautifulSoup as BS

url ='https://weather.rambler.ru/world/'
r = requests.get(url)
html = BS(r.text,'html.parser')
f = open('Cities.txt','a')
divs = html.find("div", class_="a5yF").find_all('a')
for div in divs:
    url_for_each_country = ('https://weather.rambler.ru'+div['href'])
    c = requests.get(url_for_each_country)
    html2 = BS(c.text,'html.parser')
    try:
        cities = html2.find("div", class_="yeW5").find_all('a')
    except:
        cities = html2.find("div", class_="tRxV").find_all('a')
    for city in cities:
       f.write(city['href']+'\n')
        

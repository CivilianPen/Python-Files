from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup as BS
cities = ['v-moskve','v-sankt-peterburge','v-parizhe/frantsiya','v-rime','v-abu-dabi','v-stambule','v-belgrade',
'v-tokio','v-londone/velikobritaniya','v-dubae','v-gonkonge','v-nyu-yorke']
        
myTable = PrettyTable(["Номер","Город", "Температура", "Давление", "Ветер" ,"Оосадки"])
cities_RU = []
print('Погода сейчас')
for i in range(len(cities)):
    city = cities[i]
    url ='https://weather.rambler.ru/'+city+'/now/'
    url2 = 'https://weather.rambler.ru/'+city+'/'
    r = requests.get(url)
    html = BS(r.text,'html.parser')
    classes = ['_2RLq','HhSR GyfK','hjtR pressure HbwD aT_0','hjtR wind HbwD aT_0','UAaG']

    V_citi = html.find(class_ = 'RkHg')
    cities_RU.append(V_citi.text[:V_citi.text.rfind(' ')])

    value = [str(i+1)]
    for j in range(len(classes)):
        t =html.find(class_ = classes[j])
        if j == 0:
            s = t.text
            tire = s.find('—')
            value.append(s[:tire])
        elif j == 1:
            value.append(t.text)
        elif j == len(classes)-1:
            os = t.text
            comma = os.find(',')
            value.append(os[comma+2:])
        else:
            so = t.text
            space = so.find(' ')
            value.append(so[space:])
            
    myTable.add_row(value)

print(myTable)

def Week(idi,cities):  
    prognoz = 'dDb8'
    city = cities[idi-1]
    r2 = requests.get('https://weather.rambler.ru/'+city+'/')
    html2 = BS(r2.text,'html.parser')
    t2 = cities = html2.find("div", class_=prognoz).find_all('span')
    db = []
    for result in t2:
        db.append(result.text)
    myTableWeek = PrettyTable(db[0:4])
    dels = []
    for i in range(1,len(db)):
        if (i-1)%6 != 0 and (i-1)%3 != 0:
            dels.append(db[i])

    for i in range(2,len(dels)-4,4):
        myTableWeek.add_row(dels[i:i+4])
    print(myTableWeek)
    
while True:
    print('')
    idi = (input('Введите номер, чтобы узнать прогноз на неделю > '))
    if idi.isdigit():
        print(cities_RU[int(idi)-1]+' на неделю')
        Week(int(idi),cities)
    else:
        break






import os
import webbrowser
import time
webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser(r"C:\Users\nesmo\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"))
webbrowser.register('Google', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
commands = ['off','start','url','app','clear','weather','zapret','exit']
url = [
'https://www.youtube.com/',
'https://tetris.com/play-tetris',
'https://www.speedtest.net/',
'https://school.mos.ru/diary/schedules/schedule',
'https://codeforces.com/',
]
app = [
r"C:\Users\nesmo\Desktop\OBS Studio.url",
r"C:\Users\nesmo\Desktop\Counter-Strike 2.url",
r"C:\Users\nesmo\Desktop\Banana.url",
r"C:\Users\Public\Desktop\Steam.lnk",
r"C:\Users\nesmo\Desktop\Soundpad.url",
r"C:\Users\nesmo\Desktop\goodbyedpi-0.2.3rc3-2\1_russia_blacklist_YOUTUBE.cmd",
]
bye = [
r"C:\Users\nesmo\Desktop\zapret\general.bat",
r"C:\Users\nesmo\Desktop\zapret\service_remove.bat",
]
def main():
    print(commands)
    print('url: 1-youtube,2-tetris,3-speedtest,4-school','5-codeforces')
    print('app: 1-obs,2-cs2,3-banana,4-steam,5-soundpad')
    print('zapret: 0-remove,1-start')
    global a
    a = input('select command >>')
    if (a[0:-1] in commands and a[-1].isdigit()) or (a in commands):
        pass
    else:
        print('not a command')
        main()
        
main()
def weather():
    from prettytable import PrettyTable
    import requests
    from bs4 import BeautifulSoup as BS
    cities = ['v-moskve']
            
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
    print( myTable)
    prognoz = 'dDb8'
    idi = 1
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
    if a == commands[0]:
        os.system('shutdown -s -t 10')
        
        main()
    if a == commands[1]:
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
        os.startfile(r"C:\Users\nesmo\Desktop\Discord.lnk")
        os.startfile(r"C:\Users\nesmo\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
        
        main()
    if a[:3] == commands[2]:
        if int(a[3]) in [4,5]:
            webbrowser.get('Yandex').open_new_tab(url[int(a[3:])-1])
        else:
            webbrowser.get('Google').open_new_tab(url[int(a[3:])-1])
                
        main()
    if a[:3] == commands[3]:
        os.startfile(app[int(a[3:])-1])
        
        main()
    if a == commands[4]:
        os.system('cls')
        
        main()
    if a == commands[5]:
        weather()
        
        main()
    if a[0:-2] == commands[6]:
        if a[-1] == '0':
            os.startfile(bye[1] , 'runas')
        if a[-1] == '1':
            os.startfile(bye[0])
            
        main()
    if a == commands[-1]:
        break


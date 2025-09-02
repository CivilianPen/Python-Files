from requests_html import HTMLSession
from getpass import getpass
from bs4 import BeautifulSoup as BS

url = 'https://app.revolt.chat/server/01J9T96D7VC4W0879DT4EHTBTS/channel/01J9T96D7VYVWXEWZZHTH0WXHR'

session = HTMLSession()

email = 'homyachok223@gmail.com'
username = 'CivilianPen'
a = {"content":"test","socketId":"eThHLqBMAbnaaT49ACYH"}
b = {"content":"testghjfhgjdfgh","nonce":"01JD02KTNTG7EAS0P76E7FA8BR","replies":[]}
r = session.get(url ,auth=(username+'#8194', getpass()))
#r = requests.get(url5,auth=(email, getpass()))

html = BS(r.text,'html.parser')

print(html)





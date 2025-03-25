import string
import random
import webbrowser

def id_generator(size=11, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def go():
    for i in range(a):
        url=r'https://www.youtube.com/watch?v='+id_generator()
        webbrowser.get().open_new_tab(url)
        
while True:
    a = input('enter a number from 1 to infinity (tip: the large numbers can destroy your pc) >>> ')
    if a.isdigit():
        a = int(a)
        go()
    else:
        print("you're bozo, it is not a number")

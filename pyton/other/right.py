import keyboard
import mouse 
import time

isClicking = False
isClicking1 = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер отключен")
    else:
        isClicking = True
        print('Кликер включен')

keyboard.add_hotkey('CTRL + CAPSLOCK', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button='right')
        time.sleep(0.009)

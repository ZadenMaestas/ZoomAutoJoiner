from time import sleep
from colorama import Fore, Back, Style
from datetime import datetime
from pyautogui import alert
import webbrowser

title = open('logo.txt', 'r')
art = title.read()
print(Fore.GREEN + art)
title.close()
true = True
while True:
    rn = datetime.now().strftime('%H:%M')
    print("Checking time"), sleep(0.1), print('.'), sleep(0.1), print('.'), sleep(0.1), print('.'), print(rn)
    if rn == "08:15":
        print("Current Period: Science")
        webbrowser.open_new_tab('redacted')
        alert(text='Current Period: Science', title='Time For Class!', button='OK')
        sleep(59)
    elif rn == "09:17":
        print("Current Period: Math")
        webbrowser.open_new_tab('redacted')
        alert(text='Current Period: Math', title='Time For Class!', button='OK')
        sleep(59)
    elif rn == "10:19":
        print("Current Period: Social Studies")
        alert(text='Current Period: Social Studies', title='Time For Class!', button='OK')
        webbrowser.open_new_tab('redacted')
        sleep(59)
    elif rn == "11:21":
        print("Current Period: Art")
        webbrowser.open_new_tab('radacted')
        alert(text='Current Period: Art', title='Time For Class!', button='OK')
        sleep(59)
    elif rn == "12:23":
        print("Current Period: Lunch, go eat!")
        alert(text='Current Period: Lunch, go eat!', title='Time For Lunch!', button='OK')
        sleep(59)
    elif rn == "13:25":
        print("Current Period: ELA")
        webbrowser.open_new_tab('radacted')
        alert(text='Current Period: ELA', title='Time For Class!', button='OK')
        sleep(59)
    elif rn == "14:27":
        print("Current Period: Music Appreciation")
        webbrowser.open_new_tab('radacted')
        alert(text='Current Period: Music Appreciation', title='Time For Class!', button='OK')
        sleep(59)
    elif rn == "15:25":
        print("School Is Over!")
        alert(text='You can relax now lol', title='School Is Over!', button='OK')
        sleep(59)
    sleep(1)

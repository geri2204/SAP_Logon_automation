from pywinauto import Desktop
from pywinauto import Application
import time
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click

def GetWindow(name):
    for win in Desktop(backend="win32").windows():
        if name in win.window_text() and win.window_text() != "":
            return win
        
def SendCmd(n, cmd, delay = 0.2):
    for i in range(0,n):
        send_keys(cmd)
        time.sleep(delay)

def Run(ertek):
    target_title = "EMP(1)/102 Bekötés megjelenítése: kezdő kép"
    
    # Megtalál és a célablakra fókuszál
    window = GetWindow(target_title)

    if window:
        print(f"Found target window: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # vár

        # Ctrl+f
        send_keys('^f')  # '^' Ctrl

        print("Ctrl+F key combination sent.")
    else:
        print("Target window not found.")

    print("Folyamat befejezve")

    target_title = "EMP(1)/102 Data Finder(adatkereső): Közműbekötés keresése"
    # Megtalál és a célablakra fókuszál
    window = GetWindow(target_title)

    if window:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # vár

        
        send_keys('{TAB}')
        time.sleep(1)
        SendCmd(2,'{RIGHT}')
        send_keys('{SPACE}')
        print("'Más kereső kritérium' - ablakra kattint! Vár!")
        time.sleep(2)
        send_keys('{TAB}')
        print("'Globális korlátozások' - alcímre lép!")

        SendCmd(9,  '{DOWN}')
        print("'Mér.pont megn.' - mezőt megkeresi!")

        send_keys(ertek)
        print("'POD-érték' - BEMÁSOLVA!")

        send_keys('{ENTER}')





        #Várakozás a következő ablak megjelenésére
        time.sleep(2)




    # Megtalál és a célablakra fókuszál


        target_title = "EMP(1)/102 Bekötés megjelenítése:"

        
    window1 = GetWindow(target_title)

    if window1:

        print(f"Célablak megtalálva: {window1.window_text()}")
        window1.set_focus()
        time.sleep(2)  # vár

        send_keys('^a')  #  Ctrl+a
        print("'Bekötés' - KIJELÖLVE!")
        time.sleep(2)
        send_keys('^c')  # Ctrl+c
        print("'Bekötés' - KIMÁSOLVA!")
        time.sleep(1)
        SendCmd(9,'{TAB}',1)
        send_keys('{ENTER}')
        print("'Időszeletek' - gomb megtalálva!")
        time.sleep(1)
        SendCmd(10,'{TAB}')
        print("'ÜK. Szeg.' - mező megtalálva!")
        send_keys('^y')
        send_keys('^c')
        print("'ÜK. Szeg.' - mező KIMÁSOLVA!")


    else:

        target_title = "EMP(1)/102 Információ"


    window = GetWindow(target_title)

    if window:

        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # vár

        print("Nem található a célablak")

        window.set_focus()
        time.sleep(2)  # vár


        print("Nem található a célablak")
        time.sleep(1)  # vár

    else:
        print("Target window not found.")
        time.sleep(1)  # Observe the target window

    print("Folyamat befejezve")

    time.sleep(1)

    window.close()

    time.sleep(1)

    window1.set_focus()


    time.sleep(1)
    send_keys('{ENTER}')
    SendCmd(21,'{TAB}')
    

    send_keys('{ENTER}')

    time.sleep(1)  # Observe the target window


file = open("C:\\Users\\G3909\\Desktop\\forras.txt", "r")

lines = file.readlines()

for line in lines:
    Run(line.replace("\r","").replace("\n",""))
    time.sleep(200)
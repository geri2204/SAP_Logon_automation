from pywinauto import Desktop, Application
import time
from pywinauto.keyboard import send_keys

def GetWindow(name):
    for win in Desktop(backend="win32").windows():
        if name in win.window_text() and win.window_text() != "":
            return win
    return None
        
def SendCmd(n, cmd, delay=0.2):
    for i in range(n):
        send_keys(cmd)
        time.sleep(delay)

def identify_controls(window):
    if window:
        try:
            window.print_control_identifiers()
        except AttributeError as e:
            print(f"Error identifying: {e}")
    else:
        print("Nincs mit identify-olni")

def Run(ertek):
    target_title = "EMP(1)/102 Bekötés megjelenítése: kezdő kép"
    
    # Megtalál és a célablakra fókuszál
    window = GetWindow(target_title)
    identify_controls(window)

    if window:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # Várakozás

        # Ctrl+f
        send_keys('^f')
        print("Ctrl+F kombináció leütve")
    else:
        print("Célablak nem található")
        return

    print("Folyamat befejezve")

    target_title = "EMP(1)/102 Data Finder(adatkereső): Közműbekötés keresése"
    window = GetWindow(target_title)

    if window:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # Várakozás

        send_keys('{TAB}')
        time.sleep(1)
        SendCmd(2, '{RIGHT}')
        send_keys('{SPACE}')
        print("'Más kereső kritérium' - ablakra kattint! Vár!")
        time.sleep(2)
        send_keys('{TAB}')
        print("'Globális korlátozások' - alcímre lép!")

        SendCmd(9, '{DOWN}')
        print("'Mér.pont megn.' - mezőt megkeresi!")

        send_keys(ertek)
        print("'POD-érték' - BEMÁSOLVA!")

        send_keys('{ENTER}')
        time.sleep(2)  # Várakozás a következő ablak megjelenésére

        target_title = "EMP(1)/102 Bekötés megjelenítése:"
        window1 = GetWindow(target_title)

        if window1:
            print(f"Célablak megtalálva: {window1.window_text()}")
            window1.set_focus()
            time.sleep(2)  # Várakozás

            send_keys('^a')  # Ctrl+a
            print("'Bekötés' - KIJELÖLVE!")
            time.sleep(2)
            send_keys('^c')  # Ctrl+c
            print("'Bekötés' - KIMÁSOLVA!")
            time.sleep(1)
            SendCmd(9, '{TAB}', 1)
            send_keys('{ENTER}')
            print("'Időszeletek' - gomb megtalálva!")
            time.sleep(1)
            SendCmd(10, '{TAB}')
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
                time.sleep(2)  # Várakozás

                print("Nem található a célablak")

                window.set_focus()
                time.sleep(2)  # Várakozás

                print("Nem található a célablak")
                time.sleep(1)  # Várakozás
            else:
                print("Nem található a célablak ")
                time.sleep(1)  # Várakozás a célablakra

        print("Folyamat befejezve")

        if window:
            window.close()

        if window1:
            window1.set_focus()

        send_keys('{ENTER}')
        SendCmd(21, '{TAB}')
        send_keys('{ENTER}')
        time.sleep(1)  # Várakozás a célablakra

def main():
    # SAP Logon indítása
    app = Application(backend="win32").start(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")
    print("SAP Logon elindult várunk a keresett ablak megnyitására....")

    # Várunk, amíg megjelenik az ablak
    target_title = "EMP(1)/102 Bekötés megjelenítése: kezdő kép"
    window = None
    while not window:
        window = GetWindow(target_title)
        time.sleep(1)

    if window:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(2)  # Várakozás a célablakra

        identify_controls(window)
    else:
        print("Célablak nem található.")
        return

    # POD-ok kiolvasása és a folyamat lefuttatása
    file_path = "C:\\Users\\G3909\\Desktop\\forras.txt"
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                Run(line.strip())
                time.sleep(20)
    except Exception as e:
        print(f"Nem olvasható a forrásfájl: {e}")

if __name__ == "__main__":
    main()

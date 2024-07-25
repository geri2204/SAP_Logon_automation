from pywinauto import Desktop, Application
import pyautogui
import time
from pywinauto.keyboard import send_keys
import pyperclip
import datetime

#Ablak megtalálása/beállítása:
def GetWindow(name):
    for win in Desktop(backend="win32").windows():
        if name in win.window_text() and win.window_text() != "":
            return win
    return None

#Függvény a többszörös billentyűparancsok kiadására:
def SendCmd(n, cmd, delay=0.2):
    for i in range(n):
        send_keys(cmd)
        time.sleep(delay)

"""
def identify_controls(window):
    if window:
        try:
            window.print_control_identifiers()
        except AttributeError as e:
            print(f"Error identifying: {e}")
    else:
        print("Nincs mit identify-olni")
"""


# Funkció egy kép megtalálására és rákattintására
def find_and_click(image_path):
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Confidence érték finomhangolható
    if location is not None:
        pyautogui.click(pyautogui.center(location))
        print(f'Rákattintott:  {image_path}')
    else:
        print(f'{image_path} - GUI elem nem található!')


#Hibakezelés
def check_error():
    send_keys('{TAB}')
    send_keys('{ENTER}')
    pyperclip.copy("Hibás\n")

def check_missing():
    find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\back.png') 


#Fő függvény. Itt hajtja végre a program a vezérlést:
def Run(ertek, outFile, open = False):
    wait_time = 0.1


    # Megtalál és a célablakra fókuszál
    window = GetWindow("EMP(1)/102 Bekötés megjelenítése: kezdő kép")
    #identify_controls(window)

    #Ha hibás volt az előző ciklus akkor nem fut le
    if window and not open:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(wait_time)  # Várakozás

        # Ctrl+f
        send_keys('^f')
        print("Ctrl+F kombináció leütve")
    elif not open:
        print("Célablak nem található")
        return True

    print("Folyamat befejezve")

    window = GetWindow("EMP(1)/102 Data Finder(adatkereső): Közműbekötés keresése")

    if window:
        print(f"Célablak megtalálva: {window.window_text()}")
        window.set_focus()
        time.sleep(wait_time)  # Várakozás

        # Kattintás a 'Más kereső kritériumok' fülre
        find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\mas kereso kriteriumok.png')
        time.sleep(1)  # Vár egy kicsit, hogy az új fül betöltődjön
        print("'Más kereső kritérium' - ablakra kattint!")

        time.sleep(wait_time)

        # Belépés a 'Mér.pont megn.' szövegmezőbe
        find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\mer pont megn.png')
        send_keys('{TAB}')
        print("'Mér.pont megn.' - mezőt megtalálva!")
        # POD bemásolása a forras.txt soraiból a szovegdobozba
        send_keys('^a')
        pyperclip.copy(ertek)
        send_keys('^v')

        #send_keys(ertek)
        print("'POD-érték' - BEMÁSOLVA!")

        send_keys('{ENTER}')

    time.sleep(0.5)  # Várakozás a következő ablak megjelenésére

    window1 = GetWindow("EMP(1)/102 Bekötés megjelenítése:")

    if window1:
        print(f"Célablak megtalálva: {window1.window_text()}")
        window1.set_focus()
        time.sleep(wait_time)  # Várakozás

        send_keys('^a')    # Ctrl+a
        print("'Bekötés' - KIJELÖLVE!")
        time.sleep(wait_time)
        send_keys('^c')  # Ctrl+c
        print("'Bekötés' - KIMÁSOLVA!")

        outFile.write(pyperclip.paste()+" ")

        time.sleep(wait_time)  # Várakozás
        pyautogui.scroll(-4000) # Lejjebb kördítés
        
        #Ellenőrzés hogy megfelelő-e a POD értéke
        try:
            find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\idoszeletek.png')
        except:
            print("Hibás POD")
            check_error()
            outFile.write("Hibás\n")
            return True
        else:

            print("'Időszeletek' - Gomb lenyomva")
            time.sleep(1)

            try:
                find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\ukszeg.png')
            except:
                outFile.write("Hibás\n")
                check_missing()
                return False


            print("'ÜK. szegm.' - Oszlop kiválasztva")
            send_keys('{DOWN}')    # Down arrow, hogy kiválaszthassuk a kellő cellát
            send_keys('^y')     # Ctrl+y a cella egyéni kijelölésére
            send_keys('^c')     # Ctrl+c
            outFile.write(pyperclip.paste()+"\n")
            print("'ÜK. szegm.' - Érték sikeresen kimásolva!")

            #'Időszeletek' ablak bezárása
            find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\close.png')   # X -eljük ki a kis ablakot
            time.sleep(wait_time)
            print("'Időszeletek' - Felugró ablak bezárva!")

            #Visszatérés az előző oldalra (Ahol ctrl+f -el újra POD-ot adhatunk meg)
            find_and_click('C:\\Users\\G3909\\Desktop\\SAP_automation\\back.png')    # Kis zöld nyilacska lenyomása
        
        print("Visszalépés megtörtént!")
        time.sleep(wait_time)
        return False
            

          

def main():
    startTime = datetime.datetime.now()


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
        time.sleep(0.5)  # Várakozás a célablakra

        #identify_controls(window)
    else:
        print("Célablak nem található.")
        return

    # POD-ok kiolvasása és a folyamat lefuttatása
    # forras.txt fájlban szerepelnek a POD-ok felsorakoztatva, egymás alatt
    
    file_path = "C:\\Users\\G3909\\Desktop\\SAP_automation\\forras.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()
        error = False

        output = open("output.txt","+a")

        for line in lines:
            error = Run(line.strip(), output, error)
            time.sleep(0.1)

        output.close()

    print("Runtime: "+str(datetime.datetime.now()-startTime))

if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
import time
from ahk import AHK
from ahk.window import Window
import pyautogui
import pytesseract
from PIL import Image
import random

ahk = AHK()

def clicked1():
    time.sleep(5)
    win1 = str(ahk.active_window)
    StartINDEX = win1.find('=') + 1
    EndINDEX = win1.find('>')
    global WindowID1
    WindowID1 = win1[StartINDEX:EndINDEX]
    messagebox.showinfo('ID '+WindowID1, 'Айдишник первого окна записан!')

def clicked3():
    okno1 = Window(ahk, ahk_id=WindowID1)
    time.sleep(5)
    while True:
        time.sleep(10)
        okno1.activate()
        startButton = pyautogui.locateOnScreen('01.png', confidence=0.7)  # ===> Ищет в окне №2 координаты 'ПРИНЯТЬ'
        if startButton == None:
                im2 = pyautogui.screenshot('my_screenshot.png', region=(1585, 900, 278, 38))
                img = Image.open('my_screenshot.png')
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                text = pytesseract.image_to_string(img)

                print(text)  # Капча

                startButton2 = pyautogui.locateOnScreen('ololo.png', confidence=0.7)
                pyautogui.click(x=startButton2[0], y=startButton2[1])
                pyautogui.mouseDown();
                pyautogui.mouseUp()
                time.sleep(5)
                for i in range(len(text)):
                    pyautogui.press(text[i])
                time.sleep(5)
                startButton3 = pyautogui.locateOnScreen('lol.png', confidence=0.7)
                pyautogui.click(x=startButton3[0], y=startButton3[1])
                pyautogui.mouseDown();
                pyautogui.mouseUp()
                time.sleep(15)

        else:
            print('Нет')
            startButton4 = pyautogui.locateOnScreen('oops.png', confidence=0.7)
            startButton5 = pyautogui.locateOnScreen('mysor.png', confidence=0.7)
            if startButton4 == None or startButton5 == None:
                print('Админ, палево!')
                pyautogui.press('F8')
                time.sleep(2)
                pyautogui.write('reconnect', interval=0.25)
                time.sleep(2)
                pyautogui.press('Enter')

            else:
                print('Заебись')
                pyautogui.moveTo(random.randint(1,1920), random.randint(1,1080), 2)
                pyautogui.press('space')




window = Tk()
window.title("ФАРМ")



btn1 = Button(window, text="ПОЛУЧИТЬ И ЗАПИСАТЬ ID ОКНА №1", command=clicked1)
btn1.grid(column=1, row=1)


btn3 = Button(window, text="НАЧАТЬ ФАРМИТЬ", bg="black", fg="yellow", command=clicked3)
btn3.grid(column=1, row=3)

window.mainloop()
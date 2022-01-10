from tkinter import *
from PIL import Image
import pyautogui,keyboard,time
import pyscreenshot as ImageGrab



# Reaction time 

def react():
    clickColor = (75, 219, 106)
    while True:
        if keyboard.is_pressed('q'):
                print("ymd")
                break
        screen = pyautogui.screenshot()
        current = screen.getpixel((pyautogui.position()))
        if current == clickColor:
            pyautogui.click()
            break

def aim():
    counter = 0
    while True:
        if keyboard.is_pressed('q'):
            print("ymd")
            break
        screen = pyautogui.screenshot()
        targetLocation = pyautogui.locateOnScreen('target.png', confidence = 0.5)
        if targetLocation:
            pyautogui.moveTo(targetLocation)
            pyautogui.click()
            counter += 1
        if counter == 31:
            break

def vm():
    screen = ImageGrab.grab(bbox = (752,222,1174,618))
    screen.save('result.png')
    time.sleep(4)
    for sq in pyautogui.locateAllOnScreen('square.JPG', confidence = 0.7):
        if keyboard.is_pressed('q'):
            print("ymd")
            break
        pyautogui.click(sq[0], sq[1])
        print(sq[0],sq[1])
         


window = Tk()

reaction = Button(window, text = 'Reaction Test')
reaction.pack()
reaction.config(command = react)

aimtest = Button(window, text = "Aim")
aimtest.pack()
aimtest.config(command = aim)

vmtest = Button(window, text = "Visual Memory")
vmtest.pack()
vmtest.config(command = vm)
window.mainloop()
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


time.sleep(2)

def click(x,y):
    win32api.setCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENT_LEFTDOWN)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENT_LEFTUP)

while keyboard.is_pressed('q') == False:

    pic=pyautogui.screenshot(region=(660,350,600,400))

    width,height = pic.size

    for x in range (o, width, 5):
        for y in range (o, height, 5):

            r,g,b= pic.getpixel((x,y))

            if b==195:
                click(x+660, y+350)
                time.sleep(0.05)
                break 

import pyautogui as pag
import time

#x and y coordinates for alch position in fullscreen 1080p
x = 1879
y = 867

for i in range(int(input("How many?"))):
    pag.moveTo(x,y,1)
    pag.click()
    pag.click()
    time.sleep(4)

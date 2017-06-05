import random
import pyautogui as pag
import time

while True:
    x = random.randrange(25,55)
    pag.click(clicks=2, interval=.4)
    time.sleep(x)

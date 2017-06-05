import time, pyautogui, random
while True:
    pyautogui.click(clicks=2, interval=.40)
    x = random.randrange(45,55,1)
    time.sleep(x)

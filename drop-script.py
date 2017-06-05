#Drop script for barbarian fishing
'''Gets x, y coordinates for first two items in inventory, and on below y to
establish the constants spaces between them.  Then requires the spacing for
the drop option.  Afterwards, script will run forever without issue.'''
import pyautogui as pag
input("Place cursor at first item")
x1, y1 = pag.position()
input('Place cursor at second item in inventory")
x2, y2 = pag.position()

xrel = x2-x1

input("Place cursor at the the first item in second row")
x3, y3 = pag.position()

yrel = y3-y1

input("Place cursor in on drop option")
x4, y4 = pag.position()

droprel = y4-y1

drop_num = int(input("How many items to drop?"))


for i in range(drop_num):
      localx = x1
      pag.moveTo(x1, y1)
      pag.rightClick()
      pag.moveTo(x1, y+droprel)
      pag.click()
      

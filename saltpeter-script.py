# this script will be for combining things, like potions,
# saltpeter and bows with bowstring.
import pyautogui as pag
import time

# constant for pixel distance from item to submenu option withdraw x
y_constant = 85

# constant for num to withdraw
num_to_withdraw = 14

# constant time for wa# iting - can be tweaked per activity (seconds)

wait_time = 33

# cursor travel time constant
cursor_travel_time = 1

# gets bank window coordinates
input("Place your cursor at the bank window")
bank_x, bank_y = pag.position()

# gets position of first item
input("Place cursor at first item in bank")
item1_x, item1_y = pag.position()

# gets position of second item
input("Place cursor at second item in bank")
item2_x, item2_y = pag.position()

# gets position of bank inventory button
input("Place cursor at the bank all option")
bank_items_x, bank_items_y = pag.position()

# get the bank x button
input("Place cursor at the x to close bank window")
close_x, close_y = pag.position()

# gets item one pos in inventory
input("Place cursor at item one in inventory")
inv1_x, inv1_y = pag.position()

# gets item two pos in inventory
input("Place cursor at item two in inventory")
inv2_x, inv2_y = pag.position()

# gets position of menu option to combine
# input("Place cursor on menu option to combine items")
# menu_x, menu_y = pag.position()

# gets position of make all option in menu
# input("Right click, then place cursor at the make all option")
# make_x, make_y = pag.position()

while (True):
    # open bank
    pag.moveTo(bank_x, bank_y, cursor_travel_time)
    pag.click()
    # deposit inventory
    pag.moveTo(bank_items_x, bank_items_y, cursor_travel_time)
    pag.click()
    # withdraw first item
    pag.moveTo(item1_x, item1_y, cursor_travel_time)
    pag.rightClick()
    pag.moveTo(item1_x, item1_y + y_constant, cursor_travel_time)
    pag.click()
    time.sleep(1)
    pag.typewrite("14", interval=.25)
    pag.press("enter")
    # withdraw second item
    pag.moveTo(item2_x, item2_y, cursor_travel_time)
    pag.rightClick()
    pag.moveTo(item2_x, item2_y + y_constant, cursor_travel_time)
    pag.click()
    time.sleep(1)
    pag.typewrite("14", interval=.25)
    pag.press("enter")
    # close bank
    pag.moveTo(close_x, close_y, cursor_travel_time)
    pag.click()
    # move to first item in inventory
    pag.moveTo(inv1_x, inv1_y, cursor_travel_time)
    pag.click()
    # move to second item in inventory
    pag.moveTo(inv2_x, inv2_y, cursor_travel_time)
    pag.click()
    time.sleep(wait_time)

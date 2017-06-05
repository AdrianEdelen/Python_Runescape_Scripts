# this script will be for combining things, like potions,
# saltpeter and bows with bowstring.
import pyautogui as pag
import time

# constant for pixel distance from item to submenu option withdraw x
y_constant = 85

# constant for num to withdraw
num_to_withdraw = 27

# constant time for waiting - can be tweaked per activity (seconds)

wait_time = 60

# cursor travel time constant
cursor_travel_time = 1

# gets bank window coordinates
input("Place your cursor at the bank window")
bank_x, bank_y = pag.position()

# gets position of logs in bank
input("Place cursor at the logs in your bank")
bank_log_x, bank_log_y = pag.position()

# get the bank x button
input("Place cursor at the x to close bank window")
close_x, close_y = pag.position()

# gets knife pos in inventory
input("Place cursor at the knife in your inventory")
knife_x, knife_y = pag.position()

# gets item two pos in inventory
input("Place cursor at the logs in your inventory")
log_x, log_y = pag.position()

# gets position of menu option to combine
input("Place cursor on menu option to combine items")
menu_x, menu_y = pag.position()

# gets position of make x option in menu
input("Right click, then place cursor at the make x option")
make_x, make_y = pag.position()

while (True):
    # open bank
    pag.moveTo(bank_x, bank_y, cursor_travel_time)
    pag.click()
    # deposit inventory
    pag.moveTo(log_x, log_y, cursor_travel_time)
    pag.rightClick()
    pag.moveTo(log_x, log_y+y_constant, cursor_travel_time)
    pag.click()
    time.sleep(1)
    pag.typewrite("27", interval=.25)
    pag.press("enter")
    # withdraw logs
    pag.moveTo(bank_log_x, bank_log_y, cursor_travel_time)
    pag.rightClick()
    pag.moveTo(bank_log_x, bank_log_y + y_constant, cursor_travel_time)
    pag.click()
    time.sleep(1)
    pag.typewrite("27", interval=.25)
    pag.press("enter")
    # close bank
    pag.moveTo(close_x, close_y, cursor_travel_time)
    pag.click()
    # move to knife in inventory
    pag.moveTo(knife_x, knife_y, cursor_travel_time)
    pag.click()
    # move to logs in inventory
    pag.moveTo(log_x, log_y, cursor_travel_time)
    pag.click()
    # move to item to be made
    pag.moveTo(menu_x, menu_y, cursor_travel_time)
    pag.rightClick()
    pag.moveTo(make_x, make_y, cursor_travel_time)
    pag.click()
    time.sleep(1)
    pag.typewrite("27", interval=.25)
    pag.press("enter")
    time.sleep(wait_time)

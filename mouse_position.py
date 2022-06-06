import pyautogui as gw
import time
import keyboard

print('find my mouse position after 5 seconds...')
time.sleep(5)

print('The position of the cursor is : ', gw.position())
print('Screen resolution is : ', gw.size())
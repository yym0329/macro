import pyautogui as gw
import time
import keyboard

print('find my mouse position after 5 seconds.')
time.sleep(5)

print(gw.position())
print('화면 해상도: ', gw.size())
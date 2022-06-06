import pyautogui as gw
import time
import keyboard

print('Start the macro after 5 seconds...')
time.sleep(5)

# print(gw.position())
# print('화면 해상도: ', gw.size())


click_times = 2
mouse_position = (1338, 613)

escape = False
while(1):
  gw.press('f5')
  time.sleep(0.1)
  gw.press('enter')
  time.sleep(0.7)
  for i in range(click_times):
    gw.click(*mouse_position, 1)
    time.sleep(0.1)
    if keyboard.is_pressed('esc'):
      escape = True
  if escape:
    break
  

  
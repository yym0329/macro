import pyautogui as gw
import time
import keyboard

print('5초 뒤 매크로를 실행합니다.')
time.sleep(5)

# print(gw.position())
# print('화면 해상도: ', gw.size())


click_times = 8
escape = False

while(1):
  gw.press('f5')
  time.sleep(0.1)
  gw.press('enter')
  time.sleep(0.2)
  for i in range(click_times):
    gw.click(1318, 923, 1)
    time.sleep(0.1)
    if keyboard.is_pressed('esc'):
      escape = True
  if escape:
    break
  time.sleep(0.5)

  
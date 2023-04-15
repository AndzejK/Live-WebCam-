import pyautogui
import time
position=pyautogui.position()
print(position)
pyautogui.doubleClick(132,246)
time.sleep(1)
pyautogui.click(375,137)
pyautogui.hotkey('command', 'right')
pyautogui.hotkey('enter')
# add a delay before typing the text
time.sleep(1)
text_v0="Well, took a while to figure it out and stil a a don't think is the best solution\n"
text_v1="Test test test"
pyautogui.press(text_v1, interval=0.2) #typewrite() AND write() AND .press()
# for char in text_v0:
#     pyautogui.press(char)
#     time.sleep(0.1)

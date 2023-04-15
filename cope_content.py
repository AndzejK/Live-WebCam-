import pyautogui
import time
import pyperclip
position=pyautogui.position()
print(position)
# files under nav menu on VS
pyautogui.doubleClick(132,246)
# Cliking the file abc.txt the beginning of it
pyautogui.click(375,137)
# select all text
pyautogui.hotkey("command","a")
# copy all text
pyautogui.hotkey("command","c")
# Using standard Python Lib
copied_txt=pyperclip.paste()

#
pyautogui.alert(copied_txt)
print(copied_txt)
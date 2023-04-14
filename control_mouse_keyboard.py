import pyautogui

position=pyautogui.position()
print(position)
# pyautogui.moveTo(151,158,duration=1)
# moves a mouse from point where I provided and this case from 151,158 to 100,0
# pyautogui.move(100,0,duration=1)

# pyautogui.moveTo(151,158) # the mouse is moved to this position
# pyautogui.click()
# pyautogui.click(151,158) # click a place based on coordinates without moving a mouse

# pyautogui.click(151,158,button='right') # clicks in this position but uses right button!


pyautogui.moveTo(1064,445,duration=1)
pyautogui.click()
pyautogui.drag(200,0,duration=1,button='left')
pyautogui.drag(0,-200,duration=1,button='left')
pyautogui.drag(-200,0,duration=1,button='left')
pyautogui.drag(0,200,duration=1,button='left')



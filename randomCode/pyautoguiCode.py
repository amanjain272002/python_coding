import pyautogui
screenWidth, screenHeight = pyautogui.size()

# # get resolution
# print(screenHeight," ",screenWidth)

# # get the current cursor position
# x,y = pyautogui.position()
# print(pyautogui.position())

# # check if the cursor is on screen
# print(pyautogui.onScreen(x,y))

# # move the mouse 
# pyautogui.moveTo(100,500,2)

# # move the ouse relative to the current position
# pyautogui.moveRel(500,100)

# # drag the mouse
# pyautogui.dragTo(200,300,duration=2)

# # drag rel
# pyautogui.dragRel(50,-100)

# pyautogui.click()
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)
# pyautogui.click(100,10,duration=2)

# pyautogui.scroll(200)

# keyboard operation
pyautogui.write("Hello! ")
pyautogui.write("welcome")

pyautogui.hotkey("ctrl","c")
pyautogui.hotkey("ctrl","v")
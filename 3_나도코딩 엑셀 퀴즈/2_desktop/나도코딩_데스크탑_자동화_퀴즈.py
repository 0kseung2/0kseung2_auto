import pyautogui

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.hotkey("enter")

pyautogui.sleep(0.25)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isMaximized == False:
    w.maximize()

pyautogui.moveTo(487,113, duration=1)
pyautogui.click()

pyautogui.moveTo(297,358, duration=1)
pyautogui.click()

import pyperclip
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)

w.close()

# pyautogui.moveTo(1156,683, duration=1)
# pyautogui.click()

pyautogui.sleep(0.5)
pyautogui.press("n")


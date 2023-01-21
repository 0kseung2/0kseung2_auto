#엑셀에서 회사1 클릭 #102,388
#ctrl + c
#마우스를 소속으로 가져감
#마우스를 한번 클릭
#소속 더블클릭 후
#ctrl + v

import pyautogui

# pyautogui.mouseInfo()
w = pyautogui.getWindowsWithTitle("회사")[0]
w.activate()
#엑셀에서 회사1 클릭
pyautogui.moveTo(102,388, duration=1)
pyautogui.doubleClick()

#ctrl + c
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
    
    #마우스를 소속으로 가져감
    
while True:
    pyautogui.moveTo(1604,649, duration=1)
    pyautogui.doubleClick()

    #ctrl + v
    pyautogui.hotkey("ctrl", "v")
    
    #마우스를 상단으로 가져감
    #f2, end, f2 누르고 ctrl+a, ctrl+c함
    
    pyautogui.moveTo(561,22, duration=1)
    pyautogui.click()
    pyautogui.press("f2")
    pyautogui.press("right")
    pyautogui.press("f2")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    
    
    
    #마우스를 이름으로 가져감
    # pyautogui.moveTo(209,i, duration=1)
    # pyautogui.click()
    # pyautogui.click()
    # pyautogui.doubleClick()
    # pyautogui.hotkey("ctrl", "a")
    # pyautogui.hotkey("ctrl", "c")

    # 위에서 복사 후 이름으로 마우스 이동 후 복사 붙여넣기
    pyautogui.moveTo(1753,764, duration=1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")

    #마우스를 상단으로 가져감
    #f2, end, f2 누르고 ctrl+a, ctrl+c함
    
    pyautogui.moveTo(561,22, duration=1)
    pyautogui.click()
    pyautogui.press("f2")
    pyautogui.press("right")
    pyautogui.press("f2")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    
    
    
    #마우스를 정보로 가져감
    #316,388
    # pyautogui.moveTo(316,i, duration=1)
    # pyautogui.click()
    # pyautogui.click()
    # pyautogui.doubleClick()
    # pyautogui.hotkey("ctrl", "a")
    # pyautogui.hotkey("ctrl", "c")

    # 위에서 복사 후 이름으로 마우스 이동 후 복사 붙여넣기
    #1906,644
    pyautogui.moveTo(1906,644, duration=1)
    pyautogui.click()
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")

    pyautogui.sleep(0.25)
    # next_slide = pyautogui.locateAllOnScreen("next_slide.png", confidence=0.8)
    # pyautogui.click(next_slide)

    # 2222,1258
    pyautogui.moveTo(2222,1258, duration=0.25)
    pyautogui.click()


     #마우스를 상단으로 가져감
    #f2, end, f2 누르고 ctrl+a, ctrl+c함
    
    pyautogui.moveTo(561,22, duration=1)
    pyautogui.click()
    pyautogui.press("f2")
    pyautogui.press("down")
    pyautogui.press("left")
    pyautogui.press("left")
    pyautogui.press("f2")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

import pyautogui
pyautogui.sleep(3) #3초 대기
# print(pyautogui.position())

# pyautogui.click(94, 20, duration=1) #1초 동안 (94, 20)로 이동 후 좌표를 마우스 클릭 
# #pyautogui.click는 pyautogui.mouseDown() 이랑 pyautogui.mouseUp을 합친거
# pyautogui.mouseDown()
# pyautogui.mouseUp() 
# drag and drop 같은 걸 할 때 마우스 다운 , 마우스 업 이용

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(400, 400)
# pyautogui.mouseDown() #마우스 버튼을 누른 상태
# pyautogui.moveTo(500, 500)
# pyautogui.mouseUp() # 마우스 뗀 상태

pyautogui.sleep(3) #3초 대기
# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1357, 507)
# pyautogui.drag(100, 0) #현재 위치 기준으로 x100만큼, y0만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) #너무 빠른 동작으로 drag 수행이 안될때는 duration 설정하기
# pyautogui.dragTo(1557, 507, duration=0.25) #절대 좌표 기준으로 x 1557, y 507로 드래그

pyautogui.scroll(-800) #양수이면 위 방향으로, 음수이면 아래방향으로 300만큼 스크롤.

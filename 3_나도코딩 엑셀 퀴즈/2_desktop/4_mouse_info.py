import pyautogui
# pyautogui.FAILSAFE = False #마우스를 네 귀퉁이에 갖다 놓아도 실행이 종료되지 않음. 가급적 사용 안하는 걸 추천
pyautogui.PAUSE = 1 #모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)
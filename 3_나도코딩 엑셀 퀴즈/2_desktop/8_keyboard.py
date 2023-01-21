import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345") #메모장에 글자 입력
# pyautogui.write("NadoCoding", interval=0.25) #글자 천천히 적기
# pyautogui.write("나도코딩") # 한글은 안적힘

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, 1, a 순서대로 적고 enter 입력
#automate the boring stuff with python 검색하고 홈페이지 들어가면 여러 키들이 있음. 참고하기

# 특수문자
# shift 4 -> $
# pyautogui.keyDown("shift") #shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

#조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") #keyDown 후 keyUp 하는 건 press("a")랑 똑같음
# pyautogui.keyUp("ctrl") # Ctrl + A

#간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift" ,"a")
#Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고

# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") #클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    
my_write("나도코딩")

# 자동화 프로그램
#win :ctrl + alt + del
#mac : cmd + shift + option + q


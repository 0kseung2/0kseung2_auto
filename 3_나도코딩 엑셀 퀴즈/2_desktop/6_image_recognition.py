import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png") # 없는 이미지, 이미지를 찾지 못하면 None이라고 출력
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"): #한 화면에서 똑같은 이미지 여러개 존재
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png") #제일 먼저 발견된 체크박스만 클릭
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

#속도 개선
#1. GrayScalte 여러색이 들어가 있는 이미지를 흑백으로 전환
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

#2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1975, 861, 2199-1975, 1006-861))
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
#1975,861 
#2199,1006 

#3. 정확도 조정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.9) #90%
# pyautogui.moveTo(trash_icon)
# print(trash_icon)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() #시작시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() #종료시간 설정
#     if end - start > timeout: #지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()
# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)
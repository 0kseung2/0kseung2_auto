import pyautogui
#스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") #파일로 저장

# pyautogui.mouseInfo()
#30,17 46,129,185 #2E81B9

pixel = pyautogui.pixel(30, 17)
print(pixel) #moustInfor를 해서 가져왔떤 RGB 값과 똑같은 값을 가져옴.

# print(pyautogui.pixelMatchesColor(30, 17, (46,129,185)))
# print(pyautogui.pixelMatchesColor(30, 17, pixel))
print(pyautogui.pixelMatchesColor(30, 17, (46,129,186)))
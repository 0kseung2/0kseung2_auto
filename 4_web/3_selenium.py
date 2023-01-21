from selenium import webdriver
from selenium.webdriver.chrome.service import Service


browswer = webdriver.Chrome("./chromedriver.exe")

browswer.get("http://daum.net")

while True:
    pass
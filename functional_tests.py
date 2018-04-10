from selenium import webdriver

browser = webdriver.Firefox(executable_path="/mnt/c/Users/Anthony/AppData/Local/Programs/Python/Python36/Scripts/geckodriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
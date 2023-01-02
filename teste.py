from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/caiom/Downloads/chromedriver.exe')
driver.get('http://www.python.org')
driver.get('PUT YOUR LINK HERE')
driver.fullscreen_window()

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/caiom/Downloads/chromedriver.exe')
driver.get('http://www.python.org')
driver.get('https://www.google.com/search?q=cu+de+macho&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjjrp7Y-7T4AhXru5UCHag6Bp0Q_AUoAXoECAEQAw&biw=1920&bih=929#imgrc=YePUFSabntQMuM')
driver.fullscreen_window()


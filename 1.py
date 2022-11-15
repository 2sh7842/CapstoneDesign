from selenium import webdriver

driver = webdriver.Chrome('/Users/2sh7842/capde/chromedriver')

driver.implicitly_wait(3)

driver.get('https://ko.infobyip.com')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

ip_address = str(sys.argv[1])

options = webdriver.ChromeOptions()
options.add_argument("headless")
#options.add_argument("--headless")
mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(ChromeDriverManager().install())
 
# 모든 동작마다 크롬브라우저가 준비될 때 까지 최대 5초씩 대기
driver.implicitly_wait(3)

driver.get("https://ko.infobyip.com/")
time.sleep(3)

element = driver.find_element_by_id("query")

element.send_keys("{}".format(ip_address))
element.send_keys("\n")

driver.quit()
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import csv
from gtts import gTTS
import playsound
import os
import time
import jpype
import asposecells

#jpype.startJVM()
#from asposecells.api import Workbook

source = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
soup = BeautifulSoup(source.content,"html.parser")

table = soup.find('table',{'class':'table-col'})
data = []

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            weather = tds[1].text
            temp = tds[5].text
            rain = tds[8].text
            if weather == "\xa0" :
                weather = "맑음"
            if rain == "\xa0" : 
                rain = "강수없음"

            print("{0} {1} {2} {3}".format(point,temp,weather,rain))
            data.append([point,temp,weather,rain])

print(data)

with open('weather.txt','w') as f:
    f.write('지역, 온도, 날씨, 강수량\n')
    for i in data:
        f.write('{0},{1}도,{2},{3}\n'.format(i[0],i[1],i[2],i[3]))


##  ip 코딩자리######################################

import socket
import re 

myIP=socket.gethostbyname(socket.gethostname())
print(myIP)
myIP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myIP.connect(("www.naver.com",443))
print(myIP.getsockname()[0])

URL='http://ipconfig.kr'
response=requests.get(URL) 
#print(response.text)
myIP_1=re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', response.text)[1]
print(myIP_1) #외부 IP를 볼 수 있다.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

ip_address = str(myIP_1)
options = webdriver.ChromeOptions()
options.add_argument("headless")
#options.add_argument("--headless")
mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(ChromeDriverManager().install())
 
# 모든 동작마다 크롬브라우저가 준비될 때 까지 최대 5초씩 대기
#driver.implicitly_wait(3)

driver.get("https://ko.infobyip.com/")
time.sleep(1)


driver.quit()

#######################################################

area = "부산"  # 이 부분에 ip에서 나온 값 대입

csv = pd.read_csv('/Users/2sh7842/capde/weather.txt',\
        names = ['area', 'degree', 'weather', 'rain'],
        \
                encoding = 'utf-8')


find_row = str(csv.loc[(csv['area'] == area)])[-25:]

#print(f"output: {find_row} {type(find_row)}")
print("output: {}".format(find_row))

#text1 = find_row
#file = open("test_text1.txt", "w")
#file.write(text1)
#file.close()

#workbook = Workbook('/Users/2sh7842/capde/weather.csv');
#workbook.save("Output.txt")
#jpype.shutdownJVM()

tts = gTTS(
    text= str(find_row),
    lang='ko')

tts.save('ex_ko.mp3')

playsound.playsound('ex_ko.mp3')




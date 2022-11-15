import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import csv

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
            print("{0:<7}{1:<7}{2:<7}{3:<7}".format(point,temp,weather,rain))
            data.append([point,temp,weather,rain])

print(data)

with open('weather.csv','w') as f:
    f.write('지역, 온도, 날씨, 강수량\n')
    for i in data:
        f.write('{0},{1},{2},{3}\n'.format(i[0],i[1],i[2],i[3]))

#area = "부산"

#csv = pd.read_csv('/Users/2sh7842/capde/weather.csv',\
#        names = ['area', 'degree', 'weather', 'rain'],
#        \
#                encoding = 'utf-8')


#find_row = csv.loc[(csv['area'] == area)]

#print(find_row)



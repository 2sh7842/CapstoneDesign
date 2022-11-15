import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt


source = requests.get('https://ko.infobyip.com')
soup = BeautifulSoup(source.content,"html.parser")
print(source.content)

table = soup.find('table',{'class':'results wide home'})
data = []


for tr in table.find_all('tr'):
    td = list(tr.find_all('td'))
    if tds.find('a'):
            Area = td.find('a').text
            print("{0}".format(Area))
            data.append([Area])


print(data)


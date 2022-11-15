import pandas as pd
import json
import csv

#with open('/Users/2sh7842/capde/weather.csv', 'w', encoding='UTF8') as f:
#    json.dump(some_dict, f, ensure_ascii=False)

#reading_file = open('/Users/2sh7842/capde/weather.csv', 'rt', encoding ='UTF8')

area = "부산"

csv = pd.read_csv('/Users/2sh7842/capde/weather.csv',\
        names = ['area', 'degree', 'weather', 'rain'],
        \
                encoding = 'utf-8')


find_row = csv.loc[(csv['area'] == area)]

#find_row = find_row.iloc[:,:4]

print(find_row)



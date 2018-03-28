# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json


# retailer = 'costco'
retype = 'note'
companys = {'walmart': [0] * 3, 'costco': [0] * 3, 'kroger': [0] * 3, 'walgreens': [0] * 3, 'amazon': [0] * 3, 
           'Lidl Deutschland': [0] * 3, 'aldiusa': [0] * 3, 'carrefour': [0] * 3, 'tesco': [0] * 3, 'metro': [0] * 3}

retailers = ['walmart', 'costco', 'kroger', 'walgreens', 'amazon',
            'Lidl Deutschland', 'aldiusa', 'carrefour', 'tesco', 'metro']

for company in retailers:
    with open('data/' + company + '/' + company + '2.json', 'r') as ff:
        data2 = json.load(ff)

        for i in data2:
            data2[i]['like'] = data2[i]['like']['summary']['total_count']
            data2[i]['love'] = data2[i]['love']['summary']['total_count']
            data2[i]['haha'] = data2[i]['haha']['summary']['total_count']
            data2[i]['sad'] = data2[i]['sad']['summary']['total_count']
            data2[i]['angry'] = data2[i]['angry']['summary']['total_count']
            data2[i]['wow'] = data2[i]['wow']['summary']['total_count']
            data2[i]['created_time'] = parse(data2[i]['created_time']).date()
            try:
                data2[i]['shares'] = data2[i]['shares']['count']
            except:
                pass

    df = pd.DataFrame(data2)
    df_T =  df.T
    df_T = df_T.drop('id', axis = 1)
    # df_T['reactions'] = df_T['like'] + df_T['love'] + df_T['haha'] + df_T['wow'] + df_T['sad'] + df_T['angry']
    # t1 = df_T[df_T['type'] != 'link']
    # t2 = t1[t1['type'] != 'video']
    # t3 = t2[t2['type'] != 'photo']
    # t4 = t3[t3['type'] != 'status']
    # print t4['created_time']
    # print t4['message']
    # print t4['type']
    df_type =  df_T[df_T['type'] == retype]
    print df_type['created_time']
    # print df_type['message']
    # print df_type['status_type']
    df2015 = df_type[df_type['created_time'] < parse('2016/01/01').date()]
    if len(df2015) != 0:
        companys[company][0] = float(sum(df2015['like']))/len(df2015)
    df2016 = df_type[df_type['created_time'] > parse('2015/12/31').date()]
    df2016 = df2016[df2016['created_time'] < parse('2017/01/01').date()]
    if len(df2016) != 0:
        companys[company][1] = float(sum(df2016['like']))/len(df2016)
    df2017 = df_type[df_type['created_time'] > parse('2016/12/31').date()]
    df2017 = df2017[df2017['created_time'] < parse('2018/01/01').date()]
    if len(df2017) != 0:
        companys[company][2] = float(sum(df2017['like']))/len(df2017)
print companys


x = np.array([0, 7, 14])
y = dict()
num = 0
for company in retailers:
    if num == 5:
        x = np.array([0.25, 7.25, 14.25])
    
    plt.bar((x + 0.5 * num), (companys[company][0], companys[company][1], companys[company][2]), width=0.5, label = company)    
    y[num] = (companys[company][0], companys[company][1], companys[company][2])
    num += 1

x = np.array([0, 7, 14])
plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
plt.title('Ten retailers annual average like of ' + retype +' post')
plt.xticks(x + 2, ('2015', '2016', '2017'))
#去掉邊框
ax = plt.gca()
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  

for z in range(10):
    if z == 5:
        x = np.array([0.25, 7.25, 14.25])
    for i, j in zip(x, y[z]):
        plt.text((i + 0.5 * z), j + 0.05, '%.1f' %j, ha='center', va='bottom', fontsize=6)



plt.show()

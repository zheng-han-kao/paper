# -*- coding: utf-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  

token = 'EAAWJXd7dIIMBACz10ycB3RFJBaZBcZA1kAANz6fDqOQa10nXgXhKhvWJzLk9rrlcwZCATOV0YgRhqDOekvBOnnk8ZCnzdOf2A1efUkRM9fw3QHY5erE41hb0F8P5smahyV4mKOVyzXNbCjiKIvXjOUq2ZAWsnutmKbBRJGCeDaAZDZD'

dict_page_id_fancou = {'aldiusa': ['218299471593750'], 'amazon': ['9465008123'], 'carrefour': ['176105152520900'], 'costco': ['15240089946'], 'kroger': ['60686173217'],
                'Lidl Deutschland': ['278565202257'], 'metro': ['119707938207'], 'tesco': ['112463368812803'], 'walgreens': ['117497138610'], 'walmart': ['159616034235']}

retailers = ['walmart', 'costco', 'kroger', 'walgreens', 'amazon',
             'Lidl Deutschland', 'aldiusa', 'carrefour', 'tesco', 'metro']

for retailer in retailers:
    page_id = dict_page_id_fancou[retailer][0]
    fancou = requests.get(
        'https://graph.facebook.com/v2.12/{}?fields=fan_count&access_token={}'.format(page_id, token))
    fancount = fancou.json()['fan_count']
    dict_page_id_fancou[retailer].append(fancount)

print dict_page_id_fancou

ymajorLocator = MultipleLocator(5000000)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式


x = np.array([0])
y = dict()
num = 0
for company in retailers:
    plt.bar((x + 0.3 * num), (dict_page_id_fancou[company][1]), width=0.25)
    y[num] = (dict_page_id_fancou[company][1])
    num += 1


# plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
plt.title('retailers fan count')
xs = [x + i * 0.3 for i, _ in enumerate(retailers)]
plt.xticks(xs, retailers)
#去掉邊框
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

for z in range(10):
    plt.text((x + 0.3 * z), y[z] + 0.05, '%.1f' %
             y[z], ha='center', va='bottom')


plt.show()

# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
post_type = {'video': [0] * 9,
             'photo': [0] * 9, 
             'status': [0] * 9, 
             'link': [0] * 9, 
             'others': [0] * 9}
reactions = ['like', 'love', 'haha', 'sad', 'angry', 'wow']
color = ['////', '...', '***', '---', '+++', 'xxxx']
x = np.arange(5)

retailer = 'Lidl Deutschland'

def count(dd, tt):
    tt[8] += 1
    tt[0] += dd['like']['summary']['total_count']
    tt[1] += dd['love']['summary']['total_count']
    tt[2] += dd['haha']['summary']['total_count']
    tt[3] += dd['sad']['summary']['total_count']
    tt[4] += dd['angry']['summary']['total_count']
    tt[5] += dd['wow']['summary']['total_count']
    return tt

with open('data/' + retailer + '/' + retailer + '2.json', 'r') as ff:
    data2 = json.load(ff)
    with open('data/' + retailer + '/' + retailer + '_comment2.json', 'r') as file:
        data = json.load(file)

        for i in data2:
            post_time = parse(data2[i]['created_time']).date()

            if post_time > parse('2016/02/22').date():
                if data2[i]['type'] == 'link':
                    post_type['link'] = count(data2[i], post_type['link'])
                    post_type['link'][7] += len(data[i])
                elif data2[i]['type'] == 'photo':
                    post_type['photo'] = count(data2[i], post_type['photo'])
                    post_type['photo'][7] += len(data[i])
                elif data2[i]['type'] == 'video':
                    post_type['video'] = count(data2[i], post_type['video'])
                    post_type['video'][7] += len(data[i])
                elif data2[i]['type'] == 'status':
                    post_type['status'] = count(data2[i], post_type['status'])
                    post_type['status'][7] += len(data[i])
                else:
                    post_type['others'] = count(data2[i], post_type['others'])
                    post_type['others'][7] += len(data[i])
                    print data2[i]['created_time']
                    # print data2[i]['message']

for ele in post_type:
    post_type[ele][6] = sum(post_type[ele][:6])
    if post_type[ele][8] != 0:
        for i in range(8):
            post_type[ele][i] = float(post_type[ele][i]) / post_type[ele][8]

print post_type['link']
############畫圖reactions##############
y = dict()

for i in range(6):
    barlist = plt.bar((x + 0.15 * i), (post_type['link'][i], post_type['photo'][i], post_type['video'][i],
                                       post_type['status'][i], post_type['others'][i]), width=0.15, label=reactions[i], color='w', edgecolor='black')
    barlist[0].set_hatch(color[i])
    barlist[1].set_hatch(color[i])
    barlist[2].set_hatch(color[i])
    barlist[3].set_hatch(color[i])
    barlist[4].set_hatch(color[i])
    y[i] = (post_type['link'][i], post_type['photo'][i], post_type['video'][i],
            post_type['status'][i], post_type['others'][i])


plt.xticks(x + 0.15, ('link', 'photo', 'video', 'status', 'others'))
plt.legend(loc='upper left', fontsize='x-small', frameon=False)
plt.title(retailer + ' post type reactions')
#去掉邊框
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


for z in range(6):
    for i, j in zip(x, y[z]):
        plt.text((i + 0.15 * z), j + 0.05, '%.1f' %j, ha='center', va='bottom', fontsize=8)

plt.show()

#############畫圖總情緒數與留言#############
# y = dict()

# for i in range(3):
#     plt.bar((x + 0.25 * i), (post_type['link'][i + 6], post_type['photo'][i + 6], post_type['video'][i + 6],
#                              post_type['status'][i + 6], post_type['offer'][i + 6]), width=0.25)
#     y[i] = (post_type['link'][i + 6], post_type['photo'][i + 6], post_type['video'][i + 6],
#             post_type['status'][i + 6], post_type['offer'][i + 6])

# plt.xticks(x + 0.25, ('link', 'photo', 'video', 'status', 'offer'))

# for z in range(3):
#     for i, j in zip(x, y[z]):
#         plt.text((i + 0.25 * z), j + 0.05, '%.1f' %
#                  j, ha='center', va='bottom')

# plt.show()

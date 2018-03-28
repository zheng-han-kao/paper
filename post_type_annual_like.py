# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
post_type = {'video': [0] * 7,
             'photo': [0] * 7,
             'status': [0] * 7,
             'link': [0] * 7,
             'others': [0] * 7}
postT = ['video', 'link', 'photo', 'status', 'others']
x = np.arange(5)
year = ['2015', '2016', '2017']
retailer = 'walgreens'
color = ['////', '...', '**']

def count(dd, tt, i):
    tt[i + 1] += 1
    tt[i] += dd['like']['summary']['total_count']
    return tt


with open('data/' + retailer + '/' + retailer + '2.json', 'r') as ff:
    data2 = json.load(ff)

    for i in data2:
        post_time = parse(data2[i]['created_time']).date()

        if post_time < parse('2016/01/01').date():
            if data2[i]['type'] == 'link':
                post_type['link'] = count(data2[i], post_type['link'], 0)
            elif data2[i]['type'] == 'photo':
                post_type['photo'] = count(data2[i], post_type['photo'], 0)
            elif data2[i]['type'] == 'video':
                post_type['video'] = count(data2[i], post_type['video'], 0)
            elif data2[i]['type'] == 'status':
                post_type['status'] = count(data2[i], post_type['status'], 0)
            else:
                post_type['others'] = count(data2[i], post_type['others'], 0)
                print data2[i]['created_time']
        elif post_time < parse('2017/01/01').date():
            if data2[i]['type'] == 'link':
                post_type['link'] = count(data2[i], post_type['link'], 2)
            elif data2[i]['type'] == 'photo':
                post_type['photo'] = count(data2[i], post_type['photo'], 2)
            elif data2[i]['type'] == 'video':
                post_type['video'] = count(data2[i], post_type['video'], 2)
            elif data2[i]['type'] == 'status':
                post_type['status'] = count(data2[i], post_type['status'], 2)
            else:
                post_type['others'] = count(data2[i], post_type['others'], 2)
                print data2[i]['created_time']
        else:
            if data2[i]['type'] == 'link':
                post_type['link'] = count(data2[i], post_type['link'], 4)
            elif data2[i]['type'] == 'photo':
                post_type['photo'] = count(data2[i], post_type['photo'], 4)
            elif data2[i]['type'] == 'video':
                post_type['video'] = count(data2[i], post_type['video'], 4)
            elif data2[i]['type'] == 'status':
                post_type['status'] = count(data2[i], post_type['status'], 4)
            else:
                post_type['others'] = count(data2[i], post_type['others'], 4)
                print data2[i]['created_time']

for ele in post_type:
    if post_type[ele][1] != 0:
        post_type[ele][0] = float(post_type[ele][0]) / post_type[ele][1]
    if post_type[ele][3] != 0:
        post_type[ele][2] = float(post_type[ele][2]) / post_type[ele][3]
    if post_type[ele][5] != 0:
        post_type[ele][4] = float(post_type[ele][4]) / post_type[ele][5]

# print post_type['link']
############畫圖reactions##############
y = dict()
num = 0
for i in range(3):
    barlist = plt.bar((x + 0.25 * i), (post_type['link'][i + num], post_type['photo'][i + num], post_type['video'][i + num],
                                       post_type['status'][i + num], post_type['others'][i + num]), width=0.25, label=year[i], color='w', edgecolor='black')
    barlist[0].set_hatch(color[i])
    barlist[1].set_hatch(color[i])
    barlist[2].set_hatch(color[i])
    barlist[3].set_hatch(color[i])
    barlist[4].set_hatch(color[i])


    y[i] = (post_type['link'][i + num], post_type['photo'][i + num], post_type['video'][i + num],
    post_type['status'][i + num], post_type['others'][i + num])
    num += 1


plt.xticks(x + 0.25, ('link', 'photo', 'video', 'status', 'others'))
plt.legend(loc='upper left', fontsize='small', frameon=False)
plt.title(retailer + ' post type annual average likes')
#去掉邊框
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


for z in range(3):
    for i, j in zip(x, y[z]):
        plt.text((i + 0.25 * z), j + 0.05, '%.1f' %
                 j, ha='center', va='bottom')

plt.show()

#############畫圖總情緒數與留言#############
# for posttype in postT:
#     post_type[posttype][6] = post_type[posttype][1] + post_type[posttype][3] + post_type[posttype][5]


# x = np.array([0])
# y = dict()
# num = 0
# for ele in postT:
#     plt.bar((x + 0.3 * num), (post_type[ele][6]), width=0.25)
#     y[num] = (post_type[ele][6])
#     num += 1


# # plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
# plt.title(retailer + ' post type count')
# xs = [x + i * 0.3 for i, _ in enumerate(postT)]
# plt.xticks(xs, postT)
# #去掉邊框
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# for z in range(5):
#     plt.text((x + 0.3 * z), y[z] + 0.05, '%.1f' %
#              y[z], ha='center', va='bottom')


# plt.show()

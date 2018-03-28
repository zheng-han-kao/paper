# -*- coding: utf-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime

token = 'EAAWJXd7dIIMBACz10ycB3RFJBaZBcZA1kAANz6fDqOQa10nXgXhKhvWJzLk9rrlcwZCATOV0YgRhqDOekvBOnnk8ZCnzdOf2A1efUkRM9fw3QHY5erE41hb0F8P5smahyV4mKOVyzXNbCjiKIvXjOUq2ZAWsnutmKbBRJGCeDaAZDZD'
company = 'walmart'
hour_post = [0] * 24
with open('data/' + company + '/' + company + '2.json', 'r') as ff:
    data2 = json.load(ff)
    for i in data2:
        postime = parse(data2[i]['created_time'])
        hour = postime.hour
        hour_post[hour] += 1


x = np.array([0])
y = dict()
num = 0
for i in range(len(hour_post)):
    plt.bar((x + 0.3 * num), (hour_post[i]), width=0.25)
    y[num] = (hour_post[i])
    num += 1


# plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
plt.title(company + ' hour post')
xs = [x + i * 0.3 for i, _ in enumerate(hour_post)]
new_ticks = np.arange(0, 24)
plt.xticks(xs, new_ticks)
#去掉邊框
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for z in range(24):
    plt.text((x + 0.3 * z), y[z] + 0.05, '%d' %
             y[z], ha='center', va='bottom')


plt.show()

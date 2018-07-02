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

company = 'walgreens'
month_post = [0] * 12
print month_post
with open('data/' + company + '/' + company + '2.json', 'r') as ff:
    data2 = json.load(ff)
    for i in data2:
        postime = parse(data2[i]['created_time'])
        if postime.date() > parse('2015/12/31').date():
            if postime.date() < parse('2017/01/01').date():
                month = postime.month
                month_post[month-1] += 1

print month_post

##### draw a picture #####
x = np.array([0])
y = dict()
num = 0
for i in range(len(month_post)):
    plt.bar((x + 0.3 * num), (month_post[i] / 3.0), width=0.25)
    y[num] = (month_post[i] / 3.0)
    num += 1


# plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
plt.title(company + ' per month post')
xs = [x + i * 0.3 for i, _ in enumerate(month_post)]
new_ticks = np.arange(1, 13)
plt.xticks(xs, new_ticks)

### remove the frame ###
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for z in range(12):
    plt.text((x + 0.3 * z), y[z] + 0.05, '%.1f' %
             y[z], ha='center', va='bottom')


plt.show()

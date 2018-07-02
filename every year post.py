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

company = 'walmart'
year_post = [0] * 3

with open('data/' + company + '/' + company + '2.json', 'r') as ff:
    data2 = json.load(ff)
    for i in data2:
        postime = parse(data2[i]['created_time'])
        year = postime.year
        year_post[year - 2015] += 1


##### draw a picture #####
x = np.array([0])
y = dict()
num = 0
for i in range(len(year_post)):
    plt.bar((x + 0.3 * num), (year_post[i]), width=0.25)
    y[num] = (year_post[i])
    num += 1

# plt.legend(loc='upper left', fontsize='xx-small', frameon=False)
plt.title(company + ' per year post')
xs = [x + i * 0.3 for i, _ in enumerate(year_post)]
new_ticks = np.arange(2015, 2018)
plt.xticks(xs, new_ticks)

### remove the frame ###
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for z in range(3):
    plt.text((x + 0.3 * z), y[z] + 0.05, '%d' %
             y[z], ha='center', va='bottom')


plt.show()

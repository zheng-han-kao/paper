# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json

token = ''
video_count = 0
photo_count = 0
status_count = 0
link_count = 0
offer_count = 0

video_like = 0
photo_like = 0
status_like = 0
link_like = 0
offer_like = 0

video_comment = 0
photo_comment = 0
status_comment = 0
link_comment = 0
offer_comment = 0
x = np.arange(5)

retailer = 'costco'


with open(retailer + '/' + retailer + '.json', 'r') as ff:
    data2 = json.load(ff)
    with open(retailer + '/' + retailer + '_comment.json', 'r') as file:
        data = json.load(file)
        for i in data2:
            post_time = parse(data2[i]['created_time']).date()
            if post_time > parse('2016/12/31').date() and post_time < parse('2018/01/01').date():
                if data2[i]['type'] == 'link':
                    link_count += 1
                    link_like += data2[i]['likes']['summary']['total_count']
                    link_comment += len(data[i])
                elif data2[i]['type'] == 'photo':
                    photo_count += 1
                    photo_like += data2[i]['likes']['summary']['total_count']
                    photo_comment += len(data[i])
                elif data2[i]['type'] == 'video':
                    video_count += 1
                    video_like += data2[i]['likes']['summary']['total_count']
                    video_comment += len(data[i])
                elif data2[i]['type'] == 'status':
                    status_count += 1
                    status_like += data2[i]['likes']['summary']['total_count']
                    status_comment += len(data[i])
                else:
                    offer_count += 1
                    offer_like += data2[i]['likes']['summary']['total_count']
                    offer_comment += len(data[i])
                    print data2[i]['created_time']
                    print data2[i]['message']



if link_count != 0:
    link_like = link_like / link_count
    link_comment = link_comment / link_count

if photo_count != 0:
    photo_like = photo_like / photo_count
    photo_comment = photo_comment / photo_count

if video_count != 0:
    video_like = video_like / video_count
    video_comment = video_comment / video_count

if status_count != 0:
    status_like = status_like / status_count
    status_comment = status_comment / status_count

if offer_count != 0:
    offer_like = offer_like / offer_count
    offer_comment = offer_comment / offer_count

print 'link count : %d' % link_count
print 'photo count : %d' % photo_count
print 'video_count : %d' % video_count
print 'status_count : %d' % status_count
print 'offer_count : %d' % offer_count

print 'link like : %d' % link_like
print 'photo like : %d' % photo_like
print 'video like : %d' % video_like
print 'status like : %d' % status_like
print 'offer like : %d' % offer_like

print 'link comment : %d' % link_comment
print 'photo comment : %d' % photo_comment
print 'video comment : %d' % video_comment
print 'status comment : %d' % status_comment
print 'offer comment : %d' % offer_comment

plt.bar(x, (link_count, photo_count, video_count,
            status_count, offer_count), width=0.25)

plt.bar(x + 0.25, (link_like, photo_like, video_like,
                    status_like, offer_like), width=0.25)
plt.bar(x + 0.5, (link_comment, photo_comment, video_comment,
                    status_comment, offer_comment), width=0.25)

plt.xticks(x + 0.25, ('link', 'photo', 'video', 'status', 'offer'))

y1 = (link_count, photo_count, video_count, status_count, offer_count)
y2 = (link_like, photo_like, video_like, status_like, offer_like)
y3 = (link_comment, photo_comment, video_comment,
        status_comment, offer_comment)

for i, j in zip(x, y1):
    plt.text(i, j + 0.05, '%.2f' % j, ha='center', va='bottom')

for i, j in zip(x, y2):
    plt.text(i + 0.25, j + 0.05, '%.2f' % j, ha='center', va='bottom')

for i, j in zip(x, y3):
    plt.text(i + 0.5, j + 0.05, '%.2f' % j, ha='center', va='bottom')

plt.show()



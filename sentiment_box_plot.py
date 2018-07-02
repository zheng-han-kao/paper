# -*- coding: utf-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

retailer = 'amazon'
sen_type = ['pos%', 'neu%', 'neg%']

# def drawboxplot(df2015, df2016, df2017):
#     post_list = []
#     for type in sen_type:
#         post2015 = df2015[type].tolist()
#         post_list.append(post2015)
#     for type in sen_type:
#         post2016 = df2016[type].tolist()
#         post_list.append(post2016)
#     for type in sen_type:
#         post2017 = df2017[type].tolist()
#         post_list.append(post2017)
#     print post_list

#     plt.boxplot(post_list, vert=True)   # vertical box aligmnent

#     plt.xticks([y + 1 for y in range(len(post_list))],
#                ['2015 pos%', '2015 neu%', '2015 neg%', '2016 pos%', '2016 neu%', '2016 neg%', '2017 pos%', '2017 neu%', '2017 neg%'])
#     plt.title(retailer + ' post ' + ' sentiment Box plot')

#     #去掉邊框
#     ax = plt.gca()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)

#     plt.show()


def drawboxplot(df2015, df2016, df2017):
    post_list = []
    for type in sen_type:
        post2015 = df2015[type].tolist()
        post_list.append(post2015)
        post2016 = df2016[type].tolist()
        post_list.append(post2016)
        post2017 = df2017[type].tolist()
        post_list.append(post2017)
   
    # vertical box aligmnent
    plt.boxplot(post_list, positions = [1, 2, 3, 4.5, 5.5, 6.5, 8, 9, 10], vert=True)

    plt.xticks([1, 2, 3, 4.5, 5.5, 6.5, 8, 9, 10],
               ['2015 pos%', '2016 pos%', '2017 pos%', '2015 neu%', '2016 neu%', '2017 neu%', '2015 neg%', '2016 neg%', '2017 neg%'])
    # plt.title(retailer + ' post ' + ' sentiment Box plot')

    ### remove the frame ###
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.show()


df = pd.read_excel("post sentiment/" + retailer + "_post_sentiment.xls")
for i in range(len(df)):
    df.ix[i, "created_time"] = parse(df.ix[i, "created_time"]).date()
    # print df.ix[i,"created_time"]

df2015 = df[df['created_time'] < parse('2016/01/01').date()]
df2016 = df[(df['created_time'] > parse('2015/12/31').date()) & (df['created_time'] < parse('2017/01/01').date())]
df2017 = df[df['created_time'] > parse('2016/12/31').date()]


drawboxplot(df2015, df2016, df2017)

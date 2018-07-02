# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import xlrd
import xlwt

sid = SentimentIntensityAnalyzer()
sentiment_avg = [0] * 7
retailer = 'walgreens'

######### write to excel #######
f = xlwt.Workbook()
sheet = f.add_sheet('sheet1', cell_overwrite_ok=True)
row0 = ["created_time", "message", "positive", "negative",
        "neutral", "pos%", "neg%", "neu%", "comment num", "like"]
rownum = 0
for i in range(len(row0)):
    sheet.write(0,i,row0[i])
rownum += 1

with open('data/' + retailer + '/' + retailer + '2.json', 'r') as ff:
    data2 = json.load(ff)
    with open('data/' + retailer + '/' + retailer + '_comment2.json', 'r') as file:
        data = json.load(file)
        for ele in data2:
            post_id = ele
            like = data2[ele]['like']['summary']['total_count']
            created_time = data2[ele]["created_time"]
            if 'message' in data2[ele]:
               post_message = data2[ele]["message"]
            else:
                post_message = 'no message'

            # if parse(created_time).date() == parse('2015/11/25').date():
            #     print post_id
            #     print created_time
            #     print post_message
            #     print data2[ele]['type']
            #     print data2[ele]['link']
            
            sheet.write(rownum, 0, created_time)
            sheet.write(rownum, 1, post_message)
        
            ##### comments sentiment analysis #####
            sentiment_avg = [0] * 7

            for comment in data[post_id]:
                print comment['message']
                sentence = comment['message']

                ss = sid.polarity_scores(sentence)
                for k in sorted(ss):
                    print '{0}: {1}, '.format(k, ss[k])
                    print
                    pass
                if ss['compound'] > 0:
                    sentiment_avg[0] += 1
                elif ss['compound'] < 0:
                    sentiment_avg[1] += 1
                else:
                    sentiment_avg[2] += 1
            
            sentiment_avg[6] = sum(sentiment_avg[:3])
            if sentiment_avg[6] != 0:
                sentiment_avg[3] = float(sentiment_avg[0]) / sentiment_avg[6]
                sentiment_avg[4] = float(sentiment_avg[1]) / sentiment_avg[6]
                sentiment_avg[5] = float(sentiment_avg[2]) / sentiment_avg[6]
            for j in range(len(sentiment_avg)):
                sheet.write(rownum, j+2, sentiment_avg[j])
            
            sheet.write(rownum, len(sentiment_avg) + 2, like)
            rownum += 1

# f.save("post sentiment/" + retailer + "_post_sentiment_plus_like.xls")

# -*- coding: utf-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json

token = 'EAAWJXd7dIIMBACz10ycB3RFJBaZBcZA1kAANz6fDqOQa10nXgXhKhvWJzLk9rrlcwZCATOV0YgRhqDOekvBOnnk8ZCnzdOf2A1efUkRM9fw3QHY5erE41hb0F8P5smahyV4mKOVyzXNbCjiKIvXjOUq2ZAWsnutmKbBRJGCeDaAZDZD'
retailer = 'walmart'

comment_break = 0
post_break = 0

comment_data = []
id_comment = {}
id_post = {}

dict_page_id = {'aldiusa': '218299471593750', 'amazon': '9465008123', 'carrefour': '176105152520900', 'costco': '15240089946', 'kroger': '60686173217', 
                'Lidl Deutschland': '278565202257', 'metro': '119707938207', 'tesco': '112463368812803', 'walgreens': '117497138610', 'walmart': '159616034235'}


page_id = dict_page_id[retailer]



####### crawling posts ########
posts = requests.get(
    'https://graph.facebook.com/v2.12/{}/posts?fields=link,created_time,message,status_type,type,story,shares,reactions.type(LIKE).limit(0).summary(1).as(like),reactions.type(LOVE).limit(0).summary(1).as(love),reactions.type(HAHA).limit(0).summary(1).as(haha),reactions.type(WOW).limit(0).summary(1).as(wow),reactions.type(SAD).limit(0).summary(1).as(sad),reactions.type(ANGRY).limit(0).summary(1).as(angry)&access_token={}'.format(page_id, token))

while 'paging' in posts.json():
    for post in posts.json()['data']:
        post_time = parse(post['created_time']).date()

        if post_time > parse('2014/12/31').date() and post_time < parse('2018/01/01').date():
            post_id = post['id']
            print post_time

            id_post[post_id] = post

            ########## get comments #########
            while True:
                try:
                    comments = requests.get(
                        'https://graph.facebook.com/v2.12/{}/comments?fields=created_time,like_count,message&limit=100&access_token={}'.format(post['id'], token))
                    break
                except:
                    time.sleep(5)
            
            while 'paging' in comments.json():
                comment_data.extend(comments.json()['data'])


                while True:
                    try:
                        if 'next' in comments.json()['paging']:
                            comments = requests.get(comments.json()['paging']['next'])
                        else:
                            comment_break = 1
                            break

                        break
                    except:
                        time.sleep(5)

                if comment_break == 1:
                    comment_break = 0
                    break

            id_comment[post_id] = comment_data
            comment_data = []

        # else:
        #     break

    while True:
        try:
            if 'next' in posts.json()['paging']:
                posts = requests.get(posts.json()['paging']['next'])
            else:
                post_break = 1
                break

            break
        except:
            time.sleep(5)

    if post_break == 1:
        post_break = 0
        break

file = open('data/' + retailer + '/' + retailer + '2.json', 'w')
json.dump(id_post, file)
file.close()

f = open('data/' + retailer + '/' + retailer + '_comment2.json', 'w')
json.dump(id_comment, f)
f.close()

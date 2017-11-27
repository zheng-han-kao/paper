# -*- coding: utf-8 -*-
import requests
import pandas as pd
from dateutil.parser import parse
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import json

token = ''
retailer = 'costco'

comment_break = 0
post_break = 0

comment_data = []
id_comment = {}
id_post = {}


###### request page  #########
pages = requests.get('https://graph.facebook.com/v2.11/search?q={}&type=page&access_token={}'.format(retailer, token))
page_id = pages.json()['data'][0]['id']

####### crawling posts ########
posts = requests.get(
    'https://graph.facebook.com/v2.11/{}/posts?fields=link,created_time,message,status_type,type,likes.limit(0).summary(True),story&access_token={}'.format(page_id, token))

while 'paging' in posts.json():
    for post in posts.json()['data']:
        post_time = parse(post['created_time']).date()

        if post_time > parse('2014/12/31').date():
            post_id = post['id']
            print post_time

            id_post[post_id] = post

            ########## get comments #########
            while True:
                try:
                    comments = requests.get(
                        'https://graph.facebook.com/v2.11/{}/comments?fields=created_time,like_count,message&limit=100&access_token={}'.format(post['id'], token))
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

        else:
            break

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

file = open(retailer + '/' + retailer + '.json', 'w')
json.dump(id_post, file)
file.close()

f = open(retailer + '/' + retailer + '_comment.json', 'w')
json.dump(id_comment, f)
f.close()

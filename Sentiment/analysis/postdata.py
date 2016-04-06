#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from .models import pages

TOKEN = \
    'EAACEdEose0cBAHdZA7lVt4KhbchZBZA80F4cRp1xZCjTTI3WF3CbWzdLWc0PvYQDD5QAqdsBLwCsA1f2gZCICr9QmP6eZASBiMBpuin7J5pzRkYeEe81zqXwxKsKIndvapjube7ziseX25pJglXhpmiNivwapS7ZBqCX5jNW8cp7wZDZD'
f = open('result.js', 'w')

def print_page(pages):
    for page in pages['data']:
        print(page['name'])
        print(page['category'])

def get_posts(query, collegeData):

    url = 'https://graph.facebook.com/search?q=' + query \
        + '&type=page&limit=10'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # print(result["data"])
    # ids = []
    # likes = []
    print_page(result)

    for res in result['data']:
        if res['category']:
            if  res['category'] == 'Education' or res['category'] == 'Community' or res['category'] == 'University':
                engagementUrl = 'https://graph.facebook.com/' + res['id'] \
                + '/?fields=name,posts.limit(4){name,likes},engagement,category'
            
                q = requests.get(engagementUrl, params=parameters)
                result = json.loads(q.text)
                p = pages(page_id = result['id'] , page_name = result['name'] , page_posts_json = result['posts'] , page_category = result['category'] , page_likes = result['engagement']['count'])
                p.save()
                # with open('data.txt', 'a') as outfile:
                #     json.dump(result, outfile)
                # collegeData += str(result)
                print(result)

    # f.write(collegeData)
            # return {"id" : ids , 'likes' : likes}

get_posts('stanford', '')

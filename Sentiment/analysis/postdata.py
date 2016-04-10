#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from .models import pages

TOKEN = \
    'EAACEdEose0cBAJVDuDChDSZCjiHQvZAQQGhqTvCBM0HZAzttZBp6vWfcd8uF7QCA3A8lWfPi8I0yafXZAiRHqZBWPVFCp5fxxCM0X2HXrdZBBTcmmvKL1GT1w0KBZCltnhxQQytfogbkdCZBiUHZAmWgZCUCWcd6lDZCovLdHOSYYKsKjgZDZD'

valid_category = ['Education' , 'Community' , 'Organisation' , 'University' , 'Institute']

def print_page(pages):
    for page in pages['data']:
        print(page['name'])
        print(page['category'])

def get_posts(query):

    url = 'https://graph.facebook.com/search?q=' + query.replace(" " , "+") \
        + '&type=page&limit=5'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    return_pages = {'data':[]}
    print_page(result)
    pages.objects.all().delete()
    for res in result['data']:
        # if res['category'] and res['category'] in valid_category:
        engagementUrl = 'https://graph.facebook.com/' + res['id'] \
        + '/?fields=id,name,posts.limit(10){name,message},engagement,category'
        q = requests.get(engagementUrl, params=parameters)
        page_result = json.loads(q.text)
        return_pages['data'].append(page_result)
        try:
            p = pages(page_id = page_result['id'] , page_name = page_result['name'] , page_posts_json = json.dumps(page_result['posts']) , page_category = page_result['category'] , page_likes = page_result['engagement']['count'] , page_json = json.dumps(page_result))
        except Exception:
            pass
        p.save()
        # with open('data.txt', 'a') as outfile:
        #     json.dump(result, outfile)
        # collegeData += str(result)
        # print(page_result)
        # print('\n')
    return return_pages

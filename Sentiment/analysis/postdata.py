#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from .models import pages

TOKEN = \
    'EAACEdEose0cBAMtZB9JZCXfbMOb3cpp0D52nc4gSEG300heIMwKUkIZANiggPqGWazOp0LdeQMJKZBSPNwzfIStUzS0PNZCZAZCXYpDZCBmRHXsxPApRRAl36zOZAYLZCPHpBnYD4efR6WX0hc2AMxOaNxFgGmW0GqXJ2dv77bkCh9qQZDZD'

valid_category = ['Education' , 'Community' , 'Organisation' , 'University' , 'Institute']

def print_page(pages):
    for page in pages['data']:
        print(page['name'])
        print(page['category'])

def get_posts(query):
    if pages.objects.filter(institute_name__iexact = query).count() >= 1:
        print("college already exists")
        return
    url = 'https://graph.facebook.com/search?q=' + query.replace(" " , "+") \
        + '&type=page&limit=5'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # return_pages = {'data':[]}
    print_page(result)
    # pages.objects.all().delete()
    for res in result['data']:
        # if res['category'] and res['category'] in valid_category:
        engagementUrl = 'https://graph.facebook.com/' + res['id'] \
        + '/?fields=id,name,posts.limit(10){name,message},engagement,category'
        q = requests.get(engagementUrl, params=parameters)
        page_result = json.loads(q.text)
        # return_pages['data'].append(page_result)
        try:
            p = pages(institute_name = query , page_id = page_result['id'] , page_name = page_result['name'] , page_posts_json = json.dumps(page_result['posts']) , page_category = page_result['category'] , page_likes = page_result['engagement']['count'] , page_json = json.dumps(page_result))
        except Exception:
            pass
        p.save()
        # with open('data.txt', 'a') as outfile:
        #     json.dump(result, outfile)
        # collegeData += str(result)
        # print(page_result)
        # print('\n')
    # return return_pages

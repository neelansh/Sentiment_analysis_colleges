#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from .models import pages

TOKEN = \
    'EAACEdEose0cBANv1dzIHZBvyd63jnZCNaG7DZBUnbl7i8BOt901tRScV4v0ZAu1KoPBDACwSOTcsVo1tZBN8QniFlSjGwqZBpWB9ZCxZBGulvBJY2s48AHnDLHuwfNIRY84CZCcC8yftTc5zWgK1FF9vPpRzx1w4Gf9f5XJiXv3kwgQZDZD'

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
        + '&type=page&limit=20'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # return_pages = {'data':[]}
    print_page(result)
    # pages.objects.all().delete()
    i=0;
    for res in result['data']:
        # if res['category'] and res['category'] in valid_category:
        engagementUrl = 'https://graph.facebook.com/' + res['id'] \
        + '/?fields=id,name,posts{name,message},engagement,category'
        q = requests.get(engagementUrl, params=parameters)
        page_result = json.loads(q.text)
        # return_pages['data'].append(page_result)
        try:
            p = pages(institute_name = query , page_id = page_result['id'] , page_name = page_result['name'] , page_posts_json = json.dumps(page_result['posts']) , page_category = page_result['category'] , page_likes = page_result['engagement']['count'] , page_json = json.dumps(page_result))
            p.save()
        except Exception:
            print(Exception)
        # with open('data.txt', 'a') as outfile:
        #     json.dump(result, outfile)
        # collegeData += str(result)
        # print(page_result)
        # print('\n')
    # return return_pages

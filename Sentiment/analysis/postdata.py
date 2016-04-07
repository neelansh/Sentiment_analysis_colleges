#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from .models import pages

TOKEN = \
    'EAACEdEose0cBACCZBy7Tb7hWQzfbARaOxyFN0S1KeSWIhARSjVZCroKpVEb8rpOUckCZAG50272PIi7dv8gnXX21ZAoHznLxKki4nyGv5cZBi18LzyNI9lbmknfZCWuWcYVMZA3lEnOApBnELeFBMIrZCuUA5HnqDoutAZBefrTFTZCQZDZD'

valid_category = ['Education' , 'Community' , 'Organisation' , 'University' , 'Institute']

def print_page(pages):
    for page in pages['data']:
        print(page['name'])
        print(page['category'])

def get_posts_old(query, collegeData):

    url = 'https://graph.facebook.com/search?q=' + query \
        + '&type=page&limit=10'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # print(result["data"])
    # ids = []
    # likes = []
    print_page(result)
    pages.objects.all().delete()
    for res in result['data']:
        if res['category'] and res['category'] in valid_category:
                engagementUrl = 'https://graph.facebook.com/' + res['id'] \
                + '/?fields=id,name,posts.limit(4){name,message},engagement,category'
                q = requests.get(engagementUrl, params=parameters)
                page_result = json.loads(q.text)
                p = pages(page_id = page_result['id'] , page_name = page_result['name'] , page_posts_json = page_result['posts'] , page_category = page_result['category'] , page_likes = page_result['engagement']['count'])
                p.save()
                # with open('data.txt', 'a') as outfile:
                #     json.dump(result, outfile)
                # collegeData += str(result)
                print(result)
                print('\n')


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
    pages.objects.all().delete()
    for res in result['data']:
        engagementUrl = 'https://graph.facebook.com/' + res['id'] \
        + '/?fields=id,name,posts.limit(4){name,message},engagement,category'
        q = requests.get(engagementUrl, params=parameters)
        page_result = json.loads(q.text)
        p = pages(page_id = page_result['id'] , page_name = page_result['name'] , page_posts_json = page_result['posts'] , page_category = page_result['category'] , page_likes = page_result['engagement']['count'])
        p.save()
        # with open('data.txt', 'a') as outfile:
        #     json.dump(result, outfile)
        # collegeData += str(result)
        print(result)
        print('\n')


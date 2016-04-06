#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

TOKEN = \
    'EAACEdEose0cBAHJ2uEee0KABv6vW7QgoX0g2wlDs5bf9pnrPS7JApYgJfm8cbAbdiBAfdQcATHHp2L4Wrttm6kjIvJUzhpNUA6Yi6EukZCtPInVkdyW8GvFtbvFM3U0BtZAP8OHMsQZAyzysFYyJXTYBtxdAFNhyHZB7flfGGgZDZD'
f = open('result.js', 'w')



def get_posts(query, collegeData):

    url = 'https://graph.facebook.com/search?q=' + query \
        + '&type=page&limit=5'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # print(result["data"])
    # ids = []
    # likes = []
    print str(result)

    for res in result['data']:
        if res['category']:
            if  res['category'] == 'Education' :
            # res['id']
                #print res['category_list'][0]['name']
                engagementUrl = 'https://graph.facebook.com/' + res['id'] \
                + '/?fields=name,posts.limit(4){name,likes},engagement,category'
            #print engagementUrl
                q = requests.get(engagementUrl, params=parameters)


                with open('data.txt', 'a') as outfile:
                    json.dump(json.loads(q.text), outfile)
                collegeData += str(json.loads(q.text))
                break
                # print str(engagementData)
                # print("Likes  = " + str(engagementData["engagement"]
                # likes.append("Likes  = " + str(engagementData["engagement"]["count"]))


    f.write(collegeData)
            # return {"id" : ids , 'likes' : likes}

get_posts('mit', ' ')

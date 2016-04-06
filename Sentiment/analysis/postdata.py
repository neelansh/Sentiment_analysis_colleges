#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

TOKEN = \
    'EAACEdEose0cBAEWArZCAn2ziUlAQsrWGiVahAEd4CVCoFhTbSRnVrk0r1ZCqaN4g0r09XyVauaKtpxImrJsfUbYDp5P8b56nQXHZAWun38ZB3nJhn9jGMqQJULZBCDyPj4yR7IyARmWsfkQYewX1JJtsbHUWOLdrsfnx1BmQZCnAZDZD'
f = open('result.js', 'w')

resultArr=[];

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
        if res['category'] == 'Education':
            # res['id']
            engagementUrl = 'https://graph.facebook.com/' + res['id'] \
            + '/?fields=name,posts.limit(4){name,likes.limit(50)},engagement'
            #print engagementUrl
            q = requests.get(engagementUrl, params=parameters)


            collegeData += str(json.loads(q.text))

                # print str(engagementData)
                # print("Likes  = " + str(engagementData["engagement"]
                # likes.append("Likes  = " + str(engagementData["engagement"]["count"]))
            f.write(collegeData)



            # return {"id" : ids , 'likes' : likes}

get_posts('usict', ' ')

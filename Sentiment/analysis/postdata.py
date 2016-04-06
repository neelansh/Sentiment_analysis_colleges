#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

TOKEN = \
    'EAACEdEose0cBAMZBE9YmhBSqljCVfp9OW38CLIw1DgRNg8Oo4CWEI2N8AYNPwP0sWHWDpBQx2I0p1DlEVdnylpjIIv9CLDI0X9zn2JAqHJFCK1OZCESGbbtlfZC09kUHvpRzjnHUg1XxYbPpswS5Qys5h8cCDamWjitKuERJQZDZD'


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

                with open('data.json', 'a') as outfile:
                    json.dump(json.loads(q.text), outfile)

                #collegeData += json.loads(q.text)
                break
                # print str(engagementData)
                # print("Likes  = " + str(engagementData["engagement"]
                # likes.append("Likes  = " + str(engagementData["engagement"]["count"]))


    #f.write(collegeData)
            # return {"id" : ids , 'likes' : likes}

get_posts('mit', {})

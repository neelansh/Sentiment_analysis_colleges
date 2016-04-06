#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

TOKEN = \
    'EAACEdEose0cBAJufUdacvGK5oK7h1vXtWbv3XuB33N5Ve3uUlznoMwnGsSadBvBheKujNCPOaapcM4jgm5ZCkvYrv186UTEjsCaqbzb16FTkocIRa3MrALF8bN6ZCFLT1aBX2osw88KMXd45TdFf8FmyxPfAfYIB8zgYurTM2zZBW7DtCPL7i8EKjroRLToWbIcydaeZCgZDZD'
f = open('result.js', 'w')


def get_posts(query, engagementData):

    url = 'https://graph.facebook.com/search?q=' + query \
        + '&type=page&limit=5'
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params=parameters)
    result = json.loads(r.text)

    # print(result["data"])
    # ids = []
    # likes = []

    for res in result['data']:
        print res['id']
        engagementUrl = 'https://graph.facebook.com/' + res['id'] \
            + '/?fields=name,posts.limit(4){name,likes.limit(50)},engagement'
        print engagementUrl
        q = requests.get(engagementUrl, params=parameters)
        print engagementData
        engagementData += str(json.loads(q.text))

                # print str(engagementData)
        # print("Likes  = " + str(engagementData["engagement"]
        # likes.append("Likes  = " + str(engagementData["engagement"]["count"]))

        print engagementData
        f.write(str(engagementData))


            # return {"id" : ids , 'likes' : likes}

get_posts('usict', ' ')

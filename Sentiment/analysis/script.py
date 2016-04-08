# #!/usr/bin/python
# # -*- coding: utf-8 -*-

# import requests
# import json

# TOKEN = \
#     'EAACEdEose0cBAHdZA7lVt4KhbchZBZA80F4cRp1xZCjTTI3WF3CbWzdLWc0PvYQDD5QAqdsBLwCsA1f2gZCICr9QmP6eZASBiMBpuin7J5pzRkYeEe81zqXwxKsKIndvapjube7ziseX25pJglXhpmiNivwapS7ZBqCX5jNW8cp7wZDZD'

# valid_category = ['Education' , 'Community' , 'Organisation' , 'University' , 'Institute']

# def print_page(pages):
#     for page in pages['data']:
#         print(page['name'])
#         print(page['category'])

# def get_posts(query, collegeData):
#     url = 'https://graph.facebook.com/search?q=' + query \
#         + '&type=page&limit=5'
#     parameters = {'access_token': TOKEN}
#     r = requests.get(url, params=parameters)
#     result = json.loads(r.text)

#     # print(result["data"])
#     # ids = []
#     # likes = []
#     print_page(result)
#     for res in result['data']:
#         if res['category']:
#             if res['category'] in valid_category:
#                 engagementUrl = 'https://graph.facebook.com/' + res['id'] \
#                 + '/?fields=id,name,posts.limit(4){name,message},engagement,category'
            
#                 q = requests.get(engagementUrl, params=parameters)
#                 result = json.loads(q.text)
#                 # with open('data.txt', 'a') as outfile:
#                 #     json.dump(result, outfile)
#                 # collegeData += str(result)
#                 print(result['posts'])
#                 print('\n')

#     # f.write(collegeData)
# get_posts('stanford' , '')




from twython import Twython
import json
APP_KEY = 'mOZbx2cTUbgaKHBOs8JzrMISZ'
APP_SECRET = '3IZBWFxExrNYINPbXIgWfrpRYwe73cknGBRu1KhUTm2PzjO4F9'

ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKTUuQAAAAAAtVMF7IGhX%2B6Mg1aqiqTByucW%2FsE%3Dz0co0E7EbvNwkjstY27fgtR9mVO5ilEgFe1BPoiBXS31FI2Wfq'

collegename = 'mit'
queryPostiive = '#' + collegename + ':)'


twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
data = twitter.search(q=queryPostiive, count='2')
# with open('dataPositive.json', 'w') as outfile:
#     json.dump(data, outfile)
print(data)
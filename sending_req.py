import requests
import json


TOKEN = 'EAACEdEose0cBAAF1FtU14Pe33pZBNxF1I4HY5vRcR8UbPhOUFbwW3ZC0j3wkt0STxgKsNjLWUGsTsY6vQdZAlvCQHUOSJ31SmRMWpQWm0WXqXUxPvz1AZAm7IIKUg0gTbnoZA26HN0lwZB3LNdobZCgzvR7TYWBpKiFSK3rgp4uvgZDZD'

def get_posts(query):
	url = "https://graph.facebook.com/search?q="+query+"&type=page&posts"
	parameters = {'access_token': TOKEN}
	r = requests.get(url, params = parameters)
	result = json.loads(r.text)
	# print(result["data"])
	for res in result["data"]:
		print(res["name"])


get_posts("usit")
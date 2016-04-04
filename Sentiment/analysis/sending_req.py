import requests
import json


TOKEN = 'EAACEdEose0cBAPzjRiAaWQicONvcg7dKzNIPs7zku0sQYZCTno36IKU1yZA3i7c0h68VU5VZC875HklH76uxqYnpPnC2tVlJAxSrYaAeZAIxbf7ejd1RRu4CqXI6waXSE1YZCdMT3vt84qrZCZB3vZBHzOIT5oXTbqZAt3zUZCP2ZASqQZDZD'

def get_posts(query):
	url = "https://graph.facebook.com/search?q="+query+"&type=page&limit=5"
	parameters = {'access_token': TOKEN}
	r = requests.get(url, params = parameters)
	result = json.loads(r.text)
	# print(result["data"])
	ids = []
	likes = []

	for res in result["data"]:
		print(res["id"])
		ids.append(res["id"])
		engagementUrl = 'https://graph.facebook.com/' + res["id"] + '/?fields=engagement';
		q = requests.get(engagementUrl, params = parameters)
		engagementData = json.loads(q.text)
		# print("Likes  = " + str(engagementData["engagement"]["count"]))
		likes.append("Likes  = " + str(engagementData["engagement"]["count"]))
	return {"id" : ids , 'likes' : likes}


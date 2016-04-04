import requests
import json


TOKEN = 'EAACEdEose0cBAOf61TUL0Rusp731Qv9fXrcs5ul9DvZCntYA9FjOzgATtfN1tdAr8HbCnZC7b5tkjv4umfjxCWt2zdhwnLTyLNs8KHePy1lSfWgZCHJA8I2Aa2pCBSjPVeHIY43JfCYHq6cdgNG1yfrv0MFxZBO5cZCvPSM4b6AZDZD'

def get_posts(query):
	url = "https://graph.facebook.com/search?q="+query+"&type=page&limit=5"
	parameters = {'access_token': TOKEN}
	r = requests.get(url, params = parameters)
	result = json.loads(r.text)
	# print(result["data"])

	for res in result["data"]:
		print res["id"].encode('utf-8')
		engagementUrl = 'https://graph.facebook.com/' + res["id"] + '/?fields=engagement';
		q = requests.get(engagementUrl, params = parameters)
		engagementData = json.loads(q.text)
		print "Likes  = " + engagementData["engagement"]["count"]


get_posts("igdtu")

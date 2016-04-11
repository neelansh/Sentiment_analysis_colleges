import requests
import json

def get_flickr(query):
	TEXT=query.replace(" ", "+")
	FORMAT='json'
	METHOD='flickr.photos.search'

	KEY='7dc81dedaee60d8498c3480f325bc1d6'

	url='https://api.flickr.com/services/rest/?'+'method='+METHOD
	parameters={'api_key':KEY,'text':TEXT,'format':FORMAT}
	r = requests.get(url,params=parameters)
	result = r.text
	result = result.replace("jsonFlickrApi(" , "")[:-1]
	result = json.loads(result)
	return {"no_pages" : result["photos"]["pages"],
			"no_photos": result["photos"]["total"]}

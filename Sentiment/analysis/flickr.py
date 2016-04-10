import requests
import json

def get_flickr(query):
	TAGS=query
	FORMAT='json'
	METHOD='flickr.photos.search'

	KEY='637f99c7944fc94332b8c1159443edb0'

	url='https://api.flickr.com/services/rest/?'+'method='+METHOD
	parameters={'api_key':KEY,'tags':TAGS,'format':FORMAT}
	r = requests.get(url,params=parameters)
	result = r.text
	result = result.replace("jsonFlickrApi(" , "")[:-1]
	result = json.loads(result)
	return {"no_pages" : result["photos"]["pages"],
			"no_photos": result["photos"]["total"]}

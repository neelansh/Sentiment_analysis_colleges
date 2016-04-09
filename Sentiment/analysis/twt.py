from twython import Twython
import json
from .models import twitter as twt

APP_KEY = 'mOZbx2cTUbgaKHBOs8JzrMISZ'
APP_SECRET = '3IZBWFxExrNYINPbXIgWfrpRYwe73cknGBRu1KhUTm2PzjO4F9'

ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKTUuQAAAAAAtVMF7IGhX%2B6Mg1aqiqTByucW%2FsE%3Dz0co0E7EbvNwkjstY27fgtR9mVO5ilEgFe1BPoiBXS31FI2Wfq'

# collegename = 'mit'

# with open('dataPositive.json', 'w') as outfile:
#     json.dump(data, outfile)


def get_tweets(query):
	queryPostiive = '#' + query + ':)'
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	data = twitter.search(q=queryPostiive, count='3')
	
	twt.objects.all().delete()
	t = twt(twitter_json = json.dumps(data))
	t.save()

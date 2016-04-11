from twython import Twython
import json
from .models import twitter as twt
from .models import tweets

APP_KEY = 'mOZbx2cTUbgaKHBOs8JzrMISZ'
APP_SECRET = '3IZBWFxExrNYINPbXIgWfrpRYwe73cknGBRu1KhUTm2PzjO4F9'

ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKTUuQAAAAAAtVMF7IGhX%2B6Mg1aqiqTByucW%2FsE%3Dz0co0E7EbvNwkjstY27fgtR9mVO5ilEgFe1BPoiBXS31FI2Wfq'

# collegename = 'mit'

# with open('dataPositive.json', 'w') as outfile:
#     json.dump(data, outfile)


def get_tweets(query):
	if twt.objects.filter(institute_name__iexact = query).count() >= 1:
		print("institute already exists")
		return
	queryPostiive =  query
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	data = twitter.search(q=queryPostiive, count='100')

	# twt.objects.all().delete()
	try:
		t = twt(institute_name = query,twitter_json = json.dumps(data))
		t.save()
	except Exception:
		print(Exception)
	for tweet in data['statuses']:
		try:
			tw = tweets(tweet_id = tweet['id'],
						favorited = tweet['favorited'],
						favorite_count = tweet['favorite_count'],
						retweeted = tweet['retweeted'],
						retweet_count = tweet['retweet_count'],
						source = tweet['source'],
						text = tweet['text'],
						user_name = tweet['user']['name'],
						user_id = tweet['user']['id'],
						institute = t)
			tw.save()
		except Exception:
			print(Exception)

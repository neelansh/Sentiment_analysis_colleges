from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# from .sending_req import get_posts
from .postdata import get_posts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import pages, twitter
import json
from json import JSONEncoder
from .twt import get_tweets

# Create your views here.
@csrf_exempt
@require_http_methods([ "GET" , "POST"])
def home(request):
	if(request.method == "GET"):
		return render(request , "analysis/home.html")
	else:
		get_posts(request.POST.get("college_name" , ""))
		get_tweets(request.POST.get("college_name" , ""))
		json_array = get_json_array()
		twitter_data = json.loads(twitter.objects.all()[0].twitter_json)
		context = { 'pages' : pages.objects.all(),
					'institute_name': request.POST.get('college_name' , ''),
					'number_of_pages' : pages.objects.all().count(),
					'json_obj': json_array,
					'tweet_json': twitter_data,
					'total_likes': get_total_likes(json_array),
					'total_posts': get_total_posts(json_array),
					'posts_text': get_posts_text(json_array),
					'total_retweet_count': get_total_retweets(twitter_data),
					'total_tweets': len(twitter_data['statuses'])}
		return render(request , "analysis/display.html" , context)

def get_json_array():
	res = []
	for page in pages.objects.all():
		json_obj = page.page_json
		res.append(json.loads(json_obj))
	return res


def get_total_likes(pages):
	total_likes = 0
	for page in pages:
		total_likes = total_likes + page['engagement']['count']
	return total_likes


def get_total_posts(pages):
	total_posts = 0
	for page in pages:
		total_posts = total_posts + len(page['posts']['data'])
	return total_posts

def get_posts_text(pages):
	posts_text = []
	for i in range(5):
		posts_text.append(pages[i]['posts']['data'])
	# posts_text = pages[0]['posts']['data']
	return posts_text

def get_total_retweets(twitter_data):
	count = 0
	for tweet in twitter_data['statuses']:
		count = count + tweet['retweet_count']
	return count
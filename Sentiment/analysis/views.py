from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# from .sending_req import get_posts
from .postdata import get_posts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import pages, twitter , tweets, fullform
import json
from json import JSONEncoder
from .twt import get_tweets
from django.db.models import Sum
from .youtube import *
from django.db.models import Q
from .insta3 import get_insta
from .flickr import get_flickr
from django.db.models import Count, Max

# Create your views here.
@csrf_exempt
@require_http_methods([ "GET" , "POST"])
def home(request):
	if(request.method == "GET"):
		return render(request , "analysis/home.html")
	else:
		college_name = request.POST.get("college_name" , "")
		college_name_full = get_fullform(college_name)

		get_posts(college_name_full)
		get_tweets(college_name)

		json_array = get_json_array(college_name_full)
		twitter_obj = twitter.objects.get(institute_name = college_name)
		twitter_data = json.loads(twitter_obj.twitter_json)

		context = { 'institute_name': college_name,
					'number_of_pages' : pages.objects.filter(institute_name = college_name_full).count(),
					'json_obj': json_array,
					'tweet_json': twitter_data,
					'total_likes': get_total_likes(json_array),
					'total_posts': get_total_posts(json_array),
					'posts_text': get_posts_text(json_array),
					'total_retweet_count': tweets.objects.filter(institute = twitter_obj).aggregate(Sum('retweet_count'))["retweet_count__sum"],
					'total_tweets': tweets.objects.filter(institute = twitter_obj).count(),
					'youtube_viewed': get_link_viewed(college_name_full),
					'youtube_relevant': get_link_relevant(college_name_full),
					'insta': get_insta(college_name),
					'flickr': get_flickr(college_name),
					'most_active_tweeter': get_most_activeuser(college_name),
					'most_retweeted_tweets': get_most_retweeted(college_name)}
		return render(request , "analysis/display.html" , context)


@csrf_exempt
@require_http_methods([ "GET" , "POST"])
def compare(request):
	if(request.method == "GET"):
		return render(request , "analysis/compare.html")
	else:
		college_name = request.POST.get("college_name" , "")
		college_name_full = get_fullform(college_name)
		get_posts(college_name)
		get_tweets(college_name)

		json_array = get_json_array(college_name)
		twitter_obj = twitter.objects.get(institute_name = college_name)
		twitter_data = json.loads(twitter_obj.twitter_json)

		context = { 'institute_name': college_name,
					'number_of_pages' : pages.objects.filter(institute_name = college_name).count(),
					'json_obj': json_array,
					'tweet_json': twitter_data,
					'total_likes': get_total_likes(json_array),
					'total_posts': get_total_posts(json_array),
					'posts_text': get_posts_text(json_array),
					'total_retweet_count': tweets.objects.filter(institute = twitter_obj).aggregate(Sum('retweet_count'))["retweet_count__sum"],
					'total_tweets': tweets.objects.filter(institute = twitter_obj).count(),
					'youtube_viewed': get_link_viewed(college_name_full),
					'youtube_relevant': get_link_relevant(college_name_full),
					'insta': get_insta(college_name),
					'flickr': get_flickr(college_name),
					'most_active_tweeter': get_most_activeuser(college_name),
					'most_retweeted_tweets': get_most_retweeted(college_name)}

		college_name = request.POST.get("college_name_2" , "")
		college_name_full = get_fullform(college_name)
		get_posts(college_name)
		get_tweets(college_name)

		json_array = get_json_array(college_name)
		twitter_obj = twitter.objects.get(institute_name = college_name)
		twitter_data = json.loads(twitter_obj.twitter_json)

		context['institute_name_2'] = college_name
		context['number_of_pages_2'] = pages.objects.filter(institute_name = college_name).count()
		context['json_obj_2'] = json_array
		context['tweet_json_2'] = twitter_data
		context['total_likes_2'] = get_total_likes(json_array)
		context['total_posts_2'] = get_total_posts(json_array)
		context['posts_text_2'] = get_posts_text(json_array)
		context['total_retweet_count_2'] = tweets.objects.filter(institute = twitter_obj).aggregate(Sum('retweet_count'))["retweet_count__sum"]
		context['total_tweets_2'] = tweets.objects.filter(institute = twitter_obj).count()
		context['youtube_viewed_2'] = get_link_viewed(college_name_full)
		context['youtube_relevant_2'] = get_link_relevant(college_name_full)
		context['insta_2'] = get_insta(college_name)
		context['flickr_2'] = get_flickr(college_name)
		context['most_active_twitter_2'] = get_most_activeuser(college_name)
		context['most_retweeted_tweets_2'] = get_most_retweeted(college_name)

		return render(request , "analysis/display2.html" , context)

def get_fullform(name):
	if(fullform.objects.filter(short_form__iexact = name).exists()):
		return fullform.objects.filter(short_form__iexact = name)[0].full_form
	else:
		return name


def get_json_array(college_name):
	res = []
	for page in pages.objects.filter(institute_name = college_name):
		json_obj = page.page_json
		res.append(json.loads(json_obj))
	return res


def get_total_likes(pages):
	total_likes=0
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
	for i in range(2):
		try:
			posts_text.append(pages[i]['posts']['data'])
		except Exception:
			print(Exception)
	# posts_text = pages[0]['posts']['data']
	return posts_text

def get_total_retweets(twitter_data):
	count = 0
	for tweet in twitter_data['statuses']:
		count = count + tweet['retweet_count']
	return count

def get_most_activeuser(college_name):
	t = tweets.objects.filter(institute = twitter.objects.get(institute_name = college_name))
	result = t.annotate(num_tweets = Count("user_id")).order_by('-num_tweets')[:3]
	return result

def get_most_retweeted(college_name):
	t = tweets.objects.filter(institute = twitter.objects.get(institute_name = college_name))
	return t.annotate(Max("retweet_count"))[:3]

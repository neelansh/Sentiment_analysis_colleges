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
		context = { 'pages' : pages.objects.all(),
					'institute_name': request.POST.get('college_name' , ''), 
					'number_of_pages' : pages.objects.all().count(),
					'json_obj': get_json_array(),
					'tweet_json': json.loads(twitter.objects.all()[0].twitter_json)}
		return render(request , "analysis/display.html" , context)

def get_json_array():
	res = []
	for page in pages.objects.all():
		json_obj = page.page_json
		res.append(json.loads(json_obj))
	return res

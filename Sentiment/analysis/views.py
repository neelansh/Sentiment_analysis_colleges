from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# from .sending_req import get_posts
from .postdata import get_posts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
@require_http_methods([ "GET" , "POST"])
def home(request):
	if(request.method == "GET"):
		return render(request , "analysis/home.html")
	else:
		get_posts(request.POST.get("college_name" , "") , '')
		# return render(request , "analysis/display.html" , result)
		return HttpResponse("<p>it ran seems ok</p>")



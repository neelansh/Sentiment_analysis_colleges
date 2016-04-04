from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods([ "GET" , "POST"])
def home(request):
	if(request.method == "GET"):
		return render(request , "analysis/home.html")
	else:
		pass



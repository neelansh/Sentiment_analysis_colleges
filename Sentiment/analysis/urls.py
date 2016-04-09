#add urls
from django.conf.urls import url
from .views import home, compare

urlpatterns = [
    url(r'^home$', home , name = "home"),
    url(r'^compare$', compare , name = "compare")
]

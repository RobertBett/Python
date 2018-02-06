from django.conf.urls import url
from . import views           # This line is new!
from django.utilis.crypto import get_random_string
urlpatterns = [
url(r'^$', views.index),
url(r'^time_display$', views.time),
url(r'^generate$',views.generate),
url(r'^reset$',views.reset),
]
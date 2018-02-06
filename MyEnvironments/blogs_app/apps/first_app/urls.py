from django.conf.urls import url
from . import views       
urlpatterns = [
    url(r'^$', views.index),
    url(r'^mail$',views.mail),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^wow$', views.wow),
    url(r'^(?P<blog_id>\d+)$', views.show),
    url(r'^(?P<blog_id>\d+)/edit$', views.edit),
    url(r'^(?P<blog_id>\d+)/delete$', views.delete)    
]
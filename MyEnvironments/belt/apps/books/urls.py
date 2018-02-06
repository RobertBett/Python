from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<book_id>\d+)$', views.show),
    url(r'^create/(?P<book_id>\d+)$', views.create_review),


]

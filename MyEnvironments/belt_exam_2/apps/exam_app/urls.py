from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main$',views.index),
    url(r'^new$',views.create_user),
    url(r'^travels$',views.display),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^travels/destination/(?P<id>\d+)$',views.trip),
    url(r'^travels/add$',views.add_trip),
    url(r'^travels/create_trip$',views.create_trip),
    url(r'^join/(?P<id>\d+)$',views.join),
    url(r'^remove/(?P<id>\d+)$',views.remove),
]

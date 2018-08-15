from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^qrcodes$', views.qrcodes, name='qrcodes'),
    url(r'^posts/details/(?P<id>\d+)/$', views.details, name='details'),
]
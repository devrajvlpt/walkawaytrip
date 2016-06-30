from django.conf.urls import patterns, url, include
from mytrips import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
		url(r'^$', views.index),
		url(r'^travel', views.travel),
        ]
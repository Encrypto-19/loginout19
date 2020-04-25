from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.logio_index, name='logio_index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^submit_article/$', views.submit_article, name = 'submit_article'),
    url(r'^user_all_article/$', views.user_all_article, name = 'user_all_article'),
    url(r'^user_specific_article/([0-9]+)$', views.user_specific_article, name = 'user_specific_article'),
]

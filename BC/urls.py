from django.urls import path
from django.conf.urls import url
from django.contrib import admin
# from .views import articlespage, successpage
from . import views

urlpatterns = [
    # url(r'^$',views.index,name = 'index'),
    url(r'^map$',views.map,name = 'map')
    # url(r'^$', articlespage, name='homepage'),
    # url(r'^success$', successpage, name='successpage'),
]
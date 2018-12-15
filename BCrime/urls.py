"""BCrime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# url mapping
from django.contrib import admin
from django.urls import path
from BC import views
from django.conf.urls import url
from BC.views import index, map, new_incident, new_ilocation, new_itime
from django.conf.urls import url, include

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),

    url(r'^map', map),
    path('map', views.map, name='map'),

    url(r'^new_incident$', new_incident),
    path('new_incident', views.new_incident, name='new_incident'),

    path('new_itime', views.new_itime, name='new_itime'),
    url(r'^new_itime$', new_itime),

    path('new_ilocation', views.new_ilocation, name='new_ilocation'),
    url(r'^new_ilocation', new_ilocation),
]



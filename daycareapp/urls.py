from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns=[
    # url('^$',views.daycareapp, name = 'daycareapp'),
    url(r'^$', views.staffProfile, name = 'staffProfile'),
]
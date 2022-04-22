# from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns=[
    # url('^$',views.daycareapp, name = 'daycareapp'),
    re_path(r'^$', views.staffProfile, name = 'staffProfile'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
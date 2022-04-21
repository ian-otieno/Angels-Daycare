from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
   url(r'^$', views.index, name='index'),
    path('services/', views.image, name='services'),
    path('enrollment/', views.enrollment, name='enrollment'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

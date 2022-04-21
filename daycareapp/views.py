from django.shortcuts import render
from .models import StaffProfile 
from django.http import HttpResponse, Http404
from .models import Images

# Create your views here.

# Image View

def image(request,image_id):
    try:
        image = Images.objects.get(id = image_id)
    except Images.DoesNotExist:
        raise Http404()


# Profile View

def staffProfile(request):
    daycareapp = StaffProfile.objects.all()
    params = {
        'daycareapp': daycareapp,
    }
    return render(request, 'about.html', params)

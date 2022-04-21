from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Images,ChildEnrollment
from .forms import ChildEnrollmentForm

# Create your views here.
def index(request):

    images = Images.objects.all()
    return render(request, 'base.html',  {"images": images,})

def image(request,image_id):
    try:
        image = Images.objects.get(id = image_id)
    except Images.DoesNotExist:
        raise Http404()
    
    return render(request,"image.html", {"image":image})

def enrollment(request):
   form=ChildEnrollmentForm()
   return render(request, 'childenrol.html',  {"form": form,})

   
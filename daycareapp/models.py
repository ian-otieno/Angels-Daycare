from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Image Model

class Images(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()@classmethod

def update_image(cls, id,value):
        image = cls.objects.filter(id=id).update(image_name=value)
        return image
   
@classmethod
def get_image_by_id(cls, image_id):
        image= cls.objects.filter(id = image_id)
        return image


# Staff Profile Model

class staffProfile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.profile

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        

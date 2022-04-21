from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
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

class ChildEnrollment(models.Model):
     child_name= models.CharField(max_length=50)
     gender=models.CharField(max_length=50) 
     age=models.IntegerField()
     monthly_charges=models.IntegerField(2500)
from django import forms
from django.contrib.auth.models import User

from daycareapp.models import ChildEnrollment


class ChildEnrollmentForm(forms.ModelForm):
    
  class Meta:
        model = ChildEnrollment
        fields = '__all__'
  
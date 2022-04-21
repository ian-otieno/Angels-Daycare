from django import forms
from django.contrib.auth.models import User


class ChildEnrollmentForm(forms.ModelForm):
    child_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    gender = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    age= forms.IntegerField(max_length=2, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    monthly_charges = forms.IntegerField(required=2500, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))

    class Meta:
        model = User
        fields = ['child_name', 'gender', 'age', 'monthly charges', '']

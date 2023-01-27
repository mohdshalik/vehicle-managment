from django.forms import fields
from .models import vehicle_detail
from django import forms

class vehicle_form(forms.ModelForm):
    class Meta:
        model = vehicle_detail
        fields ='__all__'
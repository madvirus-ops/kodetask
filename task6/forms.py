from django.db import models
from django import forms
from .models import Hotel_Data

class Hotel_Data_Form(forms.ModelForm):
    class Meta:
        model = Hotel_Data
        fields = '__all__'
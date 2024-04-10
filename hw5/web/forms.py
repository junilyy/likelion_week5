from django import forms
from .models import person

class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['name','event','position','intro','elite','live','age']
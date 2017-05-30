#form.py
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Colors


class ColorsForm(forms.ModelForm):

    class Meta:
        model = Colors
        fields = ('title','description', 'color', 'secondary_color','third_color')
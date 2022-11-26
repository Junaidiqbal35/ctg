from django import forms
from .models import FileMaker


class FileMakerForm(forms.ModelForm):
    class Meta:
        model = FileMaker
        fields = '__all__'

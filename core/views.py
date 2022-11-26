from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .forms import FileMakerForm
from .models import FileMaker


class FileMakerView(CreateView):
    model = FileMaker
    form_class = FileMakerForm
    template_name = 'filmmaker.html'

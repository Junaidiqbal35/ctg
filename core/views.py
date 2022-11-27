from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, DetailView, ListView
from .forms import FileMakerForm
from .models import FileMaker


class CreateFileMakerView(CreateView):
    model = FileMaker
    form_class = FileMakerForm
    template_name = 'filmmaker.html'


class FileMakerDetailView(DetailView):
    model = FileMaker
    slug_field = 'pk'
    context_object_name = 'file_maker_detail'
    template_name = 'filmmaker_detail.html'


class FileMakerListView(ListView):
    paginate_by = 50
    template_name = "file_maker_list.html"
    queryset = FileMaker.objects.all()
    context_object_name = 'file_maker_list'
    # filterset_class = StudentFilter
    model = FileMaker

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = self.filterset_class
    #     return context

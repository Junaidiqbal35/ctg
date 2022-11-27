import django_filters
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, DetailView, ListView
from django_filters.views import FilterView

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


class FileMakerFilter(django_filters.FilterSet):
    class Meta:
        model = FileMaker
        fields = ['first_name', 'last_name', 'agencyCompany', 'department',
                  'email', 'phone', 'country', 'skype_name', 'city', 'state']


class FileMakerListView(ListView):
    paginate_by = 50
    template_name = "file_maker_list.html"
    queryset = FileMaker.objects.all()
    context_object_name = 'file_maker_list'
    filterset_class = FileMakerFilter
    model = FileMaker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset_class
        return context


class SearchFileMakerListView(FilterView):
    model = FileMaker
    context_object_name = 'file_maker_list'
    filterset_class = FileMakerFilter
    paginate_by = '10'

    template_name = 'file_maker_list.html'

    queryset = FileMaker.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            qs = FileMaker.objects.filter(Q(first_name=query) | Q(last_name=query) | Q(email=query) |
                                          Q(phone=query) | Q(country=query) | Q(skype_name=query) |
                                          Q(city=query) | Q(state=query) |
                                          Q(agencyCompany=query) | Q(department__icontains=query)).order_by('-id')
            return qs
        return qs

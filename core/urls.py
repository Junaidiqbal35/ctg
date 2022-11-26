
from django.urls import path
from .views import FileMakerView
urlpatterns = [
    path('index/', FileMakerView.as_view(), name='file_maker')
    # path('', include('core.urls'))
]

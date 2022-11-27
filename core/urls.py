from django.urls import path
from .views import CreateFileMakerView, FileMakerDetailView, FileMakerListView

urlpatterns = [
    path('index/', CreateFileMakerView.as_view(), name='create_file_maker'),
    path('file-maker/detail/<int:pk>/', FileMakerDetailView.as_view(), name='file_maker_detail'),
    path('file-maker/list/', FileMakerListView.as_view(), name='file_maker_list_view'),

    # path('', include('core.urls'))
]

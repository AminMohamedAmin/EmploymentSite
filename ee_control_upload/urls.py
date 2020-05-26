from django.urls import path
from .views import save_file, read_file, update_file, delete_file

urlpatterns = [
    path('savefile/<str:username>/',save_file,name='savefile'),
    path('read/<str:username>/',read_file,name='read'),
    path('update/<str:username>/',update_file,name='update'),
    path('delete/<str:username>/',delete_file,name='delete'),
]
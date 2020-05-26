from django.urls import path
from .views import index, like, dislike, love, loved
from . import views

urlpatterns = [
    path('index/<str:username>/',index,name='index'),
    path('like/<str:username>/',like,name='like'),
    path('dislike/<str:username>/',dislike,name='dislike'),
    path('love/<str:username>/',love,name='love'),
    path('loved/',loved,name='loved'),
]
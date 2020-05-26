from django.urls import path
from .views import home_page, gmail, sub

urlpatterns = [
    path('',home_page,name='homepage'),
    path('gmail/',gmail,name='gmail'),
    path('sub/',sub,name='sub'),
]
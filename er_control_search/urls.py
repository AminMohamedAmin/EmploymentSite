from django.urls import path
from .views import posts_list, posts_detail, home


urlpatterns = [
    path('lists/', posts_list, name='lists'),
    path('details/<int:id>/', posts_detail, name='details'),
    path('home/', home, name='home'),
]
from django.urls import path
from .views import form, post_create, post_detail, post_list, post_delete


urlpatterns = [
    path('form/',form,name='form'),
    path('create/',post_create,name='create'),
    path('detail/<int:id>/',post_detail,name='detail'),
    path('list/', post_list, name='list'),
    # path('edit/<int:id>/',post_update,name='update'),
    path('delete/<int:id>/',post_delete,name='delete'),

]
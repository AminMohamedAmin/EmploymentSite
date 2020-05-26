from django.urls import path
from .views import in_loginn, up_sighnn, employee_loginn, employer_loginn, employer_logoutt, backhomee

urlpatterns = [
    path('inlogg/',in_loginn,name='inlogg'),
    path('upsighnn/',up_sighnn,name='upsighnn'),
    path('logineee/',employee_loginn,name='logineee'),
    path('logouteee/',employer_logoutt,name='logouteee'),
    path('loginerr/',employer_loginn,name='loginerr'),
    path('backhomee/',backhomee,name='backhomee'),
]
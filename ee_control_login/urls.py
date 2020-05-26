from django.urls import path
from .views import in_log, up_sighn, employee_login, employer_login, employee_logout, backhome

urlpatterns = [
    path('inlog/',in_log,name='inlog'),
    path('upsighn/',up_sighn,name='upsighn'),
    path('loginee/',employee_login,name='loginee'),
    path('logoutee/',employee_logout,name='logoutee'),
    path('loginer/',employer_login,name='loginer'),
    path('backhome/',backhome,name='backhome'),
]
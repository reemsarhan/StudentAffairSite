from django.urls import path, include
from django.contrib.auth.views import LoginView as login, LogoutView as logout

from . import views

app_name = 'urls'

urlpatterns = [
    path('', views.index),
    path('login/', login.as_view(template_name='login.html'), name='login'),
    path('logout/', logout.as_view(), name='logout'),
]

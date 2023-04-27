from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LogInForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.signup, name='sign_up'),
    path('log_in/', auth_views.LoginView.as_view(template_name='core/log_in.html', authentication_form=LogInForm), name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    
]

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url('signup/', views.SignUp.as_view(), name='signup'),
]
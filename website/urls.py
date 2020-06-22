from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login.html', views.login, name="login"),
    path('qrform.html', views.qrform, name="qrform"),
    path('register.html', views.register, name="register"),
    path('dashboard.html', views.dashboard, name="dashboard"),
]

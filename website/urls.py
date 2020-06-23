from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('login.html', views.login, name="login"),
    path('qrform.html', views.qrform, name="qrform"),
    path('dashboard.html', views.dashboard, name="dashboard"),
    path('dashboard_table.html', views.dashboard_table, name="dashboard_table"),
]

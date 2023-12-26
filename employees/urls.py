# employee/urls.py
from django.urls import path
from . import views

app_name = 'employees'  # Namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('Loginpage/', views.Loginpage, name='Loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('check_in', views.check_in, name='check_in'),
    
    # Add other paths as needed
]

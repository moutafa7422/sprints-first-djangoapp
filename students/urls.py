from django.urls import path 
from . import views



urlpatterns = [
    
    path('', views.list_view, name = 'list'),

    path('login/', views.home_view, name = 'login'),
]

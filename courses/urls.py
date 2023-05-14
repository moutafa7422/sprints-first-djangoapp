from django.urls import path 
from . import views


urlpatterns = [

    path('', views.cours_list, name='Courses List'),
    
]
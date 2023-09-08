from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutme/', views.aboutme, name='about me'),
]
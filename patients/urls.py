from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('dashboard/', views.stats, name='dashboard'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('stats/', views.stats, name='stats'),
    
]

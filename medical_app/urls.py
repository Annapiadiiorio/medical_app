
from django.contrib import admin
from django.urls import path
from patients import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('stats/', views.stats, name='stats'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path
from patients import views

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 👈 questa riga fa puntare la home alla dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('stats/', views.dashboard, name='stats'),
]

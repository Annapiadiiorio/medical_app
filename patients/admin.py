from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Patient, Exam


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'eta', 'genere', 'diagnosi', 'tipologia', 'modalita_diagnosi')
    list_filter = ('genere', 'diagnosi', 'tipologia')
    search_fields = ('nome', 'cognome', 'diagnosi')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('paziente', 'nome_esame', 'appropriato')
    list_filter = ('appropriato',)
    search_fields = ('nome_esame',)


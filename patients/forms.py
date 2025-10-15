from django import forms
from .models import Patient, Exam

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['paziente', 'nome_esame', 'appropriato']

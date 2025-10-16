from django.shortcuts import render, redirect
from .models import Patient, Exam
from .forms import PatientForm, ExamForm

def home(request):
    return render(request, 'patients/home.html')



def dashboard(request):
    maschi = Patient.objects.filter(genere="M").count()
    femmine = Patient.objects.filter(genere="F").count()

    totale_pazienti = Patient.objects.count()
    totale_esami = Exam.objects.count()
    percentuale_appropriati = 0
    media_esami = 0

    labels_genere = ["Maschi", "Femmine"]
    data_genere = [maschi, femmine]

    context = {
        "totale_pazienti": totale_pazienti,
        "totale_esami": totale_esami,
        "percentuale_appropriati": percentuale_appropriati,
        "media_esami": media_esami,
        "labels_genere": labels_genere,
        "data_genere": data_genere,
    }

    return render(request, "patients/dashboard.html", context)


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})



def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats')
    else:
        form = ExamForm()
    return render(request, 'patients/exam_form.html', {'form': form})

def home(request):
    return redirect('dashboard')


from django.shortcuts import render, redirect
from .models import Patient, Exam
from .forms import PatientForm, ExamForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats')
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
    return render(request, 'patients/home.html')

from django.db.models import Count, Q
from django.shortcuts import render
from .models import Patient, Exam

from django.db.models import Count
from django.shortcuts import render
from .models import Patient, Exam

def stats(request):
    pazienti = Patient.objects.all()
    esami = Exam.objects.all()

    totale_pazienti = pazienti.count()
    totale_esami = esami.count()
    tot_appropriati = esami.filter(appropriato=True).count()

    # ✅ Calcolo protetto per evitare divisioni per zero
    if totale_esami > 0:
        percentuale_appropriati = round((tot_appropriati / totale_esami) * 100, 2)
    else:
        percentuale_appropriati = 0

    # ✅ Sempre definita
    percentuale_non_appropriati = 100 - percentuale_appropriati
    media_esami_paziente = round(totale_esami / totale_pazienti, 2) if totale_pazienti > 0 else 0

    # Grafici
    labels_pazienti = [f"{p.nome} {p.cognome}" for p in pazienti]
    esami_paziente = [p.esami.count() for p in pazienti]

    # Distribuzione per tipologia (solo se il campo esiste)
    try:
        tipologie = pazienti.values('tipologia').annotate(tot=Count('id'))
    except Exception:
        tipologie = []

    context = {
        'totale_pazienti': totale_pazienti,
        'totale_esami': totale_esami,
        'tot_appropriati': tot_appropriati,
        'percentuale_appropriati': percentuale_appropriati,
        'percentuale_non_appropriati': percentuale_non_appropriati,
        'media_esami_paziente': media_esami_paziente,
        'labels_pazienti': labels_pazienti,
        'esami_paziente': esami_paziente,
        'tipologie': list(tipologie),
    }

    return render(request, 'patients/dashboard.html', context)

from django.shortcuts import render
from .models import Diagnosis

def diagnosis_list(request):
    diagnoses = Diagnosis.objects.all()
    return render(request, 'diagnoses/diagnosis_list.html', {'diagnoses': diagnoses})



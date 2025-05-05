# patients/forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'patient_id',
            'name',
            'birth_date',
            'age',
            'gender',
            'blood_type',
            'allergies',
            'medical_conditions',
        ]

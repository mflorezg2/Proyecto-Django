# patients/urls.py
from django.urls import path
from .views import patient_list, patient_create, patient_detail

urlpatterns = [
    path('',         patient_list,   name='patient_list'),
    path('create/',  patient_create, name='patient_create'),
    path('<int:pk>/',patient_detail, name='patient_detail'),
]



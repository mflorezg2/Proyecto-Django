from django.urls import path
from .views import diagnosis_list

urlpatterns = [
    path('', diagnosis_list, name='diagnosis_list'),
]


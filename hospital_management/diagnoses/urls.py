from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.diagnosis_list, name='diagnosis_list'),
]

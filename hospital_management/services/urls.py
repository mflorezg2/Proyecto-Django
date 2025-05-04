from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.service_list, name='service_list'),
]

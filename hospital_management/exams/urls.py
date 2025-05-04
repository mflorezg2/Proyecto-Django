from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.exam_list, name='exam_list'),
]

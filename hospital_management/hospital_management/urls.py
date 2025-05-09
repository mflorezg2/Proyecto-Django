"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# hospital_management/views.py
# hospital_management/urls.py
from django.contrib import admin
from django.urls import path, include
from views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('exams/', include('exams.urls')),
    path('services/', include('services.urls')),
    path('patients/', include('patients.urls')),
    path('diagnoses/', include('diagnoses.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),  # Auth0 endpoints
]




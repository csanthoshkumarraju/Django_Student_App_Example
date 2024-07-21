# urls.py (app level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register_student'),
    # Define other URLs as needed
]


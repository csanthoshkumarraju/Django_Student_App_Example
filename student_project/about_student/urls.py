# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('about_student/<int:student_id>/', views.about_student, name='about_student'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('logout/', views.logout_view, name='logout'),
    # Add other URLs as needed
]

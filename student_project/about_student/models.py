from django.db import models
from student_registration_app.models import Student

class EducationDetail(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    Education_SSC_School_Name = models.CharField(max_length=500,null=True)
    Education_SSC_school_Grade = models.CharField(max_length=50,null=True)
    Education_SSC_school_Location = models.CharField(max_length=500,null=True)
    Education_Inter_College_Name = models.CharField(max_length=500,null=True)
    Education_Inter_College_Grade = models.CharField(max_length=50,null=True)
    Education_Inter_College_Location = models.CharField(max_length=500,null=True)
    Education_Btech_Degree_College_Name = models.CharField(max_length=500,null=True)
    Education_Btech_Degree_College_Grade = models.CharField(max_length=50,null=True)
    Education_Btech_Degree_College_Location = models.CharField(max_length=500,null=True)
    Today_homework_todo = models.TextField(max_length=100000,null=True)
    Today_homework_completed = models.TextField(max_length=100000,null=True)
    Future_goal_plans = models.TextField(max_length=100000,null=True)
    Future_goal_plans_completed = models.TextField(max_length=100000,null=True)

    # goals = models.TextField(blank=True)
    # homework = models.TextField(blank=True)
    
    def __str__(self):
        return f"Education details of {self.student.name}"
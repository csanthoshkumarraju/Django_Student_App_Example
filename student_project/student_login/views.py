from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from student_registration_app.models import Student

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            try:
                student = Student.objects.get(phone_number=phone_number)
                if student.password == password:
                    request.session['student_id'] = student.id
                    # return redirect('about_student',student_id=student.id) 
                    return redirect('student_detail',student_id=student.id) 
                else:
                    form.add_error(None, "Incorrect password")
            except Student.DoesNotExist:
                form.add_error(None, "Student with this phone number does not exist")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

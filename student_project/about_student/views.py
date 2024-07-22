from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, EducationDetail
from .forms import EducationDetailForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# def about_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     context = {
#         'student_id': student_id  
#     }
#     return render(request, 'about_student.html', context)

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     education_detail, created = EducationDetail.objects.get_or_create(student=student)
    
#     if request.method == 'POST':
#         form = EducationDetailForm(request.POST, instance=education_detail)
#         if form.is_valid():
#             form.save()
#             return redirect('student_detail', student_id=student_id)
#     else:
#         form = EducationDetailForm(instance=education_detail)
    
#     context = {
#         'student': student,
#         'form': form,
#         'education_detail': education_detail,
#     }
#     return render(request, 'about_student.html', context)
# @login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    education_detail, created = EducationDetail.objects.get_or_create(student=student)
    
    if request.method == 'POST':
        form = EducationDetailForm(request.POST, instance=education_detail)
        if form.is_valid():
            form.save()
            # Redirect to the same view to display updated data
            return redirect('student_detail', student_id=student_id)
    else:
        form = EducationDetailForm(instance=education_detail)
    
    context = {
        'student': student,
        'form': form,
        'education_detail': education_detail,
    }
    return render(request, 'about_student.html', context)
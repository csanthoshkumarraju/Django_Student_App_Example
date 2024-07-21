from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages framework
from .forms import StudentForm
from .models import Student

# def register_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             print(f"Attempting to register student with name: {name}")
#             # Check if a student with the same name already exists
#             if Student.objects.filter(name=name).exists():
#                 messages.error(request, f'A student with the name "{name}" already exists.')
#             else:
#                 form.save()
#                 return HttpResponse('Registration successful!')
#                 # return redirect('registration_success')  # Replace 'registration_success' with your success URL name
#     else:
#         form = StudentForm()
    
#     return render(request, 'registration.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Check if a student with the same name already exists
            if Student.objects.filter(name=name).exists():
                messages.error(request, f'A student with the name "{name}" already exists.')
            email = form.cleaned_data['email']
            if Student.objects.filter(email=email).exists():
                messages.error(request, f'A student with the email "{email}" already exists.')
            phone_number = form.cleaned_data['phone_number']
            # Check if a student with the same phone number already exists
            if Student.objects.filter(phone_number=phone_number).exists():
                messages.error(request, f'A student with the phone number "{phone_number}" already exists.')
            else:
                form.save()
                # return HttpResponse('Registration successful!')
                return redirect('login')  # Redirect to clear form data on reload
        else:
            # Handle form errors if any
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    
    return render(request, 'registration.html', {'form': form})
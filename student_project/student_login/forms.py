from django import forms
from student_registration_app.models import Student

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")

        if phone_number and password:
            try:
                student = Student.objects.get(phone_number=phone_number)
                if student.password != password:
                    raise forms.ValidationError("Incorrect password")
            except Student.DoesNotExist:
                raise forms.ValidationError("Student with this phone number does not exist")
        return cleaned_data

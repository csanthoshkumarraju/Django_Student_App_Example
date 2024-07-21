# # forms.py

# from django import forms
# from .models import Student

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'  # Use '__all__' to include all fields of the Student model
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.fields['name'].widget.attrs.update({
#             'placeholder': 'Enter student name'
#         })
        
#         self.fields['email'].widget.attrs.update({
#             'placeholder': 'Enter student email'
#         })
        
#         self.fields['phone_number'].widget.attrs.update({
#             'placeholder': 'Enter phone number'
#         })
        
#         self.fields['date_of_birth'].widget.attrs.update({
#             'placeholder': 'YYYY-MM-DD/2000-01-01 or DD-MM-YYYY/01/01/2000'
#         })
        
#         self.fields['address'].widget.attrs.update({
#             'placeholder': 'Enter address'
#         })
#         self.fields['password'].widget = forms.PasswordInput()
#         self.fields['password'].widget.attrs.update({
#             'placeholder': 'Enter password'
#         })
#         self.fields['Confirm_password'].widget = forms.PasswordInput()
#         self.fields['Confirm_password'].widget.attrs.update({
#             'placeholder': 'Confirm password'
#         })
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError(
#                 "Password and confirm password do not match."
#             )

#         return cleaned_data

    
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    Confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = '__all__'  # Use '__all__' to include all fields of the Student model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter student name'
        })
        
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter student email'
        })
        
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Enter phone number'
        })
        
        self.fields['date_of_birth'].widget.attrs.update({
            'placeholder': 'YYYY-MM-DD or DD-MM-YYYY'
        })
        
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Enter address'
        })
        
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter password'
        })
        
        self.fields['Confirm_password'].widget = forms.PasswordInput()
        self.fields['Confirm_password'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("Confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('Confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        # Override save method if needed
        return super().save(commit=commit)

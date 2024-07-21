from django import forms
from .models import EducationDetail

class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        # fields = ['goals', 'homework']
        fields = '__all__'
        exclude = ['student']
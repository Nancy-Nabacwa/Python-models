from django import forms
from .models import Classroom


class ClassroomRegistrationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

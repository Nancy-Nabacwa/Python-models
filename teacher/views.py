from django.shortcuts import render
from .forms import TeacherRegistrationForm

def register_teacher(request):
    form = TeacherRegistrationForm()
    return render(request, "teacher/register_teacher.html", {"form":form})

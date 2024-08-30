from django.shortcuts import render
from .forms import ClassroomRegistrationForm

def register_classroom(request):
    form = ClassroomRegistrationForm()
    return render(request, "class_model/register_classroom.html", {"form":form})
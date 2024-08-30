from django.shortcuts import render
from .forms import CourseRegistrationForm

def register_course(request):
    form = CourseRegistrationForm()
    return render(request, "course/register_course.html", {"form":form})
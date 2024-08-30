from django.shortcuts import render
from .forms import ClassPeriodRegistrationForm

def register_classPeriod(request):
    form = ClassPeriodRegistrationForm()
    return render(request, "classPeriod/register_classPeriod.html", {"form":form})
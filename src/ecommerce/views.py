from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def homepage(request):
    forms = ContactForm(request.POST or None)
    context ={
        "form":forms
    }

    if forms.is_valid():
        print(forms.cleaned_data)
    return render(request,"hello.html",context)
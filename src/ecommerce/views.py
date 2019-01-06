from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def homepage(request):
    forms = ContactForm(request.POST or None)
    context ={
        "form": forms
    }
    if forms.is_valid():
        print(forms.cleaned_data)
    return render(request, "contact/contact.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            print('logged in')
            redirect('/login')
        else:
            print('Error')
    return render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", context)

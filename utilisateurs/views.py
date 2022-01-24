from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .form import LoginForm, RegisterForm


def auth(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/articles/")

    return render(request, "users/auth.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            row_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=row_password)
            return redirect("/login/")
    else:
        form = RegisterForm

    return render(request, "users/register.html", {"form": form})

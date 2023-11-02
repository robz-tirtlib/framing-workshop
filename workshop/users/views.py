from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm


def login(request):
    context = {}
    return render(request, "users/login.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            print(form.__dict__)
            context = {}
            return redirect(reverse("workshopapp:index", kwargs=context))

    context = {}
    return render(request, "users/register.html", context)


def profile(request, user_id: int):
    context = {}
    return render(request, "users/profile.html", context)

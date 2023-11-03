from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User

from .forms import RegisterForm


def login(request):
    context = {}
    return render(request, "users/login.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]):
                form.add_error("username", "This field should be unique.")
                return render(request, "users/register.html", {"form": form})

            if User.objects.filter(email=form.cleaned_data["email"]):
                form.add_error("email", "This field should be unique.")
                return render(request, "users/register.html", {"form": form})

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
                )
            user.save()
            context = {}
            return redirect(reverse("workshopapp:index", kwargs=context))
        return render(request, "users/register.html", {"form": form})

    return render(request, "users/register.html", {"form": RegisterForm()})


def profile(request, user_id: int):
    context = {}
    return render(request, "users/profile.html", context)

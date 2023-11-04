from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def forgot_password(request):
    return render(request, "users/forgot_password.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("workshopapp:index"))
        context = {"error": "Wrong credentials."}
        return render(request, "users/login.html", context)
    return render(request, "users/login.html", {})


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

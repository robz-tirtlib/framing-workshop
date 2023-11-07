from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import logout

from .services.auth_service.infrastructure import (
    get_register_response, get_login_response
)

from .services.user_profile_service.infrastructure import (
    get_user_from_request, get_response)

from .forms import RegisterForm

from .dao import UserDAO


def forgot_password(request):
    return render(request, "users/forgot_password.html", {})


def login_user(request):
    if request.method != "POST":
        return render(request, "users/login.html", {})
    return get_login_response(request)


def logout_user(request):
    logout(request)
    return redirect(reverse("workshopapp:index"))


def register(request):
    if request.method != "POST":
        return render(request, "users/register.html", {"form": RegisterForm()})
    return get_register_response(request, UserDAO())


def profile(request, profile_id: int):
    user = get_user_from_request(request)
    return get_response(request, user, profile_id)

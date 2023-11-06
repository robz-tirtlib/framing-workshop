from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login

from users.forms import RegisterForm

from .domain import UserRegisterDTO

from users.dao import UserDAO


def get_user_dto(form: RegisterForm) -> tuple[str]:
    return UserRegisterDTO(
        username=form.cleaned_data.get("username"),
        email=form.cleaned_data.get("email"),
        password=form.cleaned_data.get("password"),
    )


def get_register_response(
        request: HttpRequest,
        user_dao: UserDAO) -> HttpResponse:
    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, "users/register.html", {"form": form})
    user = get_user_dto(form)

    if not is_unique(form, user, user_dao):
        return render(request, "users/register.html", {"form": form})

    user_obj = user_dao.create_user(user)
    login(request, user_obj)

    return redirect(reverse("workshopapp:index"))


def is_unique(
        form: RegisterForm,
        user: UserRegisterDTO,
        user_dao: UserDAO) -> bool:
    if not is_username_unique(user, user_dao):
        form.add_error("username", "This field should be unique.")

    if not is_email_unique(user, user_dao):
        form.add_error("email", "This field should be unique.")

    if (not (is_username_unique(user, user_dao) and
             is_email_unique(user, user_dao))):
        return False
    return True


def is_username_unique(user: UserRegisterDTO, user_dao: UserDAO) -> bool:
    if user_dao.filter_by_username(user.username) is not None:
        return False
    return True


def is_email_unique(user: UserRegisterDTO, user_dao: UserDAO) -> bool:
    if user_dao.filter_by_email(user.email) is not None:
        return False
    return True

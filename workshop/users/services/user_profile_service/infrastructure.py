from django.http import HttpRequest, HttpResponseForbidden, HttpResponse
from django.shortcuts import render

from .domain import UserDTO, is_user_allowed


def get_user_from_request(request: HttpRequest) -> UserDTO | None:
    if not request.user.is_authenticated:
        return None

    return UserDTO(
        id=request.user.id,
        username=request.user.username,
        email=request.user.email,
        password=request.user.password,
    )


def get_response(
        request: HttpRequest,
        user: UserDTO | None,
        profile_id: int) -> HttpResponse:
    if not is_user_allowed(user, profile_id):
        return HttpResponseForbidden("You are not allowed to view this page.")
    return render(request, "users/profile.html")

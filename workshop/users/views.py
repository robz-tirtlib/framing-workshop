from django.shortcuts import render


def login(request):
    context = {}
    return render(request, "users/login.html", context)


# TODO: validate passwords match
# TODO: validate e-mail
def register(request):
    context = {}
    return render(request, "users/register.html", context)


def profile(request, user_id: int):
    context = {}
    return render(request, "users/profile.html", context)

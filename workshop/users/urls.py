from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("forgot-password/", views.forgot_password, name="forgot-password"),
    path("<int:user_id>/", views.profile, name="profile"),
]

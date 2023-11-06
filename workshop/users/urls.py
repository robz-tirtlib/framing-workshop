from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    path("forgot-password/", views.forgot_password, name="forgot-password"),
    path("<int:profile_id>/", views.profile, name="profile"),
]

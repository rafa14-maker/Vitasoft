from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("me/update/", views.update_user_profile, name="update_user_profile"),
    path("me/delete/", views.delete_user_profile, name="delete_user_profile"),
]

from . import views
from django.urls import path

urlpatterns = [
    path("register", views.register, name = "register"),
    path("profile/", views.profile, name = "profile"),
    path("profile/upload-photo", views.CreateProfileView.as_view(), name = 'photo'),
    path("login/", views.MyLoginView.as_view(), name = "login"),
    path("logout/", views.MyLogoutView.as_view(), name = "logout")
]
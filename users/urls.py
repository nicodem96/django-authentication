from . import views
from django.urls import path

urlpatterns = [
    path("", views.profile, name = "profile"),
    path("upload-photo/", views.CreateProfileView.as_view(), name = 'photo')
]
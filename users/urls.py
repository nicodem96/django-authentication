from . import views
from django.urls import path

urlpatterns = [
    path("", views.profile, name = "profile"),
    path("upload-profile/", views.CreateProfileView.as_view(), name = 'update-profile'),
    path("upload-photo/", views.ModifyImageView.as_view(), name = "photo")
]
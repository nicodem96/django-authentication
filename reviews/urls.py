from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewsListView.as_view(), name = 'home'),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.review, name = "review"),
    path("reviews/<int:pk>", views.DetailListView.as_view(), name = "review-detail")
]

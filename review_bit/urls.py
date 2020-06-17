from django.urls import path
from .views import (ReviewListView, ReviewDetailView, ReviewCreate, 
                    ReviewUpdateView, ReviewDeleteView)
from . import views

urlpatterns = [
    path("", ReviewListView.as_view(), name="gamebit-review"),
    path("new/", ReviewCreate, name="gamebit-create"),
    path("<int:pk>/", ReviewDetailView.as_view(), name="gamebit-detail"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="gamebit-edit"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="gamebit-delete"),
]
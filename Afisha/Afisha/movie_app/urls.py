# urls.py
from django.urls import path
from .views import (
    DirectorListCreateView, DirectorUpdateDeleteView,
    MovieListCreateView, MovieUpdateDeleteView,
    ReviewListCreateView, ReviewUpdateDeleteView
)

urlpatterns = [
    path('api/v1/directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('api/v1/directors/<int:pk>/', DirectorUpdateDeleteView.as_view(), name='director-update-delete'),
    path('api/v1/movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('api/v1/movies/<int:pk>/', MovieUpdateDeleteView.as_view(), name='movie-update-delete'),
    path('api/v1/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/v1/reviews/<int:pk>/', ReviewUpdateDeleteView.as_view(), name='review-update-delete'),
]

from .views import RegistrationView, ConfirmationView, LoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('confirm/', ConfirmationView.as_view(), name='confirm'),
    path('login/', LoginView.as_view(), name='login'),
]

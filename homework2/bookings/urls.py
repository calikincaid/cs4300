from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list_view, name="movie_list"),
    path("movies/<int:movie_id>/book/", views.seat_booking_view, name="book_seat"),
    path("bookings/history/", views.booking_history_view, name="booking_history"),
]

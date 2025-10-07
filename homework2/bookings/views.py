from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response


from datetime import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


##########################################

# HTML VIEWS
# ---------------------------

def movie_list_view(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

def seat_booking_view(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        if not seat_id:
            return HttpResponseBadRequest("seat_id is required")

        seat = get_object_or_404(Seat, pk=seat_id)
        if seat.book_status:
            return HttpResponseBadRequest("That seat is already booked.")

        Booking.objects.create(movie=movie, seat=seat, user=request.user, booking_date=datetime.now())
        seat.book_status = True
        seat.save(update_fields=["book_status"])
        return redirect("booking_history")

    available_seats = Seat.objects.filter(book_status=False).order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {"movie": movie, "available_seats": available_seats})

def booking_history_view(request):
    bookings = (
        Booking.objects.filter(user=request.user)
        .select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})
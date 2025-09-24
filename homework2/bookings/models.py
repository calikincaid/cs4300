# Create your models here.
from django.db import models
from django.conf import settings


class Movie(models.Model):
    # 4 FIELDS SPECIFIED IN THE ASSIGNMENT: TITLE, DESC., RELEASE DATE, DURATION
    title = models.CharField(max_length=30)
    description = models.TextField() # NOT PUTTING ANY ARGUMENTS FOR FIELD VALUES FOR NOW 
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title}\n{self.release_date} | {self.duration}\n{self.description}"


class Seat(models.Model):
    seat_number = models.CharField(max_length=3) # ALLOWS SEATS LIKE A99
    book_status = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.movie} @ {self.seat} booked {self.booking_date}"

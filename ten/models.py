from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    booking_count = models.PositiveIntegerField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    remaining_count = models.PositiveIntegerField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    max_bookings = models.PositiveIntegerField(default=0)
    booked_date = models.DateTimeField(auto_now=True)

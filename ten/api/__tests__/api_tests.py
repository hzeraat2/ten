from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from ten.models import Member, Inventory, Booking
from datetime import datetime
import json


class APITest(APITestCase):
    test_booking = None

    @classmethod
    def setUpTestData(cls):
        test_member = Member(
            name="Jon", surname="Doe", booking_count=0, date_joined=datetime.now()
        )
        test_member.save()

        date = datetime(2023, 5, 17)
        test_inventory = Inventory(
            title="Mars",
            description="New holiday destination",
            remaining_count=10,
            expiration_date=date,
        )
        test_inventory.save()

        test_booking = Booking(
            max_bookings=0, inventory=test_inventory, member=test_member
        )
        test_booking.save()

    # booking api

    def test_successful_booking(self):
        response = self.client.post(
            "/api/v1/book/",
            {"name": "Jon", "surname": "Doe", "title": "Mars"},
            format="json",
        )
        decoded_response = response.content.decode()
        self.assertEqual(decoded_response, '{"message":"Booked!","httpStatus":200}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_when_inventory_not_in_DB(self):
        response = self.client.post(
            "/api/v1/book/",
            {"name": "Jon", "surname": "Doe", "title": "Moon"},
            format="json",
        )
        decoded_response = response.content.decode()
        self.assertEqual(
            decoded_response, '{"message":"inventory or member error","httpStatus":401}'
        )

    def test_error_when_member_not_in_DB(self):
        response = self.client.post(
            "/api/v1/book/",
            {"name": "someone", "surname": "not in DB", "title": "Moon"},
            format="json",
        )
        decoded_response = response.content.decode()
        self.assertEqual(
            decoded_response, '{"message":"inventory or member error","httpStatus":401}'
        )

    # cancellation api
    def test_cancel_booking_id(self):
        test_member = Member(
            name="Hi", surname="Jack", booking_count=0, date_joined=datetime.now()
        )
        test_member.save()

        date = datetime(2023, 5, 17)
        test_inventory = Inventory(
            title="Mars",
            description="New holiday destination",
            remaining_count=1,
            expiration_date=date,
        )
        test_inventory.save()

        test_booking = Booking(
            max_bookings=0, inventory=test_inventory, member=test_member
        )
        test_booking.save()

        response = self.client.post(
            "/api/v1/cancel/", {"id": test_booking.id}, format="json"
        )
        decoded_response = response.content.decode()
        self.assertEqual(
            decoded_response, '{"message":"booking cancelled","httpStatus":200}'
        )

    def test_cancel_api_incorrect_booking_id(self):
        response = self.client.post("/api/v1/cancel/", {"id": 1000}, format="json")
        decoded_response = response.content.decode()
        self.assertEqual(
            decoded_response,
            '{"message":"Booking does not exist for this id","httpStatus":401}',
        )

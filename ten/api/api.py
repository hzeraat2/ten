from rest_framework.decorators import api_view
from rest_framework.response import Response
from ten.models import Member, Inventory, Booking
import json
import logging


@api_view(["POST"])
def book(request):
    body = json.loads(request.body)
    member = None
    inventory = None
    try:
        member = Member.objects.get(name=body["name"], surname=body["surname"])
    except Member.DoesNotExist:
        logging.warning("Member.DoesNotExist")

    try:
        inventory = Inventory.objects.get(title=body["title"])
    except Inventory.DoesNotExist:
        logging.warning("Inventory.DoesNotExist")

    if inventory and member:
        booking, created = Booking.objects.get_or_create(
            member=member, inventory=inventory, defaults={"max_bookings": 1}
        )

        if not created:
            if booking.max_bookings >= 2:
                return Response(
                    {
                        "message": "your MAX_BOOKING has reached the maximum 2!",
                        "httpStatus": 401,
                    }
                )
            else:
                if inventory.remaining_count == 0:
                    return Response(
                        {
                            "message": "inventory's remaining count has been depleated try another inventory!",
                            "httpStatus": 401,
                        }
                    )
                booking.max_bookings += 1
                booking.save()

        return Response({"message": "Booked!", "httpStatus": 200})
    else:
        return Response(
            {
                "message": "inventory or member error",
                "httpStatus": 401,
            }
        )


@api_view(["POST"])
def cancel(request):
    body = json.loads(request.body)
    try:
        booking = Booking.objects.get(id=body["id"])
        booking.delete()
        return Response({"message": "booking cancelled", "httpStatus": 200})
    except Booking.DoesNotExist:
        return Response(
            {"message": "Booking does not exist for this id", "httpStatus": 401}
        )

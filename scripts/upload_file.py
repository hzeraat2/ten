import csv
from datetime import datetime
from ten.models import Inventory, Member


def run(*args):

    if args[0] == "Inventory.csv":
        # save inventory
        with open(args[0], "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass  # not interested in titles
                else:
                    title = row[0]
                    description = row[1]
                    remaining_count = row[2]
                    expiration_date = row[3]

                    expiration_date_list = expiration_date.split("/")

                    if len(expiration_date_list) == 3:  # only save rows with valid date
                        year = int(expiration_date_list[2])
                        month = int(expiration_date_list[1])
                        day = int(expiration_date_list[0])
                        formatted_expiration_date = datetime(year, month, day)
                        inventory = Inventory(
                            title=title,
                            description=description,
                            remaining_count=remaining_count,
                            expiration_date=formatted_expiration_date,
                        )
                        inventory.save()

    elif args[0] == "Members.csv":
        # save members
        with open(args[0], "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass  # not interested in titles
                else:
                    name = row[0]
                    surname = row[1]
                    booking_count = row[2]
                    date_joined = row[3]

                    member = Member(
                        name=name,
                        surname=surname,
                        booking_count=booking_count,
                        date_joined=date_joined,
                    )
                    member.save()

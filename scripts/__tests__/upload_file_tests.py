from django.test import TestCase
from ten.models import Inventory, Member
from scripts import upload_file
from datetime import datetime


class InventoryCase(TestCase):
    def setUp(self):
        upload_file.run("Inventory.csv")
        upload_file.run("Members.csv")

    def test_inventory_stores_in_db(self):
        inventory = Inventory.objects.get(title="Bali")
        self.assertEqual(inventory.remaining_count, 5)
        self.assertEqual(
            inventory.description,
            "Suspendisse congue erat ac ex venenatis mattis. Sed finibus sodales nunc, nec maximus tellus aliquam id. Maecenas non volutpat nisl. Curabitur vestibulum ante non nibh faucibus, sit amet pulvinar turpis finibus",
        )

    def test_member_stores_in_db(self):
        member = Member.objects.get(name="Sophie", surname="Davis", booking_count=1)
        self.assertEqual(member.name, "Sophie")
        self.assertEqual(member.surname, "Davis")
        self.assertEqual(member.booking_count, 1)

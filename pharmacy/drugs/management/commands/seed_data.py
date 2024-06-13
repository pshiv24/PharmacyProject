from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from drugs.models import Drug
from orders.models import Order


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Users
        users = [
            {"username": "admin1", "password": "adminpass", "role": "admin"},
            {"username": "customer1", "password": "customerpass", "role": "customer"},
        ]

        for user_data in users:
            user = User.objects.create_user(
                username=user_data["username"], password=user_data["password"]
            )
            if user_data["role"] == "admin":
                user.is_admin = True
                user.is_customer = False
            user.save()

        # Drugs
        drugs = [
            {
                "name": "Aspirin",
                "description": "Pain reliever and fever reducer",
                "price": 5.99,
            },
            {
                "name": "Ibuprofen",
                "description": "Nonsteroidal anti-inflammatory drug (NSAID)",
                "price": 7.99,
            },
            {
                "name": "Paracetamol",
                "description": "Pain reliever and fever reducer",
                "price": 4.99,
            },
        ]

        for drug_data in drugs:
            Drug.objects.create(**drug_data)

        # Orders
        orders = [
            {"username": "customer1", "drug_id": 1, "quantity": 2, "status": "pending"},
            {"username": "customer1", "drug_id": 2, "quantity": 1, "status": "shipped"},
        ]

        for order_data in orders:
            customer = User.objects.get(username=order_data["username"])
            drug = Drug.objects.get(id=order_data["drug_id"])
            Order.objects.create(
                customer=customer,
                drug=drug,
                quantity=order_data["quantity"],
                status=order_data["status"],
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database"))

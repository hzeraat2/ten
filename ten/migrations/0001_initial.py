# Generated by Django 3.1.5 on 2021-01-31 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
                ("remaining_count", models.PositiveIntegerField()),
                ("expiration_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("booking_count", models.PositiveIntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("max_bookings", models.PositiveIntegerField(default=0)),
                ("booked_date", models.DateTimeField(auto_now=True)),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ten.inventory"
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ten.member"
                    ),
                ),
            ],
        ),
    ]

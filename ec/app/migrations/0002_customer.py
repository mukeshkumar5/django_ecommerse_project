# Generated by Django 5.0 on 2024-01-03 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("mobile", models.ImageField(default=0, upload_to="")),
                ("zipcode", models.ImageField(upload_to="")),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Andhra Pradesh", "Andhra Pradesh"),
                            ("Arunachal Pradesh", "Arunachal Pradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Chhattisgarh", "Chhattisgarh"),
                            ("Goa", "Goa"),
                            ("Gujarat", "Gujarat"),
                            ("Haryana", "Haryana"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                            ("Jharkhand", "Jharkhand"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Maharashtra", "Maharashtra"),
                            ("Manipur", "Manipur"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Nagaland", "Nagaland"),
                            ("Odisha", "Odisha"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Sikkim", "Sikkim"),
                            ("Tamil Nadu", "Tamil Nadu"),
                            ("Telangana", "Telangana"),
                            ("Tripura", "Tripura"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Uttarakhand", "Uttarakhand"),
                            ("West Bengal", "West Bengal"),
                            (
                                "Andaman and Nicobar Islands",
                                "Andaman and Nicobar Islands",
                            ),
                            ("Chandigarh", "Chandigarh"),
                            (
                                "Dadra and Nagar Haveli and Daman and Diu",
                                "Dadra and Nagar Haveli and Daman and Diu",
                            ),
                            ("Delhi", "Delhi"),
                            ("Jammu and Kashmir", "Jammu and Kashmir"),
                            ("Ladakh", "Ladakh"),
                            ("Lakshadweep", "Lakshadweep"),
                            ("Puducherry", "Puducherry"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

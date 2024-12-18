# Generated by Django 5.1.3 on 2024-11-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_user_last_login_ip"),
    ]

    operations = [
        migrations.CreateModel(
            name="IPAddress",
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
                ("captured_ip_address", models.GenericIPAddressField(editable=False)),
            ],
        ),
    ]

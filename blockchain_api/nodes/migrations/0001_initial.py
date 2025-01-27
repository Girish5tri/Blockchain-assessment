# Generated by Django 5.1.5 on 2025-01-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlockchainNode",
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
                ("name", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=50)),
                ("uptime", models.FloatField()),
                ("resource_utilization", models.JSONField()),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_rename_createad_adds_rename_email_ctr_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("UserName", models.CharField(blank=True, max_length=100, null=True)),
                ("Email", models.CharField(blank=True, max_length=100, null=True)),
                ("Password", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

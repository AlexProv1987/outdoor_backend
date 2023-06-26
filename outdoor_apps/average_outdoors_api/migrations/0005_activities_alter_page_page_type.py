# Generated by Django 4.2.2 on 2023-06-26 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("average_outdoors_api", "0004_alter_page_page_type_delete_pagetype"),
    ]

    operations = [
        migrations.CreateModel(
            name="activities",
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
                ("activity_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="page",
            name="page_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="average_outdoors_api.activities",
            ),
        ),
    ]
# Generated by Django 4.2.14 on 2024-07-18 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_user_is_active_alter_user_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    7,
                    18,
                    12,
                    58,
                    33,
                    419971,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
    ]
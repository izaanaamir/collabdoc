# Generated by Django 4.2.14 on 2024-07-17 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "users",
            "0002_remove_user_updated_at_alter_user_created_at_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    7,
                    17,
                    13,
                    47,
                    33,
                    141950,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]

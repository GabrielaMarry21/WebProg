# Generated by Django 5.0.6 on 2024-06-19 02:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('eb49902b-fb4a-4ed2-9949-c924209ee510'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

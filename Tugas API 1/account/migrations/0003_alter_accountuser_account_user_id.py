# Generated by Django 5.0.6 on 2024-06-24 08:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('83e9968e-0abb-4292-9028-908534bbb431'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

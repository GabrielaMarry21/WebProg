# Generated by Django 5.0.6 on 2024-06-28 07:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('4e1ff725-3bb1-4156-a78d-a546138f704f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.UUIDField(default=uuid.UUID('a0dae52b-ae50-442f-9a4d-a621832551b7'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(editable=False, max_length=255)),
                ('course_created_by', models.CharField(max_length=255)),
                ('course_created_date', models.DateTimeField(auto_now_add=True)),
                ('course_updated_by', models.CharField(max_length=255, null=True)),
                ('course_updated_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('course_id',),
                'indexes': [models.Index(fields=['course_id'], name='account_cou_course__97ad3e_idx')],
            },
        ),
        migrations.CreateModel(
            name='AttendingCourse',
            fields=[
                ('attending_course_id', models.UUIDField(default=uuid.UUID('0ea6c3ad-29dd-4e02-bf07-e9a4eb1798cd'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('attending_account_profile_id', models.CharField(editable=False, max_length=255)),
                ('attending_course_created_by', models.CharField(max_length=255)),
                ('attending_course_created_date', models.DateTimeField(auto_now_add=True)),
                ('attending_course_updated_by', models.CharField(max_length=255, null=True)),
                ('attending_course_updated_date', models.DateTimeField(auto_now_add=True)),
                ('attending_courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.course')),
            ],
            options={
                'ordering': ('attending_course_id',),
                'indexes': [models.Index(fields=['attending_course_id', 'attending_courseid'], name='account_att_attendi_ade6c1_idx')],
            },
        ),
    ]
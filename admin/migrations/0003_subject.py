# Generated by Django 5.0.1 on 2024-01-09 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_alter_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptive_title', models.CharField(max_length=64, unique=True)),
                ('course_number', models.CharField(max_length=32, unique=True)),
                ('lecture_hours', models.IntegerField()),
                ('lab_hours', models.IntegerField()),
                ('units', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.course')),
            ],
        ),
    ]

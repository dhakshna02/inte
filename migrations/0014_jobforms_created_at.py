# Generated by Django 5.0.7 on 2024-08-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0013_alter_images_pagename'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobforms',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
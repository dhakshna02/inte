# Generated by Django 5.0.7 on 2024-08-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0014_jobforms_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobforms',
            name='created_at',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

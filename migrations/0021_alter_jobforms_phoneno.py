# Generated by Django 5.0.7 on 2024-09-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0020_alter_jobforms_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobforms',
            name='Phoneno',
            field=models.IntegerField(blank=True, max_length=12345678974, null=True),
        ),
    ]

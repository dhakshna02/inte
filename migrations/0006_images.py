# Generated by Django 5.0.7 on 2024-08-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0005_rename_mail_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagename', models.CharField(max_length=100)),
                ('requiredpictures', models.ImageField(upload_to='')),
            ],
        ),
    ]

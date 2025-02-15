# Generated by Django 5.0.7 on 2024-08-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0010_remove_masterdatamanagement_bgimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bigdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('subhead1', models.CharField(max_length=35)),
                ('subtxt1', models.CharField(max_length=400)),
                ('subhead2', models.CharField(max_length=50)),
                ('subtxt2', models.CharField(max_length=400)),
                ('subhead3', models.CharField(max_length=50)),
                ('subtxt3', models.CharField(max_length=400)),
                ('subhead4', models.CharField(max_length=50)),
                ('subtxt4', models.CharField(max_length=400)),
                ('lowerhead', models.CharField(max_length=30)),
                ('fsubhead1', models.CharField(max_length=25)),
                ('fsubtxt1', models.CharField(max_length=125)),
                ('fsubhead2', models.CharField(max_length=25)),
                ('fsubtxt2', models.CharField(max_length=125)),
                ('fsubhead3', models.CharField(max_length=25)),
                ('fsubtxt3', models.CharField(max_length=125)),
                ('fsubhead4', models.CharField(max_length=25)),
                ('fsubtxt4', models.CharField(max_length=125)),
            ],
        ),
    ]

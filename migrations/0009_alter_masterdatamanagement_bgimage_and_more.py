# Generated by Django 5.0.7 on 2024-08-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adr', '0008_masterdatamanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdatamanagement',
            name='Bgimage',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='masterdatamanagement',
            name='subimage2',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='masterdatamanagement',
            name='subimage3',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='masterdatamanagement',
            name='subimage4',
            field=models.URLField(),
        ),
    ]
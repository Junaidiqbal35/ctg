# Generated by Django 4.1.3 on 2022-11-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemaker',
            name='nyc_agency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'VIP'), (2, 'Agencyhead'), (3, 'Forum Irep'), (4, 'Forum Exec Committee'), (5, 'CTG Standing Committee')], null=True),
        ),
    ]
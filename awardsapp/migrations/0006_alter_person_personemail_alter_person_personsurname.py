# Generated by Django 4.0.1 on 2022-01-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0005_person_personagegroup_person_personfineornot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personEmail',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='personSurName',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
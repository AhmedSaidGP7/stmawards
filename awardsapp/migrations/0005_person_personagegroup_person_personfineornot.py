# Generated by Django 4.0.1 on 2022-01-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0004_person_persondoesheknow'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personAgeGroup',
            field=models.CharField(default='0', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='personFineorNot',
            field=models.CharField(default='fine', max_length=12),
            preserve_default=False,
        ),
    ]
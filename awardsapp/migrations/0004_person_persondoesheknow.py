# Generated by Django 4.0.1 on 2022-01-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0003_ips'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personDoesHeKnow',
            field=models.CharField(default='yes', max_length=12),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-18 06:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191117_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 6, 24, 58, 396192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 6, 24, 58, 396144, tzinfo=utc)),
        ),
    ]

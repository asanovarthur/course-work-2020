# Generated by Django 2.1.7 on 2020-03-06 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0021_auto_20200306_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 11, 13, 39, 327796)),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-28 21:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20191128_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_variants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer_variants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_order',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='flat',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], max_length=2)),
                ('price', models.IntegerField(max_length=2)),
                ('area', models.IntegerField(max_length=2)),
                ('status', models.CharField(choices=[('sold', 'გაყიდულია'), ('available', 'ხელმისაწვდომია'), ('reserved', 'დარეზერვებულია')], max_length=60)),
            ],
        ),
    ]

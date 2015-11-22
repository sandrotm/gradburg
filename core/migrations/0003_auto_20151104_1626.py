# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_flat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.IntegerField(),
        ),
    ]

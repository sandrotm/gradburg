# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151122_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='status',
            field=models.CharField(choices=[('sold', 'გაყიდულია'), ('available', 'თავისუფალია'), ('reserved', 'რეზერვ.')], max_length=60, default='available'),
        ),
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('schematic', 'სქემატური'), ('render', 'რენდერი'), ('photo', 'ფოტო')], max_length=95, default='photo'),
        ),
    ]

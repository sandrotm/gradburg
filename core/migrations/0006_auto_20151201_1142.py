# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151122_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_taken',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='status',
            field=models.CharField(choices=[('sold', 'გაყიდულია'), ('available', 'თავისუფალია'), ('reserved', 'რეზერვ.')], default='available', max_length=60),
        ),
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('schematic', 'სქემატური'), ('render', 'რენდერი'), ('photo', 'ფოტო')], default='photo', max_length=95),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151122_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='type',
            field=models.ForeignKey(to='core.FlatType', default=1),
        ),
        migrations.AlterField(
            model_name='flat',
            name='area',
            field=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='status',
            field=models.CharField(max_length=60, choices=[('sold', 'გაყიდულია'), ('available', 'ხელმისაწვდომია'), ('reserved', 'დარეზერვებულია')], default='available'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

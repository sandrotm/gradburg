# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151201_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatMeta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(choices=[('area', 'ფართობი'), ('sqm price', 'კვმ ფასი'), ('total price', 'ბინის ჯამური ფასი'), ('conditions', 'ჩაბარების პირობები'), ('standard areas', 'სტანდარტული გადატიხრვა')], max_length=190)),
                ('value', models.TextField()),
                ('title', models.CharField(max_length=190)),
            ],
        ),
        migrations.AlterField(
            model_name='flat',
            name='status',
            field=models.CharField(default='available', choices=[('sold', 'გაყიდულია'), ('available', 'იყიდება'), ('reserved', 'რეზერვ.')], max_length=60),
        ),
        migrations.AddField(
            model_name='flattype',
            name='meta',
            field=models.ManyToManyField(to='core.FlatMeta'),
        ),
    ]

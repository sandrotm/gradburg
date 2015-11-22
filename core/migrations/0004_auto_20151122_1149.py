# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151104_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=190)),
                ('descr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=190)),
                ('image', models.ImageField(height_field='height', upload_to='images', width_field='width')),
                ('type', models.CharField(choices=[('schematic', 'სქემატური'), ('render', 'რენდერი'), ('photo', 'ფოტო')], max_length=95, default='1')),
            ],
        ),
        migrations.AddField(
            model_name='flattype',
            name='images',
            field=models.ManyToManyField(to='core.Image', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(default='', blank=True, max_length=100)),
                ('description', models.TextField(default='', blank=True)),
                ('end', models.DateField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Testing'), (4, 'Done')], default=1)),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateField(null=True, blank=True)),
                ('due', models.DateField(null=True, blank=True)),
                ('completed', models.DateField(null=True, blank=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(blank=True, null=True, to='board.Sprint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

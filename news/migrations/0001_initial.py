# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('summary', models.CharField(max_length=500)),
                ('img_src', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
            ],
        ),
    ]

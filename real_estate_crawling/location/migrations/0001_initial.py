# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('area', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('agency', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_included', models.NullBooleanField()),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('html_id', models.CharField(blank=True, max_length=100, null=True)),
                ('last_change', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfferCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('street', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('finishTime', models.DateTimeField()),
                ('finishReason', models.CharField(max_length=200)),
                ('requestBytes', models.BigIntegerField()),
                ('responseBytes', models.BigIntegerField()),
                ('requestCount', models.BigIntegerField()),
                ('responseCount', models.BigIntegerField()),
                ('responseReceivedCount', models.BigIntegerField()),
                ('requestDepthMax', models.IntegerField()),
                ('requestStatusCount200', models.BigIntegerField()),
                ('requestStatusCount301', models.BigIntegerField()),
                ('requestStatusCount302', models.BigIntegerField()),
                ('requestStatusCount500', models.BigIntegerField()),
                ('requestStatusCount404', models.BigIntegerField()),
                ('dupeFiltered', models.BigIntegerField()),
                ('imgCount', models.BigIntegerField()),
                ('nbScrapedItems', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent_string', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.OfferCategory'),
        ),
        migrations.AddField(
            model_name='offer',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Place'),
        ),
        migrations.AddField(
            model_name='offer',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Source'),
        ),
    ]

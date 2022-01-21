# Generated by Django 3.0 on 2022-01-20 12:29

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='glasses')),
            ],
            options={
                'db_table': 'glass',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('units', models.CharField(max_length=128)),
                ('abv', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'db_table': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('iba', models.BooleanField(default=False)),
                ('color', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=6), default=list, size=None)),
                ('garnish', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), default=list, size=None)),
                ('recipe', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cocktails.Category')),
                ('glass', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cocktails.Glass')),
                ('ingredients', models.ManyToManyField(related_name='cocktails', to='cocktails.Ingredient')),
            ],
            options={
                'db_table': 'cocktail',
            },
        ),
    ]
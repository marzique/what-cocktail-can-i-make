# Generated by Django 3.0 on 2022-01-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_auto_20220120_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cocktails'),
        ),
    ]

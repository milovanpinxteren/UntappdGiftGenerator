# Generated by Django 5.0.3 on 2024-03-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftGenerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beers',
            name='brewery',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]

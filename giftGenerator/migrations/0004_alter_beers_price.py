# Generated by Django 5.0.3 on 2024-03-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftGenerator', '0003_beers_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beers',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]

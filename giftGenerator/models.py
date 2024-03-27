from django.db import models
from django.core.exceptions import ValidationError

def untappd_url_validator(value):
    if not value.startswith('https://untappd.com/v'):
        raise ValidationError('URL must start with https://untappd.com/v')

def https_url_validator(value):
    if not value.startswith('https://'):
        raise ValidationError('URL must start with https://')
class Venues(models.Model):
    name = models.CharField(max_length=250, default='', blank=True)
    untappd_url = models.URLField(validators=[untappd_url_validator])
    venue_website_url = models.URLField(validators=[https_url_validator])


class Beers(models.Model):
    name = models.CharField(max_length=250, default='', blank=True)
    brewery = models.CharField(max_length=250, default='', blank=True)
    venue = models.ForeignKey(Venues, on_delete=models.CASCADE)
    untappd_url = models.URLField(validators=[untappd_url_validator], null=True)
    venue_website_url = models.URLField(validators=[https_url_validator], null=True)
    abv = models.FloatField(default=0, null=True)
    ibu = models.FloatField(default=0, null=True)
    rating = models.FloatField(default=0, null=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2, null=True)
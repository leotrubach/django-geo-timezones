from django.db import models
from django.contrib.gis.db.models import PolygonField

__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'


class TimezoneManager(models.Manager):

    def find(self, point):
        return self.filter(geom__contains=point).first()


class Timezone(models.Model):

    class Meta:
        app_label = 'geo_timezones'

    timezone = models.CharField(max_length=30)
    geom = PolygonField()

    objects = TimezoneManager()

    def __str__(self):
        return self.timezone

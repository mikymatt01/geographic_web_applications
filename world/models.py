from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, null=True)
    area = models.IntegerField(null=True)
    pop2005 = models.IntegerField('Population 2005', null=True)
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2, null=True)
    iso3 = models.CharField('3 Digit ISO', max_length=3, null=True)
    un = models.IntegerField('United Nations Code', null=True)
    region = models.IntegerField('Region Code', null=True)
    subregion = models.IntegerField('Sub-Region Code', null=True)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

'''
conversione wsg84 to lat lng
from django.contrib.gis.geos import Point
pnt = Point(30, 50, srid=4326)#srid di standard wsg84 (lat, lng)
desired_srid = 32140  23032#srid dello standard 
pnt.transform(desired_srid)
pnt.ewkt
'''
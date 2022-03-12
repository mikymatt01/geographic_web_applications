from django.contrib.gis.db import models

class Italy(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    fid  = models.IntegerField(null=True)
    cod_rip  = models.IntegerField(null=True)
    cod_reg  = models.IntegerField(null=True)
    cod_prov  = models.IntegerField(null=True)
    cod_cm  = models.IntegerField(null=True)
    cod_uts  = models.IntegerField(null=True)
    pro_com = models.IntegerField(null=True)
    pro_com_t = models.CharField(max_length=6, null=True)
    comune = models.CharField('comune', max_length=34, null=True)
    comune_a  = models.CharField('comune_a', max_length=36, null=True)
    cc_uts = models.IntegerField(null=True)
    shape_Leng = models.FloatField(null=True)
    GlobalID = models.CharField(max_length=38, null=True)
    SHAPE_Le_1 = models.FloatField(null=True)
    shape_Area = models.FloatField(null=True)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.comune

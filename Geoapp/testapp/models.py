from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
class Country(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.GeometryField()

    class  Meta:  
        verbose_name_plural  =  "Countries"


    def _str_(self):
        return self.name
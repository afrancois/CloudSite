from django.db import models
from autoslug import AutoSlugField
from geoposition.fields import GeopositionField
import uuid
# Create your models here.

def _slug_default_():
        return uuid.uuid4()

class CurrentState(models.Model):

    RGB = 1
    DISCO = 2
    BLUE_SKY = 3
    NIGHT = 4
    OVERCAST = 5
    GOLDEN = 6
    SNOW = 7
    LIGHTNING = 8
    OUTSIDE = 0

    STATE_CHOICES = (
        ( RGB, 'RGB Color'),
        ( DISCO, 'Disco Mode'),
        ( BLUE_SKY, 'Blue Sky'),
        ( NIGHT, 'Night Time'),
        ( OVERCAST, 'Overcast'),
        ( GOLDEN,'Golden'),
        ( SNOW,'Snow'),
        ( LIGHTNING,'Lightning'),
        ( OUTSIDE,"What it's doing outside"),
    )



    created = models.DateTimeField(auto_now_add=True)
    cloud_title = models.CharField(max_length=100,blank=False,default='new cloud',unique=True)
    cloud_slug = AutoSlugField(max_length=100,blank=False,populate_from='cloud_title',unique=True,always_update=True,default=_slug_default_)
    cloud_state = models.IntegerField(choices=STATE_CHOICES,blank=False,default=OUTSIDE)
    cloud_rgb = models.CharField(max_length=7,blank=False,default='#ffffff')
    position = GeopositionField()



    def __unicode__(self):
        return self.cloud_title

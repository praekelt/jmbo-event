from django.db import models

from ckeditor.fields import RichTextField
from content.models import ModelBase
from show.models import ShowContributor

PROVINCES = (
    ('Eastern Cape', 'Eastern Cape'),
    ('Free State', 'Free State'),
    ('Gauteng', 'Gauteng'),
    ('KwaZulu-Natal', 'KwaZulu-Natal'),
    ('Limpopo', 'Limpopo'),
    ('Mpumalanga', 'Mpumalanga'),
    ('Northern Cape', 'Northern Cape'),
    ('North-West', 'North-West'),
    ('Western Cape', 'Western Cape'),
)
    
class Location(models.Model):
    city = models.CharField(max_length=255, help_text='Name of the city.')
    province = models.CharField(
        choices=PROVINCES,
        max_length=255,
        help_text='Name of the province.'
    )

    def __unicode__(self):
        return "%s, %s" % (self.city, self.province)

class Venue(models.Model):
    name = models.CharField(max_length=255, help_text='A short descriptive name.')
    address = models.CharField(max_length=512, help_text='Physical venue address.')
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        help_text='Location of the venue.'
    )

    def __unicode__(self):
        return self.name

class Event(ModelBase):
    venue = models.ForeignKey(
        Venue,
        help_text='Venue where the event will take place.'
    )
    content = RichTextField(help_text='Full article detailing this event.')

class Appearance(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='apearances'
    )
    show_contributor = models.ForeignKey(
        ShowContributor,
        related_name='apearances'
    )

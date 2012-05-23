from django.db import models
from mezzanine.core.models import Displayable, RichTextField

class Micropage(Displayable):
    PAGETYPE_CHOICES = (
        (u'Subpage', u'Subpage'),
        (u'Home', u'Home'),
    )
    page_type = models.CharField(max_length=8, choices=PAGETYPE_CHOICES, default='Subpage')
    header_top_left = RichTextField(blank=True, verbose_name="Header Top Left")
    header_top_right = RichTextField(blank=True, verbose_name="Header Top Right")
    header_middle_left = RichTextField(blank=True, verbose_name="Header Bottom Left")
    header_middle_right = RichTextField(blank=True, verbose_name="Header Bottom Right")
    body_left_column_top = RichTextField(blank=True, verbose_name="Body Column Left Top")
    body_left_column_bottom = RichTextField(blank=True, verbose_name="Body Column Left Bottom")
    body_middle_column_top = RichTextField(blank=True, verbose_name="Body Column Middle Top")
    body_middle_column_bottom = RichTextField(blank=True, verbose_name="Body Column Middle Bottom")
    body_right_column = RichTextField(blank=True, verbose_name="Body Column Right Bottom")
    event_details = RichTextField(blank=True, verbose_name="Event Details")
    footer = RichTextField(blank=True, verbose_name="Footer")


    def __unicode__(self):
        return self.title

class Event(models.Model):
    event_date = models.DateField(verbose_name="Date", blank=True, null=True)
    event = models.CharField(max_length=400, verbose_name="Event")
    location = models.CharField(max_length=400, verbose_name="Location")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    
    def __unicode__(self):
        return self.event


from django.db import models
from django.utils.timezone import now


class Being(models.Model):
    """Living being objects"""
    name = models.CharField(max_length=30, unique=True)
    birth = models.DateTimeField(default=now, blank=True)
    routine = models.TextField(blank=True) # Python 
    # weight = models.DecimalField(max_digits=7, decimal_places=3, default=1)
    # color

    def __unicode__(self):
        return self.name

    def speak(self, message):
        # TODO
        print('{} speaks: {}'.format(self, message))

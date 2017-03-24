from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CY(models.Model):
    name = models.CharField(max_length=30)
    spell = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    derivation = models.CharField(max_length=1024)
    samples = models.CharField(max_length=1024)
    first = models.CharField(max_length=24)
    last = models.CharField(max_length=24)

    def __unicode__(self):
        return u'%s  %s  ' % (self.id, self.name)


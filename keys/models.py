from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=40)
    def __unicode__(self):
        return self.address
# Create your models here.

from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Land(models.Model):
    address = models.CharField(max_length=60)
    postalCode = models.CharField(max_length=60)
    sqrAcres = models.DecimalField(max_digits=1000, decimal_places=3)

    def __str__(self):
        return self.address + self.postalCode
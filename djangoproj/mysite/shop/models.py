from __future__ import unicode_literals

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
from django.db import models
# Create your models here.
from django.db.models import ForeignKey
from django.utils.timezone import now


@python_2_unicode_compatible  # only if you need to support Python 2
class Product(models.Model):

    product_name = models.CharField(max_length=300, blank=True)
    official_price = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    in_cart_number= models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

@python_2_unicode_compatible  # only if you need to support Python 2
class Image(models.Model):

    related_to_product = ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    name = models.CharField(max_length=300, default='default')

    def __str__(self):
        return self.name

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from travelize.address.models import Address


@python_2_unicode_compatible
class Diller(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'))
    name = models.CharField(_('Name of User'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=255)
    address = models.ManyToManyField(Address, _('addresses'),
                                     db_table='diller_addresses')
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default='1')
    airport = models.CharField(_('Airport'), blank=True, max_length=255)
    image = models.ImageField(upload_to="event_image", blank=True, )

    def __str__(self):
        return 'Diller: %s, Products %s' % (self.name, self.product_dillers.values_list('pk', flat=True))

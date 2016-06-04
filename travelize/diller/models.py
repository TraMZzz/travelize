# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from travelize.address.models import Address


@python_2_unicode_compatible
class Diller(models.Model):
    name = models.CharField(_('Name of User'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=255)
    address = models.ManyToManyField(Address, _('addresses'),
                                     db_table='diller_addresses')
    airport = models.CharField(_('Airport'), blank=True, max_length=255)

    def __str__(self):
        return 'Diller: %s, Products %s' % (self.name, self.product_dillers.values_list('pk', flat=True))

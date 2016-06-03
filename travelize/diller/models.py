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

    def __str__(self):
        return self.name
